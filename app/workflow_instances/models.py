from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database.database import Base


class WorkflowInstance(Base):
    __tablename__ = "workflow_instances"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_template_id = Column(
        Integer,
        ForeignKey("workflow_templates.id"),
        nullable=False
    )

    request_id = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String(50),
        default="Pending"
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )