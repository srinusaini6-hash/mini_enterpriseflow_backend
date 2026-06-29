from datetime import datetime

from pydantic import BaseModel


class KnowledgeTagCreate(BaseModel):
    article_id: int
    tag_name: str


class KnowledgeTagResponse(BaseModel):
    id: int
    article_id: int
    tag_name: str
    created_at: datetime

    class Config:
        from_attributes = True