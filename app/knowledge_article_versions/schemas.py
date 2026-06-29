from pydantic import BaseModel
from datetime import datetime


class KnowledgeArticleVersionCreate(BaseModel):
    article_id: int
    version_number: str
    content: str


class KnowledgeArticleVersionResponse(BaseModel):
    id: int
    article_id: int
    version_number: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True