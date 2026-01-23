from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from .assistant import AssistantRead

class UserBase(BaseModel):
    user_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    username: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_blocked: Optional[bool] = None

class UserRead(BaseModel):
    id: int
    user_id: str
    first_name: str
    last_name: str
    username: str

    assistants: List[AssistantRead] = []

    is_blocked: bool = False
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
