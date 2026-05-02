from multi_ai_agent_systems.agents.base import AgentContext, AgentResult


class ResearchAgent:
    name = "research"
    description = "Uses RAG context and API hooks to support planning."
    skill_file = "skills/research_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        return AgentResult(
            self.name,
            "Reviewed retrieved knowledge for decision support.",
            ["Used RAG context to support the final answer"],
            [],
            {"knowledge_used": context.knowledge},
        )
