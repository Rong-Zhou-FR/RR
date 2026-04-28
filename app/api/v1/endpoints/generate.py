"""Text generation endpoint."""
from fastapi import APIRouter, HTTPException
from app.schemas.generation import GenerationRequest, GenerationResponse
from app.services.generation import generate_text

router = APIRouter()

@router.post("/", response_model=GenerationResponse)
async def generate(request: GenerationRequest):
    """Generate text in Rong's style based on scenario."""
    try:
        generated_text = await generate_text(request)
        return GenerationResponse(
            text=generated_text,
            model=request.model,
            scenario=request.scenario
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
