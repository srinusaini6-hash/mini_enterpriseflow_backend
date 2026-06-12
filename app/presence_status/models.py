from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class PresenceStatus(Base):
    __tablename__ = "presence_status"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    last_seen = Column(DateTime(timezone=True), server_default=func.now())
    socket_session_id = Column(String(255), nullable=True)