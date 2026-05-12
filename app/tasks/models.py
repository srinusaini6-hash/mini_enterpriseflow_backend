from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Boolean,
    DateTime
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.database import Base


class Task(Base):

    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String(255))

    description = Column(Text)

    status = Column(
        String(50),
        default="TODO"
    )

    priority = Column(String(50))

    assigned_to = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_by = Column(Integer)

    # ✅ Soft Delete Fields
    is_deleted = Column(
        Boolean,
        default=False
    )

    deleted_at = Column(
        DateTime,
        nullable=True
    )

    # Relationship
    assigned_user = relationship("User")