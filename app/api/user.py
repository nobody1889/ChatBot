from fastapi import APIRouter
from app.schemas.user import UserCreate, UserRead
from app.services.accounts import UserService

router = APIRouter(
    prefix="/accounts/user",
    tags=["User"],
)

@router.get("/", response_model=UserRead)
async def get_user():
    return


@router.post("/", response_model=UserCreate)
async def create_or_update_user():
    return