"""Custom exception classes for RR (Robotika Ron)."""
from typing import Any, Dict, Optional


class RRException(Exception):
    """Base exception class for RR with error codes and troubleshooting guidance."""

    def __init__(
        self,
        error_code: str,
        message: str,
        details: Optional[Dict[str, Any]] = None,
        troubleshooting: Optional[str] = None,
    ):
        """
        Initialize RR exception.

        Args:
            error_code: Unique error code in uppercase with underscores
                (e.g., STYLE_NOT_FOUND)
            message: Human-readable error message
            details: Additional context information for debugging
            troubleshooting: Guidance for resolving the error
        """
        self.error_code = error_code
        self.message = message
        self.details = details or {}
        self.troubleshooting = troubleshooting
        super().__init__(message)


class StyleNotFoundError(RRException):
    """Raised when a style file is not found or invalid."""

    def __init__(self, scenario: str, path: str):
        super().__init__(
            error_code="STYLE_NOT_FOUND",
            message=f"Style file not found for scenario: {scenario}",
            details={"scenario": scenario, "path": path},
            troubleshooting=(
                "Check that the style file exists and is properly formatted YAML. "
                "Ensure the scenario name matches a directory in data/styles/."
            ),
        )


class ModelInferenceError(RRException):
    """Raised when model inference fails."""

    def __init__(self, model: str, error_details: str):
        super().__init__(
            error_code="MODEL_INFERENCE_ERROR",
            message=f"Model inference failed for model: {model}",
            details={"model": model, "error": error_details},
            troubleshooting=(
                "Check your Hugging Face API token and model availability. "
                "Verify network connectivity and API rate limits."
            ),
        )


class ConfigurationError(RRException):
    """Raised when configuration is invalid or missing."""

    def __init__(self, config_key: str, message: str):
        super().__init__(
            error_code="CONFIGURATION_ERROR",
            message=f"Configuration error for {config_key}: {message}",
            details={"config_key": config_key, "message": message},
            troubleshooting=(
                "Check your .env file and environment variables. "
                "Ensure all required configuration values are set."
            ),
        )


class GenerationError(RRException):
    """Raised when text generation fails."""

    def __init__(self, scenario: str, error_details: str):
        super().__init__(
            error_code="GENERATION_ERROR",
            message=f"Text generation failed for scenario: {scenario}",
            details={"scenario": scenario, "error": error_details},
            troubleshooting=(
                "Check the prompt structure and style examples. "
                "Verify the model is responding correctly."
            ),
        )
