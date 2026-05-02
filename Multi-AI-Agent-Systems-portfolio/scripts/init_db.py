from pathlib import Path

from multi_ai_agent_systems.db.base import Base, SessionLocal, engine
from multi_ai_agent_systems.db.repository import Repository

Path("data").mkdir(exist_ok=True)
Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    repo = Repository(db)
    if not repo.list_documents():
        repo.add_document(
            "Family AI Operating Principles",
            "Prioritize privacy, reliability, memory, reminders, and useful tool execution.",
            "seed",
        )
        repo.add_document(
            "Multi-Agent Architecture",
            "Use an orchestrator to route requests to specialist agents. Each agent owns a domain.",
            "seed",
        )
        repo.add_document(
            "Enterprise Extension",
            "Scale with RBAC, audit trails, observability, model governance, and CI/CD testing.",
            "seed",
        )
finally:
    db.close()

print("Database initialized.")
