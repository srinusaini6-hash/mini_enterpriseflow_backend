from datetime import datetime

from sqlalchemy import (
    Integer,
    ForeignKey,
    String,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class MeetingAttendee(Base):
    __tablename__ = "meeting_attendees"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    meeting_id: Mapped[int] = mapped_column(
        ForeignKey("meetings.id", ondelete="CASCADE")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    response_status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING"
    )

    responded_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )