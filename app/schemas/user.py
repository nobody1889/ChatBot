from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    user_id: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_blocked: bool = False

    model_config = ConfigDict(from_attributes=True)

    @property
    def name(self) -> str:
        return self.first_name or self.username or f"User_{self.user_id}"


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime
