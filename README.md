# 🏏 IPL RAG Search Engine

Ask anything about IPL — powered by **ChromaDB + sentence-transformers **.

## Architecture

```
User Query
    │
    ▼
[ FastAPI /search ]
    │
    ▼
[ sentence-transformers ]  ← embed query (local, free)
    │
    ▼
[ ChromaDB ]  ← cosine similarity → top-5 chunks
    │
    ▼
[ Claude API ]  ← context + query → answer
    │
    ▼
[ JSON response ]  → frontend
```

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your Anthropic API key
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Run the server
```bash
uvicorn main:app --reload --port 8000
```

### 4. Open in browser
```
http://localhost:8000
```

---

## API Endpoints

### `POST /search`
RAG query — retrieve + generate.

**Request:**
```json
{
  "query": "Who has scored the most runs in IPL?",
  "top_k": 5
}
```

**Response:**
```json
{
  "query": "Who has scored the most runs in IPL?",
  "answer": "Virat Kohli is the all-time leading run scorer...",
  "sources": [
    {
      "text": "Virat Kohli is the all-time...",
      "category": "player",
      "relevance_score": 0.923
    }
  ],
  "total_chunks_searched": 25
}
```

### `POST /ingest`
Add new documents to the knowledge base.

```json
{
  "documents": [
    {
      "id": "match_001",
      "text": "MI vs CSK final 2023 — CSK won by 5 wickets...",
      "metadata": { "category": "match", "season": "2023" }
    }
  ]
}
```

### `GET /stats`
Returns collection info.

### `GET /health`
Health check.

---

## Adding More IPL Data

Edit `data/ipl_data.py` and add more entries to `IPL_DOCUMENTS`. Each document needs:
- `id` — unique string
- `text` — the knowledge chunk (1–3 paragraphs)
- `metadata` — dict with `category` and other tags

Then **delete the `chroma_db/` folder** and restart the server to re-ingest.

Alternatively, use the `/ingest` endpoint at runtime to add documents without restarting.

---

## Tech Stack

| Component | Library | Why |
|-----------|---------|-----|
| API | FastAPI | Fast, async, auto-docs |
| Vector DB | ChromaDB | Local, persistent, easy |
| Embeddings | sentence-transformers | Free, runs locally |
| LLM | Claude (Anthropic) | Best answer quality |
| Frontend | Vanilla HTML/CSS/JS | Zero dependencies |
