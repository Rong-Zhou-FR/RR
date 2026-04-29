"""Tests for prompt engine."""
import pytest

from app.core.exceptions import GenerationError
from app.core.prompt_engine import build_prompt, build_prompt_with_params


@pytest.fixture
def tech_guides_scenario():
    """Fixture for tech_guides scenario."""
    return "tech_guides"


@pytest.fixture
def code_docs_scenario():
    """Fixture for code_docs scenario."""
    return "code_docs"


@pytest.fixture
def user_input():
    """Fixture for user input."""
    return "Write a guide about Python decorators"


def test_build_prompt_basic(tech_guides_scenario, user_input):
    """Test basic prompt building."""
    prompt = build_prompt(tech_guides_scenario, user_input)

    assert "Write in Rong's style for tech guides" in prompt
    assert "User request:" in prompt
    assert user_input in prompt
    assert "Response:" in prompt


def test_build_prompt_includes_style_examples(tech_guides_scenario, user_input):
    """Test that prompt includes style examples."""
    prompt = build_prompt(tech_guides_scenario, user_input)

    # Should include style examples section
    assert "Style examples:" in prompt


def test_build_prompt_with_custom_context(tech_guides_scenario, user_input):
    """Test building prompt with additional context."""
    additional_context = "Focus on beginner-friendly explanations"
    custom_instructions = "Use simple language"

    prompt = build_prompt_with_params(
        tech_guides_scenario,
        user_input,
        additional_context=additional_context,
        custom_instructions=custom_instructions,
    )

    assert additional_context in prompt
    assert custom_instructions in prompt


def test_build_prompt_invalid_scenario():
    """Test building prompt with invalid scenario."""
    with pytest.raises(GenerationError):
        build_prompt("invalid_scenario", "test input")


def test_build_prompt_with_params_basic(tech_guides_scenario, user_input):
    """Test building prompt with parameters."""
    prompt = build_prompt_with_params(tech_guides_scenario, user_input)

    assert "Write in Rong's style for tech guides" in prompt
    assert user_input in prompt
    assert "Response:" in prompt


def test_build_prompt_scenario_formatting(tech_guides_scenario, user_input):
    """Test that scenario name is formatted correctly."""
    prompt = build_prompt(tech_guides_scenario, user_input)

    # Should replace underscores with spaces
    assert "tech guides" in prompt
    assert "tech_guides" not in prompt
