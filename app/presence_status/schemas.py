from pydantic import BaseModel
from datetime import datetime


class PresenceCreate(BaseModel):
    tenant_id: int
    user_id: int
    status: str


class PresenceResponse(BaseModel):
    id: int
    tenant_id: int
    user_id: int
    status: str
    last_seen: datetime

    class Config:
        from_attributes = True