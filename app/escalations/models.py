from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class ApprovalEscalation(Base):

    __tablename__ = "approval_escalations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    approval_id = Column(Integer)

    escalated_from = Column(Integer)

    escalated_to = Column(Integer)

    reason = Column(
        String(255)
    )

    escalation_level = Column(
        Integer,
        default=1
    )

    status = Column(
        String(50),
        default="PENDING"
    )

    escalated_at = Column(
        DateTime,
        default=datetime.utcnow
    )