"""Model provider factory."""
from typing import Optional
from app.models.base import BaseModelProvider
from app.core.config import settings


def get_model_provider(model: Optional[str] = None) -> BaseModelProvider:
    """Get model provider instance.
    
    Args:
        model: Optional model name to override default
        
    Returns:
        Model provider instance
        
    Note:
        This factory can be extended to support local models in the future.
        Currently supports HuggingFaceProvider and MockProvider.
    """
    # Uncomment the following line to use MockProvider for testing
    # from app.models.mock import MockProvider
    # return MockProvider()
    
    # Use Hugging Face Inference API
    from app.models.huggingface import HuggingFaceProvider
    return HuggingFaceProvider(model=model)
