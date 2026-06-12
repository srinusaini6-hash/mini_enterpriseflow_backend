from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=False)
    conversation_type = Column(String(50), nullable=False)  # direct/group
    created_by = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ConversationMember(Base):
    __tablename__ = "conversation_members"

    id = Column(Integer, primary_key=True, index=True)

    conversation_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    joined_at = Column(DateTime(timezone=True), server_default=func.now())    