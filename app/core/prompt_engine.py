"""Prompt engineering system."""
from app.core.exceptions import GenerationError
from app.core.style_manager import get_style_examples


def build_prompt(scenario: str, user_input: str) -> str:
    """Build prompt with style injection for given scenario.

    Args:
        scenario: The scenario name (e.g., "tech_guides")
        user_input: The user's request or input text

    Returns:
        Formatted prompt with style examples and instructions

    Raises:
        GenerationError: If prompt construction fails
    """
    try:
        # Get style examples for the scenario
        style_examples = get_style_examples(scenario)

        # Build the prompt with clear structure
        prompt = f"""Write in Rong's style for {scenario.replace('_', ' ')}.

Style examples:
{style_examples}

User request: {user_input}

Response:"""

        return prompt
    except Exception as e:
        raise GenerationError(
            scenario=scenario, error_details=f"Failed to build prompt: {str(e)}"
        )


def build_prompt_with_params(
    scenario: str,
    user_input: str,
    additional_context: str = None,
    custom_instructions: str = None,
) -> str:
    """Build prompt with additional parameters.

    Args:
        scenario: The scenario name
        user_input: The user's request
        additional_context: Additional context to include
        custom_instructions: Custom instructions for the AI

    Returns:
        Formatted prompt with all components
    """
    try:
        style_examples = get_style_examples(scenario)

        prompt_parts = [
            f"Write in Rong's style for {scenario.replace('_', ' ')}.",
            "",
            "Style examples:",
            style_examples,
            "",
            f"User request: {user_input}",
        ]

        if additional_context:
            prompt_parts.extend(["", f"Additional context: {additional_context}"])

        if custom_instructions:
            prompt_parts.extend(["", f"Instructions: {custom_instructions}"])

        prompt_parts.append("")
        prompt_parts.append("Response:")

        return "\n".join(prompt_parts)
    except Exception as e:
        raise GenerationError(
            scenario=scenario,
            error_details=f"Failed to build prompt with params: {str(e)}",
        )
