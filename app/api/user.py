from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserCreate, UserRead, UserUpdate
from app.services.accounts import   UserService, get_user_service
from app.core import logging
from fastapi.exceptions import FastAPIError 
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/accounts/user",
    tags=["User"],
)

@router.post("/", response_model=UserRead)
async def create_or_update_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        user_obj = await user_service.update_or_create(user)
        logger.info(f"User created or updated: {user_obj.username or user_obj.user_id}")
        return UserRead.model_validate(user_obj)
    
    except FastAPIError as e:
        logger.error(f"fastapi error in create or update: {e}")

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
        
        logger.info(f"User found: {user_obj.username or user_obj.user_id}")

        return UserRead.model_validate(user_obj)
    
    except HTTPException as e:
        raise
    
    except Exception as e:
        logger.error(f"Error getting user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting user"
        )
    
@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: str, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    try:
        user_obj = await user_service.update_user(user_id, user)

        if not user_obj:
            logger.info(f"User not found: {user_id}")

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="User not found"
            )
        
        logger.info(f"User updated: {user_obj}")
        return UserRead.model_validate(user_obj)
    
    except HTTPException as e:
        raise
    
    except Exception as e:
        logger.error(f"Error updating user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating user"
        )

@router.patch("/{user_id}/block")
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
    
    except HTTPException as e:
        raise
    
    except Exception as e:
        logger.error(f"Error blocking user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error blocking user"
        )

@router.patch("/{user_id}/unblock")
async def unblock_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        success = await user_service.unblock_user(user_id)

        if not success:
            logger.info(f"User not found: {user_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        logger.info(f"User unblocked: {user_id}")
        return {"status": status.HTTP_200_OK, "message": f" user {user_id} unblocked"}
    
    except HTTPException as e:
        raise
    
    except Exception as e:
        logger.error(f"Error unblocking user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error unblocking user"
        )

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        success = await user_service.delete_user(user_id)

        if not success:
            logger.info(f"User not found: {user_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        logger.info(f"User deleted: {user_id}")
        return {"status": status.HTTP_200_OK, "message": f" user {user_id} get delete"}
    
    except HTTPException as e:
        raise
    
    except Exception as e:
        logger.error(f"Error deleting user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting user"
        )