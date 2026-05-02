from celery import Celery

from multi_ai_agent_systems.config import settings

celery_app = Celery(
    "multi_ai_agent_systems",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend,
)
celery_app.autodiscover_tasks(["multi_ai_agent_systems.worker"])
