# Models Module Documentation

## Overview

The models module handles AI model providers and inference for RR.

## Components

### Base Model Provider

**Interface**: `BaseModelProvider`

Abstract base class for all model providers.

**Method**: `async generate(prompt: str, params: Dict[str, Any]) -> str`

### Hugging Face Provider

**Class**: `HuggingFaceProvider`

Implements Hugging Face Inference API integration.

**Configuration**:
- Uses `HF_API_TOKEN` environment variable
- Default model: `mistralai/Mistral-7B-Instruct-v0.1`

### Provider Factory

**Function**: `get_model_provider(model: Optional[str] = None) -> BaseModelProvider`

Returns the appropriate model provider instance.

## Usage

```python
from app.models.provider import get_model_provider

provider = get_model_provider()
text = await provider.generate(prompt, params)
```
