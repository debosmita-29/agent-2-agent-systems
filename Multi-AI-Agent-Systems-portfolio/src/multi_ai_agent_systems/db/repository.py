import json
from sqlalchemy.orm import Session

from multi_ai_agent_systems.db.models import AgentRun, ExpenseItem, KnowledgeDocument, MemoryItem, TaskItem


class Repository:
    def __init__(self, db: Session):
        self.db = db

    def add_memory(self, namespace: str, key: str, value: str, embedding: list[float] | None = None):
        item = MemoryItem(
            namespace=namespace,
            key=key,
            value=value,
            embedding_json=json.dumps(embedding) if embedding else None,
        )
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_memory(self, namespace: str | None = None, limit: int = 50):
        query = self.db.query(MemoryItem)
        if namespace:
            query = query.filter(MemoryItem.namespace == namespace)
        return query.order_by(MemoryItem.created_at.desc()).limit(limit).all()

    def add_document(self, title: str, content: str, source: str = "manual"):
        doc = KnowledgeDocument(title=title, content=content, source=source)
        self.db.add(doc)
        self.db.commit()
        self.db.refresh(doc)
        return doc

    def list_documents(self):
        return self.db.query(KnowledgeDocument).order_by(KnowledgeDocument.created_at.desc()).all()

    def add_task(self, agent: str, title: str, details: str = "", priority: str = "normal", due_at: str | None = None):
        task = TaskItem(agent=agent, title=title, details=details, priority=priority, due_at=due_at)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def list_tasks(self, status: str | None = None):
        query = self.db.query(TaskItem)
        if status:
            query = query.filter(TaskItem.status == status)
        return query.order_by(TaskItem.created_at.desc()).limit(100).all()

    def add_expense(self, category: str, amount: float, note: str = ""):
        expense = ExpenseItem(category=category, amount=amount, note=note)
        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense

    def list_expenses(self):
        return self.db.query(ExpenseItem).order_by(ExpenseItem.created_at.desc()).limit(100).all()

    def add_agent_run(self, user_message: str, selected_agents: list[str], final_answer: str, status: str = "completed"):
        run = AgentRun(
            user_message=user_message,
            selected_agents=json.dumps(selected_agents),
            final_answer=final_answer,
            status=status,
        )
        self.db.add(run)
        self.db.commit()
        self.db.refresh(run)
        return run
