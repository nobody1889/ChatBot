from ..db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.sql import func
from datetime import datetime

class Assistant(Base):
    __tablename__ = "ai"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    name: Mapped[str] = mapped_column(String(100), unique=True)
    model: Mapped[str] = mapped_column(String(255))

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="assistants")

    created_at: Mapped[datetime] = mapped_column(default=func.now()) 
