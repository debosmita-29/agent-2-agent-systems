from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    message: str
    knowledge: list[dict] = field(default_factory=list)
    memories: list[dict] = field(default_factory=list)


@dataclass
class AgentResult:
    agent_name: str
    summary: str
    actions: list[str]
    tool_outputs: list[dict[str, Any]]
    data: dict[str, Any] = field(default_factory=dict)
