"""OpenAI-compatible chat completions endpoint."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = Field("local", description="Model to use")
    messages: List[ChatMessage]
    max_tokens: Optional[int] = 500
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9
    stream: Optional[bool] = False


class ChatCompletionChoice(BaseModel):
    index: int = 0
    message: ChatMessage
    finish_reason: str = "stop"


class ChatCompletionResponse(BaseModel):
    id: str = "chatcmpl-rr"
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatCompletionChoice]


router = APIRouter()


@router.post("/completions")
async def chat_completions(request: ChatCompletionRequest):
    """OpenAI-compatible chat completions endpoint."""
    from app.services.generation import generate_text
    from app.schemas.generation import GenerationRequest
    import time

    # Extract user prompt from messages
    user_prompt = ""
    for msg in request.messages:
        if msg.role == "user":
            user_prompt = msg.content

    if not user_prompt:
        raise HTTPException(status_code=400, detail="No user message found")

    # Build generation request
    gen_request = GenerationRequest(
        prompt=user_prompt,
        scenario="tech_guides",
        model=None,  # Use default from settings
        max_tokens=request.max_tokens or 500,
        temperature=request.temperature or 0.7,
        top_p=request.top_p or 0.9,
    )

    try:
        generated_text = await generate_text(gen_request, use_rag=False)
        return ChatCompletionResponse(
            created=int(time.time()),
            model=request.model,
            choices=[
                ChatCompletionChoice(
                    message=ChatMessage(role="assistant", content=generated_text)
                )
            ],
        )
    except Exception as e:
        import traceback
        print("Chat error:", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
