# AGENTS-core.md — Core Module Agent Instructions

## Summary
Core module handles prompt engineering, style management, and configuration for RR.

## Purpose and Expected Behavior
- **Prompt Engine**: Constructs prompts with style injection based on scenario
- **Style Manager**: Loads and validates writing style examples
- **Config**: Manages application configuration and environment variables

## Constraints and Invariants
- Styles must be stored as YAML files in `data/styles/`
- Prompt templates must be reusable across scenarios
- Configuration must be environment-driven (no hardcoded values)
- Style validation must ensure required fields are present

## Input/Output Expectations
- **Prompt Engine**: Takes scenario + user input → Returns formatted prompt
- **Style Manager**: Takes scenario name → Returns style examples
- **Config**: Reads environment → Returns validated configuration

## Documentation Reference
- Pydantic validation: https://docs.pydantic.dev/
- YAML spec: https://yaml.org/spec/

## Domain-Specific Rules for Agents

### Prompt Engineering
- Always include style examples in prompts
- Use clear delimiters between instructions and user content
- Include scenario-specific context
- Optimize for target model's token limits

### Style Management
- Store styles in `data/styles/{scenario}/` directories
- Each style file must contain:
  - `name`: Style identifier
  - `examples`: Array of text examples
  - `description`: Human-readable description
- Validate style files on load

### Configuration
- Use `.env` file for local development
- Never commit `.env` to version control
- All config values must have defaults
- Use Pydantic for config validation

### Module Files
- `app/core/prompt_engine.py`: Prompt construction logic
- `app/core/style_manager.py`: Style loading and validation
- `app/core/config.py`: Configuration management
