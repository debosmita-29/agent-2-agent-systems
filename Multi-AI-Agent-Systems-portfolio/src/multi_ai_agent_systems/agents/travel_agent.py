from multi_ai_agent_systems.agents.base import AgentContext, AgentResult


class TravelAgent:
    name = "travel"
    description = "Handles trips, packing checklists, and itineraries."
    skill_file = "skills/travel_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        reminder = tools.reminders.run(
            agent=self.name,
            title="Prepare travel plan and packing checklist",
            details=context.message,
            priority="normal",
        )
        return AgentResult(
            self.name,
            "Created travel planning workflow.",
            [reminder.message],
            [reminder.__dict__],
            {"checklist_seed": ["documents", "medications", "chargers", "clothes", "snacks"]},
        )
