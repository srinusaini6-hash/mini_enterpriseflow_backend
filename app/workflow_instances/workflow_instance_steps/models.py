from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class WorkflowInstanceStep(Base):
    __tablename__ = "workflow_instance_steps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_instance_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("workflow_instances.id"),
        nullable=False
    )

    workflow_step_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("workflow_steps.id"),
        nullable=False
    )

    assigned_to: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Pending"
    )