from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AiTextRequest(BaseModel):
    message: str

class AiTextResponse(BaseModel):
    message: str