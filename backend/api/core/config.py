"""Application configuration."""

from typing import Literal

from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Application
    PROJECT_NAME: str = "FastAPI Monorepo"
    VERSION: str = "0.1.0"
    APP_ENV: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = True
    
    # API
    V1_PREFIX: str = "/v1"
    SECRET_KEY: str = "changeme"
    
    # Database
    DATABASE_URL: PostgresDsn
    
    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: str | list[str]) -> list[str]:
        """Parse CORS origins from string or list."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


settings = Settings()
