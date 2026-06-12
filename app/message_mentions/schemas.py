from pydantic import BaseModel
from datetime import datetime


class MentionCreate(BaseModel):
    mentioned_user_id: int
    mention_type: str


class MentionResponse(BaseModel):
    id: int
    message_id: int
    mentioned_user_id: int
    mention_type: str
    created_at: datetime

    class Config:
        from_attributes = True