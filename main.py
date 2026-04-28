"""
FastAPI backend for IPL RAG Search Engine.
LLM: Ollama (free, runs locally)
Endpoints:
  POST /search  — RAG query (retrieve + generate)
  POST /ingest  — Add new documents
  GET  /stats   — Collection stats
  GET  /health  — Health check
"""

from app.rag_engine import RAGEngine
from typing import List, Optional
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import httpx
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ─────────────────────────────────────────────
# App setup
# ─────────────────────────────────────────────

app = FastAPI(
    title="IPL RAG Search Engine",
    description="Ask anything about IPL — powered by RAG + Ollama (free!)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialise RAG engine once at startup
rag = RAGEngine(persist_directory="./chroma_db")

# Ollama config — runs locally on your machine, 100% free
OLLAMA_URL = "http://localhost:11434/api/chat"
# change to "mistral" or "phi3" if you prefer
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3")


# ─────────────────────────────────────────────
# Schemas
# ─────────────────────────────────────────────

class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5


class SearchResponse(BaseModel):
    query: str
    answer: str
    sources: List[dict]
    total_chunks_searched: int


class IngestDocument(BaseModel):
    id: str
    text: str
    metadata: Optional[dict] = {}


class IngestRequest(BaseModel):
    documents: List[IngestDocument]


# ─────────────────────────────────────────────
# LLM call — Ollama (free, local)
# ─────────────────────────────────────────────

async def generate_answer(query: str, context: str) -> str:
    """Call local Ollama model with retrieved context to generate an answer."""

    prompt = f"""You are an expert IPL (Indian Premier League) cricket analyst.
Use ONLY the context below to answer the question. Be concise and enthusiastic about cricket.
If the context doesn't have enough info, say so honestly.

Context:
{context}

Question: {query}

Answer:"""

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                }
            )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=502,
                    detail=f"Ollama error: {response.text}. Make sure Ollama is running!"
                )

            data = response.json()
            return data["message"]["content"]

    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="Cannot connect to Ollama. Is it running? Run: ollama serve"
        )


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")


@app.get("/health")
async def health():
    # Check if Ollama is reachable
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            r = await client.get("http://localhost:11434")
            ollama_status = "running" if r.status_code == 200 else "error"
    except Exception:
        ollama_status = "not running"

    return {"status": "ok", "ollama": ollama_status, "model": OLLAMA_MODEL}


@app.get("/stats")
async def stats():
    return rag.stats()


@app.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    """
    RAG Pipeline:
      1. Embed query
      2. Retrieve top-K similar chunks from ChromaDB
      3. Build context from chunks
      4. Call Claude with context + query
      5. Return answer + sources
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    # Step 1 & 2: Retrieve relevant chunks
    chunks = rag.retrieve(request.query, top_k=request.top_k)

    # Step 3: Build context string
    context = rag.build_context(chunks)

    # Step 4: Generate answer with LLM
    answer = await generate_answer(request.query, context)

    # Step 5: Format sources for response
    sources = [
        {
            "text": c["text"][:200] + "..." if len(c["text"]) > 200 else c["text"],
            "category": c["metadata"].get("category", "unknown"),
            "relevance_score": round(1 - c["distance"], 3),
        }
        for c in chunks
    ]

    return SearchResponse(
        query=request.query,
        answer=answer,
        sources=sources,
        total_chunks_searched=rag.collection.count(),
    )


@app.post("/ingest")
async def ingest(request: IngestRequest):
    """Add new documents to the knowledge base."""
    docs = [
        {"id": d.id, "text": d.text, "metadata": d.metadata}
        for d in request.documents
    ]
    rag.add_documents(docs)
    return {"message": f"Successfully ingested {len(docs)} documents."}
