from fastapi.testclient import TestClient

from multi_ai_agent_systems.api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_agent_run():
    response = client.post("/agents/run", json={"message": "Create a grocery reminder"})
    assert response.status_code == 200
    body = response.json()
    assert "grocery" in body["selected_agents"]
    assert body["answer"]
