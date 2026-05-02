from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from multi_ai_agent_systems.db.base import Base


class MemoryItem(Base):
    __tablename__ = "memory_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    namespace: Mapped[str] = mapped_column(String(80), index=True, default="general")
    key: Mapped[str] = mapped_column(String(160), index=True)
    value: Mapped[str] = mapped_column(Text)
    embedding_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class KnowledgeDocument(Base):
    __tablename__ = "knowledge_documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    content: Mapped[str] = mapped_column(Text)
    source: Mapped[str] = mapped_column(String(200), default="manual")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_message: Mapped[str] = mapped_column(Text)
    selected_agents: Mapped[str] = mapped_column(Text)
    final_answer: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(40), default="completed")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class TaskItem(Base):
    __tablename__ = "task_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    agent: Mapped[str] = mapped_column(String(80), index=True)
    title: Mapped[str] = mapped_column(String(240))
    details: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(40), default="open")
    priority: Mapped[str] = mapped_column(String(40), default="normal")
    due_at: Mapped[str | None] = mapped_column(String(80), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class ExpenseItem(Base):
    __tablename__ = "expense_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category: Mapped[str] = mapped_column(String(80), index=True)
    amount: Mapped[float] = mapped_column(Float)
    note: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
