from sqlalchemy import (
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_template_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("workflow_templates.id")
    )

    step_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    approver_role: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    step_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_required: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )