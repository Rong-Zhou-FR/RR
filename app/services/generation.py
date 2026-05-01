"""Text generation service."""
from app.core.exceptions import GenerationError
from app.core.prompt_engine import build_prompt
from app.models.provider import get_model_provider
from app.schemas.generation import GenerationRequest


async def generate_text(
    request: GenerationRequest,
    use_rag: bool = False,
) -> str:
    """Generate text in Rong's style.

    Args:
        request: Generation request containing prompt, scenario, and parameters
        use_rag: Whether to use RAG for style example retrieval

    Returns:
        Generated text string

    Raises:
        GenerationError: If text generation fails at any step
    """
    try:
        # Get style examples (from RAG or static)
        style_examples = None
        if use_rag:
            from app.services.rag import get_rag

            rag = await get_rag()
            style_examples = await rag.retrieve(
                request.prompt,
                request.scenario,
                top_k=3,
            )

        # Build prompt with style injection
        prompt = build_prompt(request.scenario, request.prompt, style_examples)

        # Get model provider
        provider = get_model_provider(request.model)

        # Prepare generation parameters
        params = {
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "top_p": request.top_p,
        }

        # Generate text using the model provider
        generated_text = await provider.generate(prompt, params)

        return generated_text

    except GenerationError:
        # Re-raise GenerationError as-is
        raise
    except Exception as e:
        # Wrap any other exceptions in GenerationError
        raise GenerationError(
            scenario=request.scenario,
            error_details=f"Unexpected error during generation: {str(e)}",
        )
