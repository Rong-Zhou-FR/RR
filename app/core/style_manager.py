"""Style management system."""
import yaml
from pathlib import Path
from typing import List, Dict, Any

STYLE_DIR = Path(__file__).parent.parent.parent / "data" / "styles"

def get_style_examples(scenario: str) -> str:
    """Get style examples for a scenario."""
    style_path = STYLE_DIR / scenario / "default.yaml"
    
    if not style_path.exists():
        raise ValueError(f"Style not found for scenario: {scenario}")
    
    with open(style_path, 'r') as f:
        style_data = yaml.safe_load(f)
    
    examples = style_data.get('examples', [])
    return "\n\n".join(examples[:3])  # Use first 3 examples

def load_style(scenario: str) -> Dict[str, Any]:
    """Load style data for a scenario."""
    style_path = STYLE_DIR / scenario / "default.yaml"
    
    if not style_path.exists():
        raise ValueError(f"Style not found for scenario: {scenario}")
    
    with open(style_path, 'r') as f:
        return yaml.safe_load(f)
