from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    sender_id: int
    content: str


class MessageResponse(BaseModel):
    id: int
    channel_id: int
    sender_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True