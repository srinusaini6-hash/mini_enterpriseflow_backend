from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


# ---------------- DEPARTMENT MODEL ----------------

class Department(Base):

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


# ---------------- AUDIT LOG MODEL ----------------

class AuditLog(Base):

    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    module_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    action_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    record_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    old_data: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    new_data: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    user_agent: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )