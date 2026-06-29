from datetime import datetime

from pydantic import BaseModel


class KnowledgeArticleCreate(BaseModel):
    tenant_id: int
    category_id: int
    title: str
    content: str
    author_id: int
    status: str = "Draft"
    is_published: bool = False


class KnowledgeArticleUpdate(BaseModel):
    title: str
    content: str
    status: str
    is_published: bool


class KnowledgeArticleResponse(BaseModel):
    id: int
    tenant_id: int
    category_id: int
    title: str
    content: str
    author_id: int
    status: str
    is_published: bool
    created_at: datetime

    class Config:
        from_attributes = True