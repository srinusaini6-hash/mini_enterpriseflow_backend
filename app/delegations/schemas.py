from datetime import datetime

from pydantic import BaseModel


# ---------------- CREATE DELEGATION ----------------

class ApprovalDelegationCreate(BaseModel):

    delegator_id: int

    delegatee_id: int

    start_date: datetime

    end_date: datetime

    reason: str


# ---------------- DELEGATION RESPONSE ----------------

class ApprovalDelegationResponse(BaseModel):

    id: int

    delegator_id: int

    delegatee_id: int

    start_date: datetime

    end_date: datetime

    reason: str

    is_active: bool

    created_at: datetime

    class Config:

        from_attributes = True