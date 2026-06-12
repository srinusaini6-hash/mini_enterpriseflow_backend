from pydantic import BaseModel
from datetime import datetime


class MessagePinCreate(BaseModel):
    user_id: int


class MessagePinResponse(BaseModel):
    id: int
    message_id: int
    user_id: int
    pinned_at: datetime

    class Config:
        from_attributes = True