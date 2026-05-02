import asyncio

from multi_ai_agent_systems.db.base import Base, SessionLocal, engine
from multi_ai_agent_systems.db.repository import Repository
from multi_ai_agent_systems.orchestration.engine import AgentOrchestrator
from multi_ai_agent_systems.worker.celery_app import celery_app


@celery_app.task(name="run_agent_job")
def run_agent_job(message: str) -> dict:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        return asyncio.run(AgentOrchestrator(Repository(db)).run(message))
    finally:
        db.close()
