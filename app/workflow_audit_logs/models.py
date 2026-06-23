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


class WorkflowAuditLog(Base):
    __tablename__ = "workflow_audit_logs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    execution_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    performed_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    remarks: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )