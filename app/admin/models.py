from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.database import Base


# ---------------- DEPARTMENT MODEL ----------------
class Department(Base):

    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# ---------------- AUDIT LOG MODEL ----------------
class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    module_name = Column(
        String(100),
        nullable=False
    )

    action_type = Column(
        String(100),
        nullable=False
    )

    record_id = Column(
        Integer,
        nullable=True
    )

    old_data = Column(
        String(1000),
        nullable=True
    )

    new_data = Column(
        String(1000),
        nullable=True
    )

    ip_address = Column(
        String(100),
        nullable=True
    )

    user_agent = Column(
        String(255),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )