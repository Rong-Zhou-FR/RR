# AGENTS-services.md — Services Module Agent Instructions

## Summary
Services module handles business logic and coordination for RR.

## Purpose and Expected Behavior
- **Generation Service**: Coordinates prompt building, model inference, and response formatting
- **Style Service**: Loads and manages writing styles
- **Validation**: Ensures data integrity throughout the pipeline

## Constraints and Invariants
- Services must be stateless
- Each service should have a single responsibility
- Services should not directly handle HTTP requests
- Use dependency injection for service dependencies

## Input/Output Expectations
- **Generation Service**: Takes request → Returns generated text
- **Style Service**: Takes scenario → Returns style data
- **Validation Service**: Takes data → Returns validated data or errors

## Documentation Reference
- FastAPI dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/

## Domain-Specific Rules for Agents

### Generation Service
1. Load style for requested scenario
2. Build prompt using prompt engine
3. Call model provider for inference
4. Format response according to OpenAI spec
5. Handle errors at each step

### Style Service
- Load styles from YAML files on startup
- Cache loaded styles for performance
- Validate style structure on load
- Provide style lookup by scenario name

### Service Dependencies
- Generation service depends on:
  - Prompt engine (core)
  - Model provider (models)
  - Style service (services)
- Use FastAPI dependencies for injection

### Module Files
- `app/services/generation.py`: Text generation coordination
- `app/services/style_loader.py`: Style loading and caching
