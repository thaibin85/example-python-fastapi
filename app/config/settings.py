from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "FastAPI Example API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Security settings
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS settings
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]

    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Database settings
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
