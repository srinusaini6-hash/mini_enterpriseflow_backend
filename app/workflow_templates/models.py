from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean
)

from app.database.database import Base


class WorkflowTemplate(Base):
    __tablename__ = "workflow_templates"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tenant_id = Column(
        Integer,
        nullable=False
    )

    name = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    module_name = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )