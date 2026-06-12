from datetime import datetime

from pydantic import BaseModel


class ChannelMemberCreate(BaseModel):
    user_id: int


class ChannelMemberResponse(BaseModel):
    id: int
    channel_id: int
    user_id: int
    joined_at: datetime

    class Config:
        from_attributes = True