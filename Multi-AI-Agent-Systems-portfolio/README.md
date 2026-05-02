# Multi-AI-Agent-Systems

Portfolio-grade multi-agent AI platform for family and personal operations.

## Features

- FastAPI backend
- Streamlit UI
- LangGraph-ready orchestration adapter
- CrewAI-ready agent mapping
- Real LLM support: OpenAI, Anthropic Claude, Ollama, or local fallback
- Tool calling layer for Gmail, Calendar, reminders, expenses, and APIs
- Persistent database: SQLite locally, Postgres in Docker
- pgvector-ready memory architecture
- Celery background workers
- Redis queue
- Agent skill files and `AGENTS.md`
- Docker Compose
- Tests and GitHub Actions CI

## Architecture

```text
User / UI / API
   |
   v
FastAPI Gateway
   |
   v
Agent Orchestrator
   |
   +-- Memory Agent
   +-- Schedule Agent
   +-- Grocery Agent
   +-- Health Agent
   +-- Finance Agent
   +-- Travel Agent
   +-- Research Agent
   |
   v
Tool Registry
   |
   +-- Reminder Tool
   +-- Expense Tool
   +-- Gmail Tool
   +-- Calendar Tool
   |
   v
Postgres + pgvector-ready Memory
   |
   v
Celery Background Workers
```

## Quick start without Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
python scripts/init_db.py
uvicorn multi_ai_agent_systems.api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run UI

```bash
streamlit run ui/streamlit_app.py
```

## Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

Services:

- API: http://localhost:8000/docs
- UI: http://localhost:8501
- Postgres: localhost:5432
- Redis: localhost:6379

## LLM providers

Default local mode:

```env
LLM_PROVIDER=rule_based
```

OpenAI:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
```

Claude:

```env
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_key
ANTHROPIC_MODEL=claude-3-5-sonnet-latest
```

Ollama:

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1
```

## API demo

```bash
curl -X POST http://127.0.0.1:8000/agents/run \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan my week, add grocery reminders, and track bills"}'
```

## Background job demo

```bash
curl -X POST http://127.0.0.1:8000/jobs/agent-run \
  -H "Content-Type: application/json" \
  -d '{"message":"Create a weekend travel checklist"}'
```

## Agent docs

- `AGENTS.md`
- `agents_md/`
- `skills/`

## Portfolio talking points

This project demonstrates agentic orchestration, persistent memory, RAG grounding, tool execution, async jobs, and human-centered AI system design.
