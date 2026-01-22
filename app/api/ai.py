from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import AiTextResponse, AiTextRequest
from app.core import logging
from app.services.assistant import AiClient

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/ai",
    tags=["Ai"],
)

@router.post('/message', response_model=AiTextResponse)
async def message_request(request_body: AiTextRequest):
    try:
        message: str = request_body.message

        if not message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Missing 'message' field in request body."
            )
        
        ai = AiClient()
        response:AiTextResponse = await ai.chat(message=message)

        return response
    
    except Exception as e:
        logger.error(f"Error while Ai message request: {e}")
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error while Ai message request"
            )

