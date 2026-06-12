from pydantic import BaseModel
from datetime import datetime


class ChannelCreate(BaseModel):
    workspace_id: int
    name: str
    slug: str
    description: str
    channel_type: str


class ChannelUpdate(BaseModel):
    name: str
    description: str
    channel_type: str


class ChannelResponse(BaseModel):
    id: int
    tenant_id: int
    workspace_id: int
    name: str
    slug: str
    description: str
    channel_type: str
    created_by: int
    is_archived: bool
    created_at: datetime

    class Config:
        from_attributes = True