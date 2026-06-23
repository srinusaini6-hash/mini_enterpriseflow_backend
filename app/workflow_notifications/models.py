from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class WorkflowNotification(Base):
    __tablename__ = "workflow_notifications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    execution_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    user_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Unread"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )