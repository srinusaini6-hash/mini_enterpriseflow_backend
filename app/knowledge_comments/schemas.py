from pydantic import BaseModel
from datetime import datetime


class KnowledgeCommentCreate(BaseModel):
    article_id: int
    user_id: int
    comment: str


class KnowledgeCommentResponse(BaseModel):
    id: int
    article_id: int
    user_id: int
    comment: str
    created_at: datetime

    class Config:
        from_attributes = True