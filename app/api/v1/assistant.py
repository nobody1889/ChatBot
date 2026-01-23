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
    logger.info(f"Creating assistant {data.name} for user {data.user_id}")
    return await service.create_assistant(data)


@router.get("/user/{user_id}", response_model=list[AssistantRead])
async def get_user_assistants(user_id: str, service: AssistantService = Depends(get_assistant_service)):
    return await service.get_user_assistants(user_id)

@router.get("/user/{user_id}/name/{name}", response_model=AssistantRead)
async def get_user_assistant(user_id: str, name: str, service: AssistantService = Depends(get_assistant_service)):
    assistant = await service.get_user_assistant(user_id, name)
    if not assistant:
        raise HTTPException(status_code=404, detail="Assistant not found")
    return assistant


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_assistant( data: AssistantDelete, service: AssistantService = Depends(get_assistant_service)):
    success = await service.delete(data)
    if not success:
        raise HTTPException(status_code=404, detail="Assistant not found")