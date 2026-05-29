from datetime import datetime

from pydantic import BaseModel


# ---------------- CREATE ESCALATION ----------------

class ApprovalEscalationCreate(BaseModel):

    approval_id: int
    escalated_from: int
    escalated_to: int
    reason: str


# ---------------- ESCALATION RESPONSE ----------------

class ApprovalEscalationResponse(BaseModel):

    id: int
    approval_id: int
    escalated_from: int
    escalated_to: int
    reason: str
    escalation_level: int
    status: str
    escalated_at: datetime

    class Config:

        from_attributes = True