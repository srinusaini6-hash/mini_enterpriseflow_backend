from pydantic import BaseModel
from datetime import datetime


class ReassignRequest(BaseModel):
    assigned_to: str
    assigned_by: str


class WorkflowAssignmentResponse(BaseModel):
    id: int
    execution_id: int
    assigned_to: str
    assigned_by: str
    action: str
    assigned_at: datetime

    class Config:
        from_attributes = True