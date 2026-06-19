from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from app.database.database import Base


class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_template_id = Column(
        Integer,
        ForeignKey("workflow_templates.id")
    )

    step_order = Column(
        Integer,
        nullable=False
    )

    approver_role = Column(
        String(100),
        nullable=False
    )

    step_name = Column(
        String(255),
        nullable=False
    )

    is_required = Column(
        Boolean,
        default=True
    )