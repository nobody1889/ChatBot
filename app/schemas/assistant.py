from pydantic import BaseModel, ConfigDict, model_validator
from datetime import datetime
from typing import Optional

class AssistantBase(BaseModel):
    model: str
    user_id: str

class AssistantCreate(AssistantBase):
    pass

class AssistantRead(BaseModel):
    id: int
    created_at: datetime
    model: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)

class AssistantDelete(BaseModel):
    id: Optional[int] = None

    user_id: str

    @model_validator(mode="before")
    def check_id_or_name(cls, values):
        if not values.get("id") and not values.get("model"):
            raise ValueError("Must provide either id or model to delete assistant")
        return values
    

class AssistantUpdate(AssistantBase):
    pass

class AiTextRequest(BaseModel):
    message: str

class AiTextResponse(BaseModel):
    message: str