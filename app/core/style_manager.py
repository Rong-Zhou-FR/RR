"""Style management system."""
from pathlib import Path
from typing import Any, Dict, List

import yaml

from app.core.exceptions import StyleNotFoundError

STYLE_DIR = Path(__file__).parent.parent.parent / "data" / "styles"


def get_style_examples(scenario: str) -> str:
    """Get style examples for a scenario.

    Args:
        scenario: The scenario name (e.g., "tech_guides")

    Returns:
        String containing style examples separated by newlines

    Raises:
        StyleNotFoundError: If the style file is not found or invalid
    """
    try:
        style_data = load_style(scenario)
        examples = style_data.get("examples", [])

        if not examples:
            raise StyleNotFoundError(
                scenario=scenario, path=str(STYLE_DIR / scenario / "default.yaml")
            )

        # Use first 3 examples for prompt injection
        return "\n\n".join(examples[:3])
    except yaml.YAMLError:
        raise StyleNotFoundError(
            scenario=scenario, path=str(STYLE_DIR / scenario / "default.yaml")
        )


def load_style(scenario: str) -> Dict[str, Any]:
    """Load style data for a scenario.

    Args:
        scenario: The scenario name (e.g., "tech_guides")

    Returns:
        Dictionary containing style data

    Raises:
        StyleNotFoundError: If the style file is not found or invalid
    """
    style_path = STYLE_DIR / scenario / "default.yaml"

    if not style_path.exists():
        raise StyleNotFoundError(scenario=scenario, path=str(style_path))

    try:
        with open(style_path, "r") as f:
            style_data = yaml.safe_load(f)

        if not style_data or "examples" not in style_data:
            raise StyleNotFoundError(scenario=scenario, path=str(style_path))

        return style_data
    except yaml.YAMLError:
        raise StyleNotFoundError(scenario=scenario, path=str(style_path))


def list_available_scenarios() -> List[str]:
    """List all available scenario directories.

    Returns:
        List of scenario names
    """
    scenarios = []
    for item in STYLE_DIR.iterdir():
        if item.is_dir():
            scenarios.append(item.name)
    return sorted(scenarios)
