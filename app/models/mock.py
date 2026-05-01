"""Mock model provider for testing when HF Inference API is unavailable."""
import asyncio
from typing import Dict, Any
from app.models.base import BaseModelProvider
from app.core.exceptions import ModelInferenceError


class MockProvider(BaseModelProvider):
    """Mock provider that returns pre-defined responses for testing."""
    
    async def generate(self, prompt: str, params: Dict[str, Any]) -> str:
        """Generate mock text response.
        
        Args:
            prompt: The prompt to generate text from
            params: Generation parameters (ignored in mock)
            
        Returns:
            Mock generated text string
        """
        # Simulate some processing time
        await asyncio.sleep(0.5)
        
        # Return a mock response that includes part of the prompt
        mock_response = (
            f"Mock response based on prompt: {prompt[:50]}...\n\n"
            f"This is a test response from the MockProvider. "
            f"The actual model would generate text in Rong's style here."
        )
        
        return mock_response
