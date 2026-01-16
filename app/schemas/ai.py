from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AssistantBase(BaseModel):
    user_id: int
    name: str
    model: str

class AssistantCreate(AssistantBase):
    pass

class AssistantRead(AssistantBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AssistantDelete(BaseModel):
    user_id: int
    name: int

class AssistantUpdate(AssistantBase):
    pass

class AiTextRequest(BaseModel):
    message: str

class AiTextResponse(BaseModel):
    message: str