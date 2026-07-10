from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    name: str
    count: int


class ExecutionStatsResponse(BaseModel):
    total_executions: int


class ApproverWorkloadResponse(BaseModel):
    assigned_steps: int


class CompletionTimeResponse(BaseModel):
    completed_workflows: int