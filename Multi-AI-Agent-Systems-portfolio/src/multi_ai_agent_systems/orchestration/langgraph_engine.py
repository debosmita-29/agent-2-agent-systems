from multi_ai_agent_systems.orchestration.engine import AgentOrchestrator


class LangGraphOrchestratorAdapter:
    """LangGraph-ready adapter.

    Keeps the project runnable without requiring LangGraph at install time.
    When LangGraph is installed, replace the fallback with a StateGraph:
    START -> route -> memory -> specialist agents -> synthesize -> END.
    """

    def __init__(self, repository):
        self.fallback = AgentOrchestrator(repository)

    async def run(self, message: str) -> dict:
        return await self.fallback.run(message)


LANGGRAPH_DESIGN = """
from langgraph.graph import StateGraph, START, END

graph = StateGraph(AgentState)
graph.add_node("route", route_node)
graph.add_node("memory", memory_node)
graph.add_node("specialists", specialist_node)
graph.add_node("synthesize", synthesize_node)

graph.add_edge(START, "route")
graph.add_edge("route", "memory")
graph.add_edge("memory", "specialists")
graph.add_edge("specialists", "synthesize")
graph.add_edge("synthesize", END)

compiled = graph.compile()
"""
