"""Style loading service."""
from app.core.style_manager import (
    get_style_examples,
    list_available_scenarios,
    load_style,
)


def get_style(scenario: str) -> dict:
    """Get style data for a scenario.

    Args:
        scenario: The scenario name (e.g., "tech_guides")

    Returns:
        Dictionary containing style data

    Raises:
        StyleNotFoundError: If the style file is not found or invalid
    """
    return load_style(scenario)


def get_style_examples_for_scenario(scenario: str) -> str:
    """Get style examples for a scenario.

    Args:
        scenario: The scenario name (e.g., "tech_guides")

    Returns:
        String containing style examples

    Raises:
        StyleNotFoundError: If the style file is not found or invalid
    """
    return get_style_examples(scenario)


def get_available_scenarios() -> list:
    """Get list of available scenario names.

    Returns:
        List of scenario names
    """
    return list_available_scenarios()
