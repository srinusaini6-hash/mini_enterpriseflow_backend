from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
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

class ApprovalHistory(Base):

    __tablename__ = "approval_history"

    id = Column(Integer, primary_key=True, index=True)

    request_id = Column(Integer)

    action = Column(String(50))

    comment = Column(Text)

    action_by = Column(Integer)    
