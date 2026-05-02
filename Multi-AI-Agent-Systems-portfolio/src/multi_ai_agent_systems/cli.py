import asyncio

import typer
from rich import print

from multi_ai_agent_systems.db.base import Base, SessionLocal, engine
from multi_ai_agent_systems.db.repository import Repository
from multi_ai_agent_systems.orchestration.engine import AgentOrchestrator

app = typer.Typer(help="Multi-AI-Agent-Systems CLI")


@app.command()
def run(message: str):
    Base.metadata.create_all(bind=engine)

    async def _run():
        db = SessionLocal()
        try:
            result = await AgentOrchestrator(Repository(db)).run(message)
            print("[bold green]Selected agents:[/bold green]", ", ".join(result["selected_agents"]))
            print("[bold blue]Answer:[/bold blue]", result["answer"])
            for agent_result in result["agent_results"]:
                print(f"[bold yellow]{agent_result['agent_name']}[/bold yellow]")
                for action in agent_result["actions"]:
                    print(f"  - {action}")
        finally:
            db.close()

    asyncio.run(_run())


if __name__ == "__main__":
    app()
