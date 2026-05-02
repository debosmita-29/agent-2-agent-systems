from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Multi AI Agent Systems"
    env: str = "local"

    database_url: str = "sqlite:///./data/app.db"
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/1"

    llm_provider: str = "rule_based"

    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"

    anthropic_api_key: str | None = None
    anthropic_model: str = "claude-3-5-sonnet-latest"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"

    gmail_enabled: bool = False
    gcalendar_enabled: bool = False

    google_client_id: str | None = None
    google_client_secret: str | None = None
    google_refresh_token: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
