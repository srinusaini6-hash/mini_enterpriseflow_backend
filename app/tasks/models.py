from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Text,
    ForeignKey,
    Boolean,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.database import Base


class Task(Base):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="TODO"
    )

    priority: Mapped[str] = mapped_column(
        String(50)
    )

    assigned_to: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    created_by: Mapped[int] = mapped_column(
        Integer
    )

    # TASK 4 FIELDS

    sla_status: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    sla_due_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    is_sla_breached: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # SOFT DELETE

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    deleted_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

    # RELATIONSHIP

    assigned_user = relationship(
        "User"
    )