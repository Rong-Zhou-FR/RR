"""FastAPI application entry point."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.v1.router import router as v1_router
from app.core.exceptions import RRException
from app.schemas.error import ErrorDetail, ErrorResponse


def create_application() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="RR (Robotika Ron)",
        description="Text generation AI agent to write text in Rong's style",
        version="0.1.0",
    )

    # Include version 1 API router
    app.include_router(v1_router, prefix="/v1")

    # Add exception handlers for custom exceptions
    @app.exception_handler(RRException)
    async def rr_exception_handler(request: Request, exc: RRException):
        """Handle custom RR exceptions with structured JSON response."""
        error_detail = ErrorDetail(
            code=exc.error_code,
            message=exc.message,
            details=exc.details,
            troubleshooting=exc.troubleshooting,
        )
        error_response = ErrorResponse(error=error_detail)
        return JSONResponse(status_code=400, content=error_response.dict())

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle unexpected exceptions with structured JSON response."""
        error_detail = ErrorDetail(
            code="UNEXPECTED_ERROR",
            message=f"An unexpected error occurred: {str(exc)}",
            details={"error": str(exc)},
            troubleshooting="Please try again later or contact support.",
        )
        error_response = ErrorResponse(error=error_detail)
        return JSONResponse(status_code=500, content=error_response.dict())

    return app


app = create_application()
