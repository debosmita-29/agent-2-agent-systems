from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:
    tool_name: str
    success: bool
    message: str
    data: dict[str, Any]
