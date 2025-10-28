"""Main FastAPI application entry point."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from api.v1.router import api_router
from api.core.config import settings
from api.core.database import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan events."""
    # Startup
    await init_db()
    yield
    # Shutdown
    # Add cleanup logic here if needed


app = FastAPI(
	title=settings.PROJECT_NAME,
	version=settings.VERSION,
	openapi_url=f"{settings.V1_PREFIX}/openapi.json",
	docs_url=f"{settings.V1_PREFIX}/docs",
	redoc_url=f"{settings.V1_PREFIX}/redoc",
	lifespan=lifespan,
)# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.V1_PREFIX)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
