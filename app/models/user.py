from ..db import Base
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    username: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)

    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(default=func.now())
