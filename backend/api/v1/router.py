"""API v1 router."""

from api.api.v1.endpoints import users
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
