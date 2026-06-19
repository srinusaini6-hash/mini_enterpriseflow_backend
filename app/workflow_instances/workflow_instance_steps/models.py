from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.database.database import Base


class WorkflowInstanceStep(Base):
    __tablename__ = "workflow_instance_steps"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_instance_id = Column(
        Integer,
        ForeignKey("workflow_instances.id"),
        nullable=False
    )

    workflow_step_id = Column(
        Integer,
        ForeignKey("workflow_steps.id"),
        nullable=False
    )

    assigned_to = Column(
        Integer,
        nullable=True
    )

    status = Column(
        String(50),
        default="Pending"
    )