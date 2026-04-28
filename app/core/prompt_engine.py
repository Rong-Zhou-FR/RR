"""Prompt engineering system."""
from typing import Dict, Any
from app.core.style_manager import get_style_examples

def build_prompt(scenario: str, user_input: str) -> str:
    """Build prompt with style injection for given scenario."""
    style_examples = get_style_examples(scenario)
    
    prompt = f"""Write in Rong's style for {scenario.replace('_', ' ')}.

Style examples:
{style_examples}

User request: {user_input}

Response:"""
    
    return prompt
