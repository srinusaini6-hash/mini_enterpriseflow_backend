from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database.database import Base


class SLARule(Base):

    __tablename__ = "sla_rules"

    id = Column(Integer, primary_key=True, index=True)

    module_name = Column(String(100))

    priority = Column(String(50))

    allowed_hours = Column(Integer)

    escalation_enabled = Column(Boolean, default=False)

    escalation_after_hours = Column(Integer)

    is_active = Column(Boolean, default=True)

    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class SLATracking(Base):

    __tablename__ = "sla_tracking"

    id = Column(Integer, primary_key=True, index=True)

    module_name = Column(String(100))

    record_id = Column(Integer)

    sla_rule_id = Column(
        Integer,
        ForeignKey("sla_rules.id")
    )

    start_time = Column(DateTime)

    due_time = Column(DateTime)

    completed_time = Column(
        DateTime,
        nullable=True
    )

    status = Column(String(50))

    breach_reason = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )