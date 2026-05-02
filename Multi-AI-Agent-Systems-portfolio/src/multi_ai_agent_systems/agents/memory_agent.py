from multi_ai_agent_systems.agents.base import AgentContext, AgentResult
from multi_ai_agent_systems.memory.vector_memory import VectorMemory


class MemoryAgent:
    name = "memory"
    description = "Stores and retrieves long-term context."
    skill_file = "skills/memory_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        memory = VectorMemory(repository)
        stored = memory.add("general", "latest_user_request", context.message)
        matches = memory.search(context.message, top_k=5)
        return AgentResult(
            self.name,
            "Updated memory and retrieved relevant context.",
            ["Stored latest request in memory", "Retrieved related memory"],
            [],
            {"stored": stored, "matches": matches},
        )
