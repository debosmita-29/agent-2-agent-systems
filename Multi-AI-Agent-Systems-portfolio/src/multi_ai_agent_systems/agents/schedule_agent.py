from multi_ai_agent_systems.agents.base import AgentContext, AgentResult


class ScheduleAgent:
    name = "schedule"
    description = "Handles calendars, reminders, and weekly planning."
    skill_file = "skills/schedule_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        reminder = tools.reminders.run(
            agent=self.name,
            title="Review family calendar and create weekly reminders",
            details=context.message,
            priority="high",
        )
        calendar = tools.calendar.run(title="Family planning review")
        return AgentResult(
            self.name,
            "Created schedule planning workflow.",
            [reminder.message, calendar.message],
            [reminder.__dict__, calendar.__dict__],
        )
