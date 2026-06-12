from pydantic import BaseModel
from datetime import datetime


class ReplyCreate(BaseModel):
    sender_id: int
    content: str


class ReplyResponse(BaseModel):
    id: int
    message_id: int
    sender_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True