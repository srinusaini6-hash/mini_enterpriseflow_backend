from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class AIMeetingSummary(Base):
    __tablename__ = "ai_meeting_summaries"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    meeting_id = Column(
        Integer,
        nullable=False
    )

    summary = Column(
        Text,
        nullable=False
    )

    decisions = Column(
        Text,
        nullable=True
    )

    action_items = Column(
        Text,
        nullable=True
    )

    suggested_owners = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )