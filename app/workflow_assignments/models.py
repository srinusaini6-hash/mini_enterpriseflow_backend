from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class WorkflowAssignment(Base):
    __tablename__ = "workflow_assignments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    execution_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    assigned_to: Mapped[str] = mapped_column(
        String(100)
    )

    assigned_by: Mapped[str] = mapped_column(
        String(100)
    )

    action: Mapped[str] = mapped_column(
        String(50)
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )