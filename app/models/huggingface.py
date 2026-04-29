"""Hugging Face Inference API provider."""
from typing import Any, Dict

import requests

from app.core.config import settings
from app.core.exceptions import ConfigurationError, ModelInferenceError
from app.models.base import BaseModelProvider


class HuggingFaceProvider(BaseModelProvider):
    """Hugging Face Inference API provider."""

    def __init__(self, model: str = None):
        """Initialize Hugging Face provider.

        Args:
            model: Model name to use (defaults to settings.default_model)

        Raises:
            ConfigurationError: If HF API token is not configured
        """
        self.model = model or settings.default_model
        self.api_token = settings.hf_api_token

        if not self.api_token:
            raise ConfigurationError(
                config_key="HF_API_TOKEN",
                message="Hugging Face API token is not configured",
            )

        self.api_url = f"https://api-inference.huggingface.co/models/{self.model}"

    async def generate(self, prompt: str, params: Dict[str, Any]) -> str:
        """Generate text using Hugging Face Inference API.

        Args:
            prompt: The prompt to generate text from
            params: Generation parameters (max_tokens, temperature, top_p)

        Returns:
            Generated text string

        Raises:
            ModelInferenceError: If the API call fails
        """
        headers = {"Authorization": f"Bearer {self.api_token}"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": params.get("max_tokens", 500),
                "temperature": params.get("temperature", 0.7),
                "top_p": params.get("top_p", 0.9),
            },
        }

        try:
            response = requests.post(
                self.api_url, json=payload, headers=headers, timeout=settings.timeout
            )
            response.raise_for_status()

            result = response.json()

            # Handle different response formats
            if isinstance(result, list) and len(result) > 0:
                if "generated_text" in result[0]:
                    return result[0]["generated_text"]
                elif "error" in result[0]:
                    raise ModelInferenceError(
                        model=self.model, error_details=result[0]["error"]
                    )

            raise ModelInferenceError(
                model=self.model, error_details="Unexpected response format from API"
            )

        except requests.exceptions.RequestException as e:
            raise ModelInferenceError(
                model=self.model, error_details=f"API request failed: {str(e)}"
            )
        except ValueError as e:
            raise ModelInferenceError(
                model=self.model,
                error_details=f"Failed to parse API response: {str(e)}",
            )
