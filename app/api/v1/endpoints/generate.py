"""Text generation endpoint."""
from fastapi import APIRouter, HTTPException

from app.core.exceptions import RRException
from app.schemas.error import ErrorDetail, ErrorResponse
from app.schemas.generation import GenerationRequest, GenerationResponse
from app.services.generation import generate_text

router = APIRouter()


@router.post("/", response_model=GenerationResponse)
async def generate(request: GenerationRequest):
    """Generate text in Rong's style based on scenario.

    Args:
        request: Generation request containing prompt, scenario, and parameters

    Returns:
        Generated text in Rong's style

    Raises:
        HTTPException: With structured JSON error response for any failures
    """
    try:
        generated_text = await generate_text(request)
        return GenerationResponse(
            text=generated_text, model=request.model, scenario=request.scenario
        )
    except RRException as e:
        # Convert custom exception to structured JSON error response
        error_detail = ErrorDetail(
            code=e.error_code,
            message=e.message,
            details=e.details,
            troubleshooting=e.troubleshooting,
        )
        error_response = ErrorResponse(error=error_detail)
        raise HTTPException(status_code=400, detail=error_response.dict())
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
