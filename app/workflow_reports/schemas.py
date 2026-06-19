from pydantic import BaseModel


class WorkflowSummary(BaseModel):
    total_workflows: int
    completed: int
    pending: int
    rejected: int


class WorkflowReportResponse(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True