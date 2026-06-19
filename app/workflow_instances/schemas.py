from pydantic import BaseModel
from datetime import datetime


class WorkflowExecutionStart(BaseModel):
    workflow_template_id: int
    request_id: int


class WorkflowInstanceResponse(BaseModel):
    id: int
    workflow_template_id: int
    request_id: int
    status: str
    started_at: datetime

    class Config:
        from_attributes = True