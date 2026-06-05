from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class MeetingNoteHistory(Base):
    __tablename__ = "meeting_note_history"

    id = Column(Integer, primary_key=True, index=True)
    note_id = Column(Integer, ForeignKey("meeting_notes.id"))
    old_note = Column(Text)

    updated_by = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())