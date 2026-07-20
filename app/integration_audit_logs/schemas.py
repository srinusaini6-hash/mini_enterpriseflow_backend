from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IntegrationAuditLogCreate(BaseModel):
    integration_id: int
    action: str
    performed_by: int
    status: str = "SUCCESS"
    remarks: Optional[str] = None


class IntegrationAuditLogUpdate(BaseModel):
    action: Optional[str] = None
    performed_by: Optional[int] = None
    status: Optional[str] = None
    remarks: Optional[str] = None


class IntegrationAuditLogResponse(BaseModel):
    id: int
    integration_id: int
    action: str
    performed_by: int
    status: str
    remarks: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True