from pydantic import BaseModel
from datetime import datetime


class KnowledgeSearchCreate(BaseModel):
    title: str
    category: str
    content: str


class KnowledgeSearchResponse(KnowledgeSearchCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True