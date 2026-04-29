"""Tests for style manager."""
import pytest

from app.core.exceptions import StyleNotFoundError
from app.core.style_manager import (
    get_style_examples,
    list_available_scenarios,
    load_style,
)


@pytest.fixture
def tech_guides_scenario():
    """Fixture for tech_guides scenario."""
    return "tech_guides"


@pytest.fixture
def invalid_scenario():
    """Fixture for invalid scenario."""
    return "invalid_scenario"


def test_get_style_examples_basic(tech_guides_scenario):
    """Test getting style examples."""
    examples = get_style_examples(tech_guides_scenario)

    assert isinstance(examples, str)
    assert len(examples) > 0


def test_get_style_examples_format(tech_guides_scenario):
    """Test that style examples are formatted correctly."""
    examples = get_style_examples(tech_guides_scenario)

    # Examples should be separated by newlines
    assert "\n\n" in examples


def test_get_style_examples_invalid_scenario(invalid_scenario):
    """Test getting style examples for invalid scenario."""
    with pytest.raises(StyleNotFoundError):
        get_style_examples(invalid_scenario)


def test_load_style_basic(tech_guides_scenario):
    """Test loading style data."""
    style_data = load_style(tech_guides_scenario)

    assert isinstance(style_data, dict)
    assert "name" in style_data
    assert "description" in style_data
    assert "examples" in style_data


def test_load_style_invalid_scenario(invalid_scenario):
    """Test loading style for invalid scenario."""
    with pytest.raises(StyleNotFoundError):
        load_style(invalid_scenario)


def test_list_available_scenarios():
    """Test listing available scenarios."""
    scenarios = list_available_scenarios()

    assert isinstance(scenarios, list)
    assert len(scenarios) > 0
    assert "tech_guides" in scenarios


def test_style_examples_not_empty(tech_guides_scenario):
    """Test that style examples are not empty."""
    style_data = load_style(tech_guides_scenario)

    assert len(style_data["examples"]) > 0


def test_style_data_structure(tech_guides_scenario):
    """Test that style data has correct structure."""
    style_data = load_style(tech_guides_scenario)

    # Check required fields
    assert "name" in style_data
    assert "description" in style_data
    assert "examples" in style_data

    # Check types
    assert isinstance(style_data["name"], str)
    assert isinstance(style_data["description"], str)
    assert isinstance(style_data["examples"], list)
