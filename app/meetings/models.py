from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class Meeting(Base):

    __tablename__ = "meetings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    meeting_type: Mapped[str] = mapped_column(
        String(50)
    )

    workspace_id: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime
    )

    end_time: Mapped[datetime] = mapped_column(
        DateTime
    )

    location: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    meeting_link: Mapped[str] = mapped_column(
        String(500),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="SCHEDULED"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )