# Services Module Documentation

## Overview

The services module handles business logic and coordination for RR.

## Components

### Generation Service

**Function**: `async generate_text(request: GenerationRequest) -> str`

Coordinates the entire text generation pipeline:
1. Builds prompt with style injection
2. Selects model provider
3. Generates text
4. Returns formatted response

### Style Service

**Function**: `get_style(scenario: str) -> dict`

Retrieves style data for a scenario.

## Usage

```python
from app.services.generation import generate_text
from app.schemas.generation import GenerationRequest

request = GenerationRequest(
    prompt="Write about Python",
    scenario="tech_guides"
)
text = await generate_text(request)
```
