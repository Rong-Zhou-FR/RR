"""Style management endpoint."""
from fastapi import APIRouter, HTTPException

from app.core.exceptions import RRException
from app.schemas.error import ErrorDetail, ErrorResponse
from app.schemas.style import StyleResponse
from app.services.style_loader import get_style

router = APIRouter()


@router.get("/{scenario}", response_model=StyleResponse)
async def get_style_endpoint(scenario: str):
    """Get writing style examples for a scenario.

    Args:
        scenario: The scenario name (e.g., "tech_guides")

    Returns:
        Style data including name, description, and examples

    Raises:
        HTTPException: With structured JSON error response if style not found
    """
    try:
        style_data = get_style(scenario)
        return StyleResponse(**style_data)
    except RRException as e:
        # Convert custom exception to structured JSON error response
        error_detail = ErrorDetail(
            code=e.error_code,
            message=e.message,
            details=e.details,
            troubleshooting=e.troubleshooting,
        )
        error_response = ErrorResponse(error=error_detail)
        raise HTTPException(status_code=404, detail=error_response.dict())
    except Exception as e:
        # Handle unexpected errors
        error_detail = ErrorDetail(
            code="UNEXPECTED_ERROR",
            message=f"An unexpected error occurred: {str(e)}",
            details={"error": str(e)},
            troubleshooting="Please try again later or contact support.",
        )
        error_response = ErrorResponse(error=error_detail)
        raise HTTPException(status_code=500, detail=error_response.dict())
