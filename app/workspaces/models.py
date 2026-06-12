from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True)

    tenant_id = Column(Integer, nullable=False)

    name = Column(String(255), nullable=False)

    slug = Column(String(255), unique=True)

    description = Column(Text)

    visibility = Column(String(50), default="PRIVATE")

    created_by = Column(Integer, nullable=False)

    is_archived = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )