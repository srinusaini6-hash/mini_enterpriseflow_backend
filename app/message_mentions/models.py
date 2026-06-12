from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database.database import Base

class MessageMention(Base):
    __tablename__ = "message_mentions"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("messages.id"))
    mentioned_user_id = Column(Integer)
    mention_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)