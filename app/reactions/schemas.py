from pydantic import BaseModel
from datetime import datetime


class ReactionCreate(BaseModel):
    user_id: int
    emoji: str


class ReactionResponse(BaseModel):
    id: int
    message_id: int
    user_id: int
    emoji: str
    created_at: datetime

    class Config:
        from_attributes = True