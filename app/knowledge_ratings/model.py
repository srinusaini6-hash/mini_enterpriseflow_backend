from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class KnowledgeRating(Base):
    __tablename__ = "knowledge_ratings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    article_id = Column(
        Integer,
        nullable=False
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    rating = Column(
        Integer,
        nullable=False
    )

    feedback = Column(
        String(500)
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )