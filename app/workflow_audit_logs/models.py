from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class WorkflowAuditLog(Base):
    __tablename__ = "workflow_audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    execution_id = Column(
        Integer,
        nullable=False
    )

    action = Column(
        String(100),
        nullable=False
    )

    performed_by = Column(
        String(100),
        nullable=False
    )

    remarks = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )