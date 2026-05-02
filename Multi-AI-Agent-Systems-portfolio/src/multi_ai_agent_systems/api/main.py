from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from multi_ai_agent_systems.api.schemas import AgentRunRequest, KnowledgeCreateRequest, MemoryCreateRequest
from multi_ai_agent_systems.config import settings
from multi_ai_agent_systems.db.base import Base, engine, get_db
from multi_ai_agent_systems.db.repository import Repository
from multi_ai_agent_systems.orchestration.engine import AgentOrchestrator
from multi_ai_agent_systems.worker.tasks import run_agent_job

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name, "env": settings.env}


@app.post("/agents/run")
async def run_agents(request: AgentRunRequest, db: Session = Depends(get_db)):
    return await AgentOrchestrator(Repository(db)).run(request.message)


@app.post("/jobs/agent-run")
def enqueue_agent_run(request: AgentRunRequest):
    job = run_agent_job.delay(request.message)
    return {"job_id": job.id, "status": "queued"}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    result = run_agent_job.AsyncResult(job_id)
    return {"job_id": job_id, "status": result.status, "result": result.result if result.ready() else None}


@app.post("/memory")
def add_memory(request: MemoryCreateRequest, db: Session = Depends(get_db)):
    item = Repository(db).add_memory(request.namespace, request.key, request.value)
    return {"id": item.id, "namespace": item.namespace, "key": item.key, "value": item.value}


@app.get("/memory")
def list_memory(namespace: str | None = None, db: Session = Depends(get_db)):
    items = Repository(db).get_memory(namespace=namespace)
    return [{"id": i.id, "namespace": i.namespace, "key": i.key, "value": i.value} for i in items]


@app.post("/knowledge")
def add_knowledge(request: KnowledgeCreateRequest, db: Session = Depends(get_db)):
    doc = Repository(db).add_document(request.title, request.content, request.source)
    return {"id": doc.id, "title": doc.title, "source": doc.source}


@app.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return [
        {
            "id": t.id,
            "agent": t.agent,
            "title": t.title,
            "details": t.details,
            "status": t.status,
            "priority": t.priority,
            "due_at": t.due_at,
        }
        for t in Repository(db).list_tasks()
    ]


@app.get("/expenses")
def list_expenses(db: Session = Depends(get_db)):
    return [
        {
            "id": e.id,
            "category": e.category,
            "amount": e.amount,
            "note": e.note,
            "created_at": e.created_at.isoformat(),
        }
        for e in Repository(db).list_expenses()
    ]
