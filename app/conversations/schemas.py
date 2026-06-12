from pydantic import BaseModel
from datetime import datetime


class ConversationCreate(BaseModel):
    tenant_id: int
    conversation_type: str
    created_by: int


class ConversationResponse(BaseModel):
    id: int
    tenant_id: int
    conversation_type: str
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True


class MemberCreate(BaseModel):
    user_id: int


class MemberResponse(BaseModel):
    id: int
    conversation_id: int
    user_id: int
    joined_at: datetime

    class Config:
        from_attributes = True