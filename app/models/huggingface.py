"""Hugging Face Inference API provider."""
import json
import asyncio
import requests
from typing import Dict, Any
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

        # Use configurable base URL (supports Inference Providers and custom endpoints)
        self.api_url = settings.hf_base_url

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
        # Use OpenAI-compatible format for Inference Providers
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": params.get("max_tokens", 500),
            "temperature": params.get("temperature", 0.7),
            "top_p": params.get("top_p", 0.9),
            "stream": False,
        }
        
        try:
            # Use json= parameter to properly format the payload
            response = requests.post(
                self.api_url, json=payload, headers=headers, timeout=settings.timeout
            )
            
            # Check if response is HTML (model not available via Inference API)
            content_type = response.headers.get("content-type", "")
            if "text/html" in content_type.lower():
                # Try to extract error message from HTML
                if "Cannot POST" in response.text:
                    raise ModelInferenceError(
                        model=self.model,
                        error_details=(
                            f"Model '{self.model}' is not available via Hugging Face Inference API. "
                            "This model may require a paid inference endpoint or local deployment. "
                            "Try a different model that supports free Inference API."
                        ),
                    )
                else:
                    raise ModelInferenceError(
                        model=self.model,
                        error_details=f"Model not available via Inference API. Try a different model.",
                    )
            
            response.raise_for_status()
            
            result = response.json()
            
            # Handle OpenAI-compatible response format
            if isinstance(result, dict):
                if "choices" in result and len(result["choices"]) >0:
                    message = result["choices"][0].get("message", {})
                    if "content" in message:
                        return message["content"]
                
                # Check for error in response
                if "error" in result:
                    error_msg = result["error"]
                    if isinstance(error_msg, dict):
                        error_msg = error_msg.get("message", str(error_msg))
                    raise ModelInferenceError(
                        model=self.model, error_details=str(error_msg)
                    )
            
            raise ModelInferenceError(
                model=self.model, error_details="Unexpected response format from API"
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
