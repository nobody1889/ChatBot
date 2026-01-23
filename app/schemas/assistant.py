from pydantic import BaseModel, ConfigDict, model_validator
from datetime import datetime
from typing import Optional

class AssistantBase(BaseModel):
    name: str
    model: str

class AssistantCreate(AssistantBase):
    user_id: int

class AssistantRead(AssistantBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AssistantDelete(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    user_id: int

    @model_validator(mode="before")
    def check_id_or_name(self, values):
        if not values.get("id") and not values.get("name"):
            raise ValueError("Must provide either id or name to delete assistant")
        return values
    

class AssistantUpdate(AssistantBase):
    id: int

class AiTextRequest(BaseModel):
    message: str

class AiTextResponse(BaseModel):
    message: str