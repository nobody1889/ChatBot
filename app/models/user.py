from ..db import Base
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import func
from datetime import datetime
from .assistant import Assistant

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    username: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)

    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)
    assistants: Mapped[list[Assistant]] = relationship("Assistant", back_populates="user", lazy="selectin", cascade="all, delete-orphan")

    created_at: Mapped[datetime] = mapped_column(default=func.now())
