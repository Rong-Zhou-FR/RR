"""FastAPI application entry point."""
from fastapi import FastAPI
from app.api.v1.router import router as v1_router

app = FastAPI(
    title="RR (Robotika Ron)",
    description="Text generation AI agent to write text in Rong's style",
    version="0.1.0"
)

# Include version 1 API router
app.include_router(v1_router, prefix="/v1")
