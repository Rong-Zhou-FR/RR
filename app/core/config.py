"""Configuration management."""
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    hf_api_token: Optional[str] = None
    hf_base_url: str = "https://router.huggingface.co/v1/chat/completions"
    default_model: str = "mistralai/Mistral-7B-Instruct-v0.1"
    max_retries: int = 3
    timeout: int = 30
    ghost_api_content: Optional[str] = None
    ghost_api_admin: Optional[str] = None
    ghost_url: Optional[str] = None

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
