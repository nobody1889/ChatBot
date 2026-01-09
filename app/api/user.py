from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserCreate, UserRead, UserUpdate
from app.services.accounts import   UserService, get_user_service
from app.core import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/accounts/user",
    tags=["User"],
)

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
    
@router.put("/{user_id}", response_model=UserRead)
async def update_user(user: UserUpdate, user_service: UserService = Depends(get_user_service)):
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
    
    except Exception as e:
        logger.error(f"Error unblocking user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error unblocking user"
        )

@router.get('/all_users')
async def get_all_users(service: UserService = Depends(get_user_service)):
    users = await service.get_all_users()
    
    if not users:
        return {
            "status":"success",
            "message":"no user in db"
        }
    
    return {
        "status":"success",
        "message":"all users in response",
        "response": users
    }



@router.get('/{user_id}/delete')
async def delete_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    try:
        response = await user_service.delete_user(user_id)

        if not response:
            logger.info(f"User not found: {user_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        logger.info(f"User deleted: {user_id}")
        return {"status": status.HTTP_200_OK, "message": f" user {user_id} get delete"}
    
    except Exception as e:
        logger.error(f"Error deleting user: {e}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting user"
        )