from multi_ai_agent_systems.db.repository import Repository
from multi_ai_agent_systems.tools.base import ToolResult


class ReminderTool:
    name = "reminder_tool"
    description = "Creates reminders and tasks in the local database."

    def __init__(self, repository: Repository):
        self.repository = repository

    def run(self, agent: str, title: str, details: str = "", priority: str = "normal", due_at: str | None = None):
        task = self.repository.add_task(agent=agent, title=title, details=details, priority=priority, due_at=due_at)
        return ToolResult(self.name, True, f"Created reminder/task: {task.title}", {"task_id": task.id})


class ExpenseTool:
    name = "expense_tool"
    description = "Records expenses in the local database."

    def __init__(self, repository: Repository):
        self.repository = repository

    def run(self, category: str, amount: float, note: str = ""):
        expense = self.repository.add_expense(category=category, amount=amount, note=note)
        return ToolResult(self.name, True, f"Recorded expense: ${expense.amount:.2f}", {"expense_id": expense.id})
