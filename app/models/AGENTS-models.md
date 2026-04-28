# AGENTS-models.md — Models Module Agent Instructions

## Summary
Models module handles AI model providers and inference for RR.

## Purpose and Expected Behavior
- **Provider Abstraction**: Switch between HF Inference API and local models
- **Model Inference**: Generate text using selected model
- **Configuration**: Manage model selection and parameters

## Constraints and Invariants
- Must support both HF Inference API and local models
- Model selection must be configurable via environment
- Never expose API keys in logs or responses
- Handle rate limiting and timeouts gracefully

## Input/Output Expectations
- Input: Prompt string + generation parameters
- Output: Generated text string
- Errors: Model-specific errors with helpful messages

## Documentation Reference
- Hugging Face Inference API: https://huggingface.co/docs/api-inference/
- Transformers docs: https://huggingface.co/docs/transformers/

## Domain-Specific Rules for Agents

### Provider Abstraction
- Create base model interface in `base.py`
- Implement HF Inference API in `huggingface.py`
- Implement local models in `local.py` (future)
- Use factory pattern for model selection

### Model Configuration
- Default model: `mistralai/Mistral-7B-Instruct-v0.1`
- Support model override via API request
- Validate model exists before inference
- Cache model metadata when possible

### Error Handling
- Handle HF API rate limiting (429 errors)
- Handle network timeouts gracefully
- Provide fallback options when possible
- Log errors without exposing secrets

### Module Files
- `app/models/base.py`: Base model interface
- `app/models/huggingface.py`: HF Inference API implementation
- `app/models/provider.py`: Provider factory and selection
