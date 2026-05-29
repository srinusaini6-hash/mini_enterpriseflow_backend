from datetime import datetime

from pydantic import BaseModel


# ---------------- CREATE SLA RULE ----------------

class SLARuleCreate(BaseModel):

    module_name: str
    priority: str
    allowed_hours: int
    escalation_enabled: bool
    escalation_after_hours: int


# ---------------- SLA RULE RESPONSE ----------------

class SLARuleResponse(BaseModel):

    id: int
    module_name: str
    priority: str
    allowed_hours: int
    escalation_enabled: bool
    escalation_after_hours: int
    is_active: bool
    created_by: int
    created_at: datetime

    class Config:

        from_attributes = True


# ---------------- SLA TRACKING RESPONSE ----------------

class SLATrackingResponse(BaseModel):

    id: int
    module_name: str
    record_id: int
    sla_rule_id: int
    start_time: datetime
    due_time: datetime
    completed_time: datetime | None
    status: str
    breach_reason: str | None

    class Config:

        from_attributes = True