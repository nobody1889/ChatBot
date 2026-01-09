from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AssistantBase(BaseModel):
    user_id: int
    name: str
    model: Optional[str] = None

class AssistantCreate(AssistantBase):
    pass

class AssistantRead(AssistantBase):
    id: int
    created_at: datetime

class AssistantDelete(BaseModel):
    user_id: int
    name: int

class AssistantUpdate(AssistantBase):
    pass

class AiTextRequest(BaseModel):
    message: str

class AiTextResponse(BaseModel):
    message: str