"""Configuration management."""
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    hf_api_token: Optional[str] = None
    default_model: str = "mistralai/Mistral-7B-Instruct-v0.1"
    max_retries: int = 3
    timeout: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
