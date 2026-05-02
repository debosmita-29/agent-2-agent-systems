class CrewAIAdapter:
    """CrewAI-compatible design placeholder.

    Agent mapping:
    - ScheduleAgent -> Family Schedule Planner
    - GroceryAgent -> Household Inventory Planner
    - HealthAgent -> Health Reminder Coordinator
    - FinanceAgent -> Family Finance Tracker
    - TravelAgent -> Travel Planner
    - MemoryAgent -> Shared context provider
    """

    def build_crew_spec(self) -> dict:
        return {
            "agents": [
                "MemoryAgent",
                "ScheduleAgent",
                "GroceryAgent",
                "HealthAgent",
                "FinanceAgent",
                "TravelAgent",
                "ResearchAgent",
            ],
            "process": "hierarchical",
            "manager": "AgentOrchestrator",
        }
