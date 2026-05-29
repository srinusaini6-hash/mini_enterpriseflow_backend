from datetime import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class ApprovalEscalation(Base):

    __tablename__ = "approval_escalations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    approval_id: Mapped[int] = mapped_column()

    escalated_from: Mapped[int] = mapped_column()

    escalated_to: Mapped[int] = mapped_column()

    reason: Mapped[str] = mapped_column(
        nullable=False
    )

    escalation_level: Mapped[int] = mapped_column(
        default=1
    )

    status: Mapped[str] = mapped_column(
        default="PENDING"
    )

    escalated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )