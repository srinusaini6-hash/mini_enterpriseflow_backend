from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database.database import Base


class MeetingReminder(Base):
    __tablename__ = "meeting_reminders"

    id = Column(Integer, primary_key=True, index=True)

    meeting_id = Column(
        Integer,
        ForeignKey("meetings.id"),
        nullable=False
    )

    reminder_time = Column(DateTime, nullable=False)

    status = Column(
        String(50),
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )