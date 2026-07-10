from datetime import datetime
from typing import List

from pydantic import BaseModel


# ---------------------------------------------------------
# Create AI Insight
# ---------------------------------------------------------
class AIInsightCreate(BaseModel):
    insight_type: str
    title: str
    description: str
    severity: str = "LOW"


# ---------------------------------------------------------
# AI Insight Response
# ---------------------------------------------------------
class AIInsightResponse(BaseModel):
    id: int
    tenant_id: int | None = None
    insight_type: str
    title: str
    description: str
    severity: str
    generated_at: datetime
    generated_by: int | None = None

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# Dashboard Summary
# ---------------------------------------------------------
class DashboardSummary(BaseModel):
    total_insights: int
    high_severity: int
    medium_severity: int
    low_severity: int
    critical_severity: int

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# Dashboard Response
# ---------------------------------------------------------
class DashboardResponse(BaseModel):
    summary: DashboardSummary
    insights: List[AIInsightResponse]

    class Config:
        from_attributes = True