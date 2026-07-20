from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IntegrationHealthBase(BaseModel):
    integration_id: int
    health_status: str
    response_time: int
    remarks: Optional[str] = None


class IntegrationHealthCreate(IntegrationHealthBase):
    pass


class IntegrationHealthUpdate(BaseModel):
    health_status: Optional[str] = None
    response_time: Optional[int] = None
    remarks: Optional[str] = None
    last_checked: Optional[datetime] = None


class IntegrationHealthResponse(IntegrationHealthBase):
    id: int
    last_checked: datetime

    class Config:
        from_attributes = True