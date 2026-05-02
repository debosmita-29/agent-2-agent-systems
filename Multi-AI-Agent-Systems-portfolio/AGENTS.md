# AGENTS.md

This project uses a specialist-agent architecture coordinated by a central orchestrator.

## Design principles

1. Each agent owns one domain.
2. Each agent can call tools.
3. Each agent writes useful context back to memory.
4. The orchestrator selects the agents needed.
5. The final synthesis layer explains what happened and what to do next.

## Agent inventory

| Agent | Purpose | Tools |
|---|---|---|
| MemoryAgent | Persistent context and personalization | VectorMemory |
| ScheduleAgent | Calendar, events, reminders, planning | ReminderTool, CalendarTool |
| GroceryAgent | Grocery lists and household inventory | ReminderTool |
| HealthAgent | Medication and wellness reminders | ReminderTool |
| FinanceAgent | Bills, expenses, subscriptions | ExpenseTool, ReminderTool |
| TravelAgent | Packing, itinerary, travel reminders | ReminderTool |
| ResearchAgent | RAG-supported planning and analysis | Retriever |

## Production controls

- Require approval before sending emails.
- Require approval before modifying calendars.
- Require approval before payments or financial actions.
- Log every tool call.
- Store audit trails.
