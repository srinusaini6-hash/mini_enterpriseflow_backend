from sqlalchemy import (
    Integer,
    String,
    Text,
    Boolean,
    DateTime
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
        String(100)
    )

    reason: Mapped[str] = mapped_column(
        Text
    )

    amount: Mapped[int] = mapped_column(
        Integer
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING"
    )

    submitted_by: Mapped[int] = mapped_column(
        Integer
    )

    current_approver: Mapped[str] = mapped_column(
        String(50)
    )

    comments: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    # TASK 4 FIELDS

    sla_status: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    sla_due_time: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=True
    )

    is_escalated: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    current_escalation_to: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )


class ApprovalHistory(Base):

    __tablename__ = "approval_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    request_id: Mapped[int] = mapped_column(
        Integer
    )

    action: Mapped[str] = mapped_column(
        String(50)
    )

    comment: Mapped[str] = mapped_column(
        Text
    )

    action_by: Mapped[int] = mapped_column(
        Integer
    )