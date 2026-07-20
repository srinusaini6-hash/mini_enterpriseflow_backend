from datetime import datetime
from typing import Optional, Dict, Any

from pydantic import BaseModel


class WebhookEventBase(BaseModel):
    integration_id: int
    event_type: str
    payload: Dict[str, Any]
    status: str = "PENDING"


class WebhookEventCreate(WebhookEventBase):
    pass


class WebhookEventUpdate(BaseModel):
    event_type: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    processed_at: Optional[datetime] = None


class WebhookEventResponse(WebhookEventBase):
    id: int
    received_at: datetime
    processed_at: Optional[datetime] = None

    class Config:
        from_attributes = True