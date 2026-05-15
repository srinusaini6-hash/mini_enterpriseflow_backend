from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime
)

from app.database.database import Base


class ApprovalRequest(Base):

    __tablename__ = "approval_requests"

    id = Column(Integer, primary_key=True, index=True)

    request_type = Column(String(100))

    reason = Column(Text)

    amount = Column(Integer)

    status = Column(String(50), default="PENDING")

    submitted_by = Column(Integer)

    current_approver = Column(String(50))

    comments = Column(Text)

    # TASK 4 FIELDS
    sla_status = Column(String, nullable=True)

    sla_due_time = Column(DateTime, nullable=True)

    is_escalated = Column(Boolean, default=False)

    current_escalation_to = Column(Integer, nullable=True)


class ApprovalHistory(Base):

    __tablename__ = "approval_history"

    id = Column(Integer, primary_key=True, index=True)

    request_id = Column(Integer)

    action = Column(String(50))

    comment = Column(Text)

    action_by = Column(Integer)