from fastapi import APIRouter
from .user import router as user_router
from .ai import router as ai_router

router = APIRouter()

router.include_router(user_router)
router.include_router(ai_router)