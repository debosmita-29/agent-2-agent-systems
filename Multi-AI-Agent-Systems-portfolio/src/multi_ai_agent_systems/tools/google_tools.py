from multi_ai_agent_systems.config import settings
from multi_ai_agent_systems.tools.base import ToolResult


class GmailTool:
    name = "gmail_tool"
    description = "Drafts or sends Gmail messages. Demo-safe by default."

    def run(self, to: str, subject: str, body: str, draft_only: bool = True):
        if not settings.gmail_enabled:
            return ToolResult(
                self.name,
                True,
                "Gmail tool ran in demo mode. No email was sent.",
                {"to": to, "subject": subject, "draft_only": draft_only},
            )

        return ToolResult(
            self.name,
            False,
            "Gmail integration is enabled but the real Gmail API client is not configured yet.",
            {},
        )


class CalendarTool:
    name = "calendar_tool"
    description = "Creates calendar events. Demo-safe by default."

    def run(self, title: str, start_time: str | None = None, end_time: str | None = None, attendees: list[str] | None = None):
        if not settings.gcalendar_enabled:
            return ToolResult(
                self.name,
                True,
                "Calendar tool ran in demo mode. No calendar event was created.",
                {"title": title, "start_time": start_time, "end_time": end_time, "attendees": attendees or []},
            )

        return ToolResult(
            self.name,
            False,
            "Calendar integration is enabled but the real Calendar API client is not configured yet.",
            {},
        )
