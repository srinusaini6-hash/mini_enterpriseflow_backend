from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


# ---------------- SLA RULE MODEL ----------------

class SLARule(Base):

    __tablename__ = "sla_rules"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    module_name: Mapped[str] = mapped_column(
        String(100)
    )

    priority: Mapped[str] = mapped_column(
        String(50)
    )

    allowed_hours: Mapped[int] = mapped_column(
        Integer
    )

    escalation_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    escalation_after_hours: Mapped[int] = mapped_column(
        Integer
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id")
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


# ---------------- SLA TRACKING MODEL ----------------

class SLATracking(Base):

    __tablename__ = "sla_tracking"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    module_name: Mapped[str] = mapped_column(
        String(100)
    )

    record_id: Mapped[int] = mapped_column(
        Integer
    )

    sla_rule_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("sla_rules.id")
    )

    start_time: Mapped[datetime] = mapped_column(
        DateTime
    )

    due_time: Mapped[datetime] = mapped_column(
        DateTime
    )

    completed_time: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50)
    )

    breach_reason: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )