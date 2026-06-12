from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from app.database.database import Base


class ReadReceipt(Base):
    __tablename__ = "read_receipts"

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

    read_at = Column(
        DateTime,
        default=datetime.utcnow
    )