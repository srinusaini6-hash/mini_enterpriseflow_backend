from pydantic import BaseModel
from datetime import datetime


class KnowledgeRatingCreate(BaseModel):
    article_id: int
    user_id: int
    rating: int
    feedback: str


class KnowledgeRatingResponse(
    KnowledgeRatingCreate
):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True