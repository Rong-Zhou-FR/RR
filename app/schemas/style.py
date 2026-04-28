"""Pydantic schemas for style data."""
from pydantic import BaseModel, Field
from typing import List

class StyleResponse(BaseModel):
    """Response schema for style data."""
    name: str = Field(..., description="Style identifier")
    description: str = Field(..., description="Human-readable description")
    examples: List[str] = Field(..., description="Writing style examples")
