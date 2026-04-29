"""Model provider factory."""
from typing import Optional

from app.models.base import BaseModelProvider
from app.models.huggingface import HuggingFaceProvider


def get_model_provider(model: Optional[str] = None) -> BaseModelProvider:
    """Get model provider instance.

    Args:
        model: Optional model name to override default

    Returns:
        Model provider instance (currently always HuggingFaceProvider)

    Note:
        This factory can be extended to support local models in the future.
        For now, it always returns a HuggingFaceProvider instance.
    """
    # For now, always use Hugging Face Inference API
    # Can be extended to support local models in the future
    return HuggingFaceProvider(model=model)
