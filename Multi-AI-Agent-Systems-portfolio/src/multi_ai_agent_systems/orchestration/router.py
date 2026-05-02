class IntentRouter:
    KEYWORDS = {
        "schedule": ["calendar", "schedule", "remind", "reminder", "school", "appointment", "event", "week"],
        "grocery": ["grocery", "groceries", "shopping", "pantry", "food", "milk", "eggs", "meal"],
        "finance": ["bill", "budget", "expense", "finance", "subscription", "$", "payment", "cost"],
        "health": ["health", "medicine", "med", "doctor", "wellness", "workout", "appointment"],
        "travel": ["travel", "trip", "flight", "hotel", "packing", "itinerary", "vacation"],
        "research": ["research", "find", "compare", "summarize", "analyze"],
    }

    def route(self, message: str) -> list[str]:
        normalized = message.lower()
        selected = []
        for agent, keywords in self.KEYWORDS.items():
            if any(keyword in normalized for keyword in keywords):
                selected.append(agent)

        if "memory" not in selected:
            selected.insert(0, "memory")

        if len(selected) == 1:
            selected.append("schedule")

        return selected
