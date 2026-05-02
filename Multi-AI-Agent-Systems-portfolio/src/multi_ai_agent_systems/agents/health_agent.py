from multi_ai_agent_systems.agents.base import AgentContext, AgentResult


class HealthAgent:
    name = "health"
    description = "Handles health reminders, appointments, and wellness tasks."
    skill_file = "skills/health_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        reminder = tools.reminders.run(
            agent=self.name,
            title="Create health or medication reminder",
            details=context.message,
            priority="high",
        )
        return AgentResult(
            self.name,
            "Created health reminder workflow.",
            [reminder.message],
            [reminder.__dict__],
        )
