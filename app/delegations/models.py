from datetime import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class ApprovalDelegation(Base):

    __tablename__ = "approval_delegations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    delegator_id: Mapped[int] = mapped_column()

    delegatee_id: Mapped[int] = mapped_column()

    start_date: Mapped[datetime] = mapped_column()

    end_date: Mapped[datetime] = mapped_column()

    reason: Mapped[str] = mapped_column()

    is_active: Mapped[bool] = mapped_column(
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )