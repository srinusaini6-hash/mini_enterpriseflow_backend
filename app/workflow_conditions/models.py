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


class WorkflowCondition(Base):
    __tablename__ = "workflow_conditions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    workflow_template_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("workflow_templates.id")
    )

    field_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    operator: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    value: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )