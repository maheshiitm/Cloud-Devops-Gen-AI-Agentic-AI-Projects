from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "development"
    openai_api_key: str = ""
    model_name: str = "gpt-5.6"
    database_path: str = "agent_memory.db"
    max_revisions: int = 2
    max_tool_calls: int = 6
    enable_tracing: bool = True
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
