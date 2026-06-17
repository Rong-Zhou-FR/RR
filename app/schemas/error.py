"""Pydantic schemas for error responses."""
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    """Detailed error information."""

    code: str = Field(..., description="Error code in uppercase with underscores")
    message: str = Field(..., description="Human-readable error message")
    details: Optional[Dict[str, Any]] = Field(
        None, description="Additional context for debugging"
    )
    troubleshooting: Optional[str] = Field(
        None, description="Guidance for resolving the error"
    )


class ErrorResponse(BaseModel):
    """Structured error response with top-level 'error' key."""

    error: ErrorDetail = Field(..., description="Error details")
