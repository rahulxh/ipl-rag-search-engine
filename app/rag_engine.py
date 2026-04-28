"""
RAG Engine - Handles embeddings, vector storage, and retrieval.
Uses ChromaDB for vector store and sentence-transformers for embeddings.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import chromadb
from chromadb.utils import embedding_functions
from data.ipl_data import IPL_DOCUMENTS
from typing import List, Dict, Any


# ─────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────
COLLECTION_NAME = "ipl_knowledge_base"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"   # small, fast, free
TOP_K = 5                               # number of chunks to retrieve


class RAGEngine:
    """
    Retrieval-Augmented Generation engine for IPL search.

    Flow:
      1. Ingest documents → embed → store in ChromaDB
      2. Query → embed query → similarity search → retrieve top-K chunks
      3. Chunks + query → LLM (Claude) → final answer
    """

    def __init__(self, persist_directory: str = "./chroma_db"):
        print("🏏 Initialising IPL RAG Engine...")

        # Embedding function (runs locally, no API key needed)
        self.ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL
        )

        # ChromaDB client (persists to disk)
        self.client = chromadb.PersistentClient(path=persist_directory)

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"}
        )

        # Ingest data if collection is empty
        if self.collection.count() == 0:
            print("📚 Ingesting IPL documents into ChromaDB...")
            self._ingest_documents()
        else:
            print(f"✅ Collection ready with {self.collection.count()} documents.")

    # ─────────────────────────────────────────
    # Ingestion
    # ─────────────────────────────────────────

    def _ingest_documents(self):
        """Embed and store all IPL documents."""
        ids = [doc["id"] for doc in IPL_DOCUMENTS]
        texts = [doc["text"] for doc in IPL_DOCUMENTS]
        metadatas = [doc["metadata"] for doc in IPL_DOCUMENTS]

        self.collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas
        )
        print(f"✅ Ingested {len(IPL_DOCUMENTS)} IPL documents.")

    def add_documents(self, documents: List[Dict[str, Any]]):
        """Add new documents dynamically at runtime."""
        ids = [doc["id"] for doc in documents]
        texts = [doc["text"] for doc in documents]
        metadatas = [doc.get("metadata", {}) for doc in documents]

        self.collection.add(ids=ids, documents=texts, metadatas=metadatas)
        print(f"✅ Added {len(documents)} new documents.")

    # ─────────────────────────────────────────
    # Retrieval
    # ─────────────────────────────────────────

    def retrieve(self, query: str, top_k: int = TOP_K) -> List[Dict]:
        """
        Embed the query and return the top-K most similar chunks.
        Returns list of dicts with 'text', 'metadata', and 'distance'.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=min(top_k, self.collection.count())
        )

        chunks = []
        for i, doc in enumerate(results["documents"][0]):
            chunks.append({
                "text": doc,
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
            })
        return chunks

    # ─────────────────────────────────────────
    # Context builder
    # ─────────────────────────────────────────

    def build_context(self, chunks: List[Dict]) -> str:
        """Format retrieved chunks into a context string for the LLM."""
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            meta = chunk["metadata"]
            label = meta.get("category", "info").upper()
            context_parts.append(f"[{i}] [{label}]\n{chunk['text']}")
        return "\n\n".join(context_parts)

    # ─────────────────────────────────────────
    # Stats
    # ─────────────────────────────────────────

    def stats(self) -> Dict:
        return {
            "total_documents": self.collection.count(),
            "collection_name": COLLECTION_NAME,
            "embedding_model": EMBEDDING_MODEL,
        }
