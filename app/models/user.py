from ..db import Base
from sqlalchemy import String, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    username: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    firsname: Mapped[str] = mapped_column(String(255), nullable=True)
    lastname: Mapped[str] = mapped_column(String(255), nullable=True)

    user_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.now())