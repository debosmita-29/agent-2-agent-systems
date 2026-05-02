import json

from multi_ai_agent_systems.agents.base import AgentContext
from multi_ai_agent_systems.agents.finance_agent import FinanceAgent
from multi_ai_agent_systems.agents.grocery_agent import GroceryAgent
from multi_ai_agent_systems.agents.health_agent import HealthAgent
from multi_ai_agent_systems.agents.memory_agent import MemoryAgent
from multi_ai_agent_systems.agents.research_agent import ResearchAgent
from multi_ai_agent_systems.agents.schedule_agent import ScheduleAgent
from multi_ai_agent_systems.agents.travel_agent import TravelAgent
from multi_ai_agent_systems.llm.client import LLMClient
from multi_ai_agent_systems.memory.vector_memory import VectorMemory
from multi_ai_agent_systems.orchestration.router import IntentRouter
from multi_ai_agent_systems.rag.retriever import Retriever
from multi_ai_agent_systems.tools.registry import ToolRegistry


class AgentOrchestrator:
    def __init__(self, repository):
        self.repository = repository
        self.router = IntentRouter()
        self.llm = LLMClient()
        self.retriever = Retriever(repository)
        self.memory = VectorMemory(repository)
        self.tools = ToolRegistry(repository)
        self.agents = {
            "memory": MemoryAgent(),
            "schedule": ScheduleAgent(),
            "grocery": GroceryAgent(),
            "finance": FinanceAgent(),
            "health": HealthAgent(),
            "travel": TravelAgent(),
            "research": ResearchAgent(),
        }

    async def run(self, message: str) -> dict:
        selected_agents = self.router.route(message)
        knowledge = self.retriever.search(message)
        memories = self.memory.search(message)
        context = AgentContext(message=message, knowledge=knowledge, memories=memories)

        results = []
        for agent_name in selected_agents:
            result = await self.agents[agent_name].run(context, self.repository, self.tools)
            results.append(result)

        final_answer = await self._synthesize(message, selected_agents, results, knowledge, memories)
        run = self.repository.add_agent_run(message, selected_agents, final_answer)

        return {
            "run_id": run.id,
            "message": message,
            "selected_agents": selected_agents,
            "answer": final_answer,
            "agent_results": [r.__dict__ for r in results],
            "knowledge": knowledge,
            "memories": memories,
        }

    async def _synthesize(self, message, selected_agents, results, knowledge, memories) -> str:
        payload = {
            "user_request": message,
            "selected_agents": selected_agents,
            "actions": [{"agent": r.agent_name, "summary": r.summary, "actions": r.actions} for r in results],
            "knowledge": knowledge,
            "memories": memories,
        }

        return await self.llm.complete(
            system_prompt=(
                "You are the final response layer for a practical family operations multi-agent system. "
                "Summarize what was done and recommend next steps."
            ),
            user_prompt=json.dumps(payload, indent=2),
        )
