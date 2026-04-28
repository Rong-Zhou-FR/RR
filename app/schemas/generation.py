"""Pydantic schemas for generation requests and responses."""
from pydantic import BaseModel, Field
from typing import Optional

class GenerationRequest(BaseModel):
    """Request schema for text generation."""
    prompt: str = Field(..., description="User prompt for text generation")
    scenario: str = Field("tech_guides", description="Scenario type for style injection")
    model: Optional[str] = Field(None, description="Model to use for generation")
    max_tokens: int = Field(500, ge=1, le=2000, description="Maximum tokens to generate")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Generation temperature")
    top_p: float = Field(0.9, ge=0.0, le=1.0, description="Top-p sampling parameter")

class GenerationResponse(BaseModel):
    """Response schema for text generation."""
    text: str = Field(..., description="Generated text")
    model: Optional[str] = Field(None, description="Model used for generation")
    scenario: str = Field(..., description="Scenario used for style injection")
