from fastapi import APIRouter, HTTPException, status
from app.core import logging
from app.services.accounts.assistant import AssistantService, get_assistant_service
from app.schemas.assistant import AssistantCreate, AssistantDelete, AssistantRead
from fastapi import Depends

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/accounts/assistant",
    tags=["Ai"],
)

@router.post("/", response_model=AssistantRead)
async def create_assistant(data: AssistantCreate, service: AssistantService = Depends(get_assistant_service)):
    try:
        assistant_obj: AssistantRead = await service.create_assistant(data)
        logger.info(f"Assistant created: {assistant_obj.name} for user {assistant_obj.user_id}")
        return assistant_obj
    
    except Exception as e:
        logger.error(f"Error creating assistant: {e}")
        raise


@router.get("/user/{user_id}", response_model=list[AssistantRead])
async def get_user_assistants(user_id: str, service: AssistantService = Depends(get_assistant_service)):
    try:
        assistants: list[AssistantRead] = await service.get_user_assistants(user_id)
        logger.info(f"Retrieved {len(assistants)} assistants for user {user_id}")
        return assistants
    except Exception as e:
        logger.error(f"Error retrieving assistants for user {user_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/user/{user_id}/name/{name}", response_model=AssistantRead)
async def get_user_assistant(user_id: str, name: str, service: AssistantService = Depends(get_assistant_service)):
    try:
        assistant = await service.get_user_assistant(user_id, name)
        if not assistant:
            raise HTTPException(status_code=404, detail="Assistant not found")
        return assistant
    except Exception as e:
        logger.error(f"Error retrieving assistant {name} for user {user_id}: {e}")
        raise 


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_assistant( data: AssistantDelete, service: AssistantService = Depends(get_assistant_service)):
    try:
        success = await service.delete(data)
        if not success:
            raise HTTPException(status_code=404, detail="Assistant not found")
    except ValueError:
        logger.error(f"did not passed id or name for deleting user {data.user_id}")
        raise

    except Exception as e:
        logger.error(f"Error deleting assistant: {e}")
        raise 