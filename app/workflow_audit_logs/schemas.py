from pydantic import BaseModel
from datetime import datetime


class AuditLogCreate(BaseModel):
    execution_id: int
    action: str
    performed_by: str
    remarks: str | None = None


class AuditLogResponse(BaseModel):
    id: int
    execution_id: int
    action: str
    performed_by: str
    remarks: str | None
    created_at: datetime

    class Config:
        from_attributes = True