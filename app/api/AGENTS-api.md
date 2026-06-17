# AGENTS-api.md — API Module Agent Instructions

## Summary
API module handles HTTP endpoints, routing, and OpenAPI-compatible request/response formatting for RR.

## Purpose and Expected Behavior
- Provides FastAPI application with versioned endpoints
- Handles incoming generation requests
- Returns OpenAI-compatible responses
- Manages API dependencies and routing

## Constraints and Invariants
- All endpoints must be OpenAI-compatible
- Use async handlers for model inference
- Validate all inputs with Pydantic schemas
- Never log secrets or API keys
- Rate limiting should be configurable

## Input/Output Expectations
- Input: JSON requests with prompt, scenario, and parameters
- Output: JSON responses with generated text and metadata
- Error responses: Standard HTTP status codes with descriptive messages

## Documentation Reference
- OpenAI API spec: https://platform.openai.com/docs/api-reference
- FastAPI docs: https://fastapi.tiangolo.com/

## Domain-Specific Rules for Agents
- **Endpoint Structure**: Use versioned routes (`/v1/`, `/v2/`)
- **Error Handling**: Return 422 for validation errors, 500 for server errors
- **Streaming**: Support streaming responses for long generations
- **Dependencies**: Use FastAPI's dependency injection for shared logic
- **Testing**: Mock external API calls in tests

### Module Files
- `app/api/v1/endpoints/generate.py`: Text generation endpoint
- `app/api/v1/endpoints/style.py`: Style management endpoint
- `app/api/v1/router.py`: Version 1 router
- `app/api/dependencies.py`: Shared dependencies
