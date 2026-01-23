from fastapi import APIRouter, HTTPException, status
from app.schemas import AiTextResponse, AiTextRequest
from app.core import logging
from app.services.assistant import AssistantClient as AiClient 

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/ai",
    tags=["Ai"],
)

@router.post('/message', response_model=AiTextResponse)
async def message_request(request_body: AiTextRequest):
    message: str = request_body.message

    if not message or not message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message cannot be empty"
        )

    try:
        ai = AiClient()
        response: AiTextResponse = await ai.chat(message=message)
        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in AI message request: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    