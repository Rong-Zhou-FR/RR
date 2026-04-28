"""Text generation service."""
from app.schemas.generation import GenerationRequest
from app.core.prompt_engine import build_prompt
from app.models.provider import get_model_provider

async def generate_text(request: GenerationRequest) -> str:
    """Generate text in Rong's style."""
    # Build prompt with style injection
    prompt = build_prompt(request.scenario, request.prompt)
    
    # Get model provider
    provider = get_model_provider(request.model)
    
    # Generate text
    params = {
        "max_tokens": request.max_tokens,
        "temperature": request.temperature,
        "top_p": request.top_p,
    }
    
    return await provider.generate(prompt, params)
