from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)


from datetime import datetime

from app.database.database import Base


class WorkflowNotification(Base):
    __tablename__ = "workflow_notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    execution_id = Column(
        Integer,
        nullable=False
    )

    user_name = Column(
        String(100),
        nullable=False
    )

    message = Column(
        String(500),
        nullable=False
    )

    status = Column(
        String(50),
        default="Unread"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )