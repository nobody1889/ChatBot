from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List
from .ai import AssistantCreate

class UserBase(BaseModel):
    user_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    username: str

class UserUpdate(UserBase):
    username: Optional[str] = None
    is_blocked: Optional[bool] = None
    assistants: Optional[List[AssistantCreate]] = None

class UserRead(UserBase):
    id: int
    username: str
    created_at: datetime
    is_blocked: bool = False
    assistants: Optional[List[AssistantCreate]] = None
    model_config = ConfigDict(from_attributes=True)
