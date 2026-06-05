from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class ActionItem(Base):
    __tablename__ = "action_items"

    id = Column(Integer, primary_key=True, index=True)

    meeting_id = Column(
        Integer,
        ForeignKey("meetings.id"),
        nullable=False
    )

    title = Column(String(255), nullable=False)

    owner_id = Column(Integer, nullable=False)

    due_date = Column(Date, nullable=False)

    status = Column(
        String(50),
        default="PENDING"
    )

    task_id = Column(Integer, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )