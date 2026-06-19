from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base


class WorkflowCondition(Base):
    __tablename__ = "workflow_conditions"

    id = Column(Integer, primary_key=True, index=True)
    workflow_template_id = Column(
        Integer,
        ForeignKey("workflow_templates.id")
    )

    field_name = Column(String(100))
    operator = Column(String(20))
    value = Column(String(100))