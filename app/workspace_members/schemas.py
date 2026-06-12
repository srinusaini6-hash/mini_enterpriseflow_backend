from pydantic import BaseModel
from datetime import datetime


class WorkspaceMemberCreate(BaseModel):
    user_id: int
    role: str


class WorkspaceMemberResponse(BaseModel):
    id: int
    workspace_id: int
    user_id: int
    role: str
    joined_at: datetime
    is_active: bool

    class Config:
        from_attributes = True