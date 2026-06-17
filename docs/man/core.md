# Core Module Documentation

## Overview

The core module handles prompt engineering, style management, and configuration for RR.

## Components

### Prompt Engine

**Function**: `build_prompt(scenario: str, user_input: str) -> str`

Builds a prompt with style injection for the given scenario.

**Example**:
```python
from app.core.prompt_engine import build_prompt

prompt = build_prompt("tech_guides", "Write about Python decorators")
```

### Style Manager

**Function**: `get_style_examples(scenario: str) -> str`

Retrieves style examples for a scenario.

**Function**: `load_style(scenario: str) -> Dict[str, Any]`

Loads complete style data for a scenario.

### Configuration

**Settings**:
- `hf_api_token`: Hugging Face API token
- `default_model`: Default model to use
- `max_retries`: Number of retries for API calls
- `timeout`: Request timeout in seconds

**Environment Variables**:
- `HF_API_TOKEN`: Hugging Face API token
- `DEFAULT_MODEL`: Default model name
