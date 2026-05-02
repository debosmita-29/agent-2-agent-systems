from multi_ai_agent_systems.agents.base import AgentContext, AgentResult


class GroceryAgent:
    name = "grocery"
    description = "Handles groceries, pantry inventory, and shopping lists."
    skill_file = "skills/grocery_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        reminder = tools.reminders.run(
            agent=self.name,
            title="Create or update grocery list",
            details="Review pantry staples, meal plan, and recurring grocery needs.",
            priority="normal",
        )
        return AgentResult(
            self.name,
            "Prepared grocery planning task.",
            [reminder.message],
            [reminder.__dict__],
            {"suggested_items": ["milk", "eggs", "fruit", "snacks", "vegetables"]},
        )
