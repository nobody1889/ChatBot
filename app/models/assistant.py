from ..db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class Assistant(Base):
    __tablename__ = "ai"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    model: Mapped[str] = mapped_column(String(255), index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="assistants")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False) 
    last_used_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), index=True, nullable=False)

    def __repr__(self):
        return f"<Assistant id={self.id} model={self.model} last_used_at={self.last_used_at}>"