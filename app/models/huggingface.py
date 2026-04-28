"""Hugging Face Inference API provider."""
import requests
from typing import Dict, Any
from app.core.config import settings
from app.models.base import BaseModelProvider

class HuggingFaceProvider(BaseModelProvider):
    """Hugging Face Inference API provider."""
    
    def __init__(self, model: str = None):
        self.model = model or settings.default_model
        self.api_token = settings.hf_api_token
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model}"
    
    async def generate(self, prompt: str, params: Dict[str, Any]) -> str:
        """Generate text using Hugging Face Inference API."""
        headers = {"Authorization": f"Bearer {self.api_token}"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": params.get("max_tokens", 500),
                "temperature": params.get("temperature", 0.7),
                "top_p": params.get("top_p", 0.9),
            }
        }
        
        response = requests.post(self.api_url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        return result[0]["generated_text"]
