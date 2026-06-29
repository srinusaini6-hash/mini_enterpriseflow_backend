from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class KnowledgeComment(Base):
    __tablename__ = "knowledge_comments"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("knowledge_articles.id"))
    user_id = Column(Integer)
    comment = Column(String(1000))
    created_at = Column(DateTime(timezone=True), server_default=func.now())