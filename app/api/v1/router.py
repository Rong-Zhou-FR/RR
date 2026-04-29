"""Version 1 API router."""
from fastapi import APIRouter

from app.api.v1.endpoints import generate, style

router = APIRouter()

# Include endpoints
router.include_router(generate.router, prefix="/generate", tags=["generation"])
router.include_router(style.router, prefix="/style", tags=["style"])
