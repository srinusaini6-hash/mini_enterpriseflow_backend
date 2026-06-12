from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.database import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=False)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True)
    description = Column(Text)
    channel_type = Column(String(50))
    created_by = Column(Integer, nullable=False)

    is_archived = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())