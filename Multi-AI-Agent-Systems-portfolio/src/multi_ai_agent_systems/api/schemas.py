from pydantic import BaseModel, Field


class AgentRunRequest(BaseModel):
    message: str = Field(..., min_length=2)


class MemoryCreateRequest(BaseModel):
    namespace: str = "general"
    key: str
    value: str


class KnowledgeCreateRequest(BaseModel):
    title: str
    content: str
    source: str = "manual"
