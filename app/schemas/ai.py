from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AssistantBase(BaseModel):
    name: str
    model: str

class AssistantCreate(AssistantBase):
    id: int

class AssistantRead(AssistantBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AssistantDelete(BaseModel):
    id: int

class AssistantUpdate(AssistantBase):
    id: int

class AiTextRequest(BaseModel):
    message: str

class AiTextResponse(BaseModel):
    message: str