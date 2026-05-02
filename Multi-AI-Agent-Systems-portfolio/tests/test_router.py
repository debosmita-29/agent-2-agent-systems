from multi_ai_agent_systems.orchestration.router import IntentRouter


def test_router_selects_expected_agents():
    routes = IntentRouter().route("Plan grocery, school calendar, health reminders, and bills")
    assert "memory" in routes
    assert "grocery" in routes
    assert "schedule" in routes
    assert "health" in routes
    assert "finance" in routes
