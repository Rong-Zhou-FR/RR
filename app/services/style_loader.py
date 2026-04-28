"""Style loading service."""
from app.core.style_manager import load_style

def get_style(scenario: str) -> dict:
    """Get style data for a scenario."""
    return load_style(scenario)
