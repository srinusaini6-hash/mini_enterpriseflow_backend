from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SyncJobBase(BaseModel):
    integration_id: int
    job_name: str
    sync_type: str
    status: str = "PENDING"


class SyncJobCreate(SyncJobBase):
    pass


class SyncJobUpdate(BaseModel):
    job_name: Optional[str] = None
    sync_type: Optional[str] = None
    status: Optional[str] = None
    completed_at: Optional[datetime] = None


class SyncJobResponse(SyncJobBase):
    id: int
    started_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True