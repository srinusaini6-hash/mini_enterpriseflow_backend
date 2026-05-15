from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class ApprovalDelegation(Base):

    __tablename__ = "approval_delegations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    delegator_id = Column(Integer)

    delegatee_id = Column(Integer)

    start_date = Column(DateTime)

    end_date = Column(DateTime)

    reason = Column(
        String(255)
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )