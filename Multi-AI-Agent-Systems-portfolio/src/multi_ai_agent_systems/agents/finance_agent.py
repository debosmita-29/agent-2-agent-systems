import re

from multi_ai_agent_systems.agents.base import AgentContext, AgentResult


class FinanceAgent:
    name = "finance"
    description = "Handles bills, budgets, expenses, and subscriptions."
    skill_file = "skills/finance_agent.skill.md"

    async def run(self, context: AgentContext, repository, tools):
        amounts = [float(x) for x in re.findall(r"\$?(\d+(?:\.\d{1,2})?)", context.message)]
        actions = []
        outputs = []

        if amounts:
            for amount in amounts[:5]:
                result = tools.expenses.run(category="general", amount=amount, note=context.message[:250])
                actions.append(result.message)
                outputs.append(result.__dict__)
        else:
            reminder = tools.reminders.run(
                agent=self.name,
                title="Review bills, budget, and subscriptions",
                details=context.message,
                priority="normal",
            )
            actions.append(reminder.message)
            outputs.append(reminder.__dict__)

        return AgentResult(self.name, "Processed finance request.", actions, outputs, {"amounts_detected": amounts})
