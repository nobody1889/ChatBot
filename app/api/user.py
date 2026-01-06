from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserRead
from app.services.accounts import UserService, UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.core.logging import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/accounts/user",
    tags=["User"],
)

def get_user_service(db : AsyncSession = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

@router.post("/", response_model=UserCreate)
async def create_or_update_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        user_obj = await user_service.update_or_create(user)
        logger.info(f"User created or updated: {user_obj}")

        return UserRead.model_validate(user_obj)
    
    except Exception as e:
        logger.error(f"Error creating or updating user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating or updating user"
        )
    
@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        user_obj = await user_service.get_by_user_id(user_id)

        if not user_obj:
            logger.info(f"User not found: {user_id}")

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        logger.info(f"User found: {user_obj}")

        return UserRead.model_validate(user_obj)
    
    except Exception as e:
        logger.error(f"Error getting user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting user"
        )
    
@router.put("/{user_id}", response_model=UserCreate)
async def update_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        user_obj = await user_service.update_user(user)

        if not user_obj:
            logger.info(f"User not found: {user_obj.user_id}")

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User not found"
            )
        
        logger.info(f"User updated: {user_obj}")
        return UserRead.model_validate(user_obj)
    
    except Exception as e:
        logger.error(f"Error updating user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating user"
        )

@router.patch("/{user_id}/block", response_model=UserCreate)
async def block_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        success = await user_service.block_user(user_id)

        if not success:
            logger.info(f"User not found: {user_id}")   

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User not found"
            )
        
        logger.info(f"User blocked: {user_id}")
        return {"status": status.HTTP_200_OK, "message": f" user {user_id} blocked"}
    
    except Exception as e:
        logger.error(f"Error blocking user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error blocking user"
        )

@router.patch("/{user_id}/unblock", response_model=UserCreate)
async def unblock_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        success = await user_service.unblock_user(user_id)

        if not success:
            logger.info(f"User not found: {user_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        logger.info(f"User unblocked: {user_id}")
        return {"status": status.HTTP_200_OK, "message": f" user {user_id} unblocked"}
    
    except Exception as e:
        logger.error(f"Error unblocking user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error unblocking user"
        )