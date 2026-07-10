from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class ApprovalRequest(Base):

    __tablename__ = "approval_requests"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    request_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    amount: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",
        nullable=False
    )

    submitted_by: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    current_approver: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # ---------------- TASK 4 FIELDS ----------------

    sla_status: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    sla_due_time: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    is_escalated: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    current_escalation_to: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    # ---------------- ANALYTICS FIELD ----------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        index=True
    )


class ApprovalHistory(Base):

    __tablename__ = "approval_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    request_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    action: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    comment: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    action_by: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )