"""Pydantic schemas for style data."""
from typing import List

from pydantic import BaseModel, Field


class StyleResponse(BaseModel):
    """Response schema for style data."""

    name: str = Field(..., description="Style identifier")
    description: str = Field(..., description="Human-readable description")
    examples: List[str] = Field(..., description="Writing style examples")
