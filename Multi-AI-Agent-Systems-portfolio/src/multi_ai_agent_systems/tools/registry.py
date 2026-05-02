from multi_ai_agent_systems.db.repository import Repository
from multi_ai_agent_systems.tools.google_tools import CalendarTool, GmailTool
from multi_ai_agent_systems.tools.local_tools import ExpenseTool, ReminderTool


class ToolRegistry:
    def __init__(self, repository: Repository):
        self.reminders = ReminderTool(repository)
        self.expenses = ExpenseTool(repository)
        self.gmail = GmailTool()
        self.calendar = CalendarTool()
