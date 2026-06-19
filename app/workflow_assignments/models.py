from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

from app.database.database import Base


class WorkflowAssignment(Base):
    __tablename__ = "workflow_assignments"

    id = Column(Integer, primary_key=True, index=True)

    execution_id = Column(
        Integer,
        ForeignKey("workflow_instances.id")
    )

    assigned_to = Column(String(100))

    assigned_by = Column(String(100))

    action = Column(String(50))

    assigned_at = Column(
        DateTime,
        default=datetime.utcnow
    )