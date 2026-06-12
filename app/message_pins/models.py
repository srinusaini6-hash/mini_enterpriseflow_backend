from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from app.database.database import Base


class MessagePin(Base):
    __tablename__ = "message_pins"

    id = Column(Integer, primary_key=True, index=True)

    message_id = Column(
        Integer,
        ForeignKey("messages.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    pinned_at = Column(
        DateTime,
        default=datetime.utcnow
    )