"""Style management endpoint."""
from fastapi import APIRouter, HTTPException
from app.schemas.style import StyleResponse
from app.services.style_loader import get_style

router = APIRouter()

@router.get("/{scenario}", response_model=StyleResponse)
async def get_style_endpoint(scenario: str):
    """Get writing style examples for a scenario."""
    try:
        style_data = get_style(scenario)
        return StyleResponse(**style_data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Style not found: {str(e)}")
