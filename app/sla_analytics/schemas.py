from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


# ---------------- SLA SUMMARY ----------------

class SLAAnalyticsResponse(BaseModel):

    total_sla_records: int
    active_sla_records: int
    completed_within_sla: int
    breached_sla_count: int
    escalated_sla_count: int

    average_resolution_time: float
    sla_compliance_percentage: float

    model_config = ConfigDict(from_attributes=True)


# ---------------- BREACH RECORD ----------------

class SLABreachRecord(BaseModel):

    task_id: int
    assigned_to: int
    sla_due_time: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------------- SLA TREND ----------------

class SLATrend(BaseModel):

    date: str
    breached: int
    completed: int


class SLATrendResponse(BaseModel):

    trends: List[SLATrend]