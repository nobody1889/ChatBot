from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    user_id: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_blocked: Optional[bool] = False

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_blocked: Optional[bool]

class UserRead(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

