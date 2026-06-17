"""Base model interface."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseModelProvider(ABC):
    """Base class for model providers."""

    @abstractmethod
    async def generate(self, prompt: str, params: Dict[str, Any]) -> str:
        """Generate text using the model."""
        pass
