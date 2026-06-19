from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_workflows: int
    pending: int
    completed: int
    rejected: int
    overdue: int