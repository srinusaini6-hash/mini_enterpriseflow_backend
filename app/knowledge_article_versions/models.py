from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class KnowledgeArticleVersion(Base):
    __tablename__ = "knowledge_article_versions"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("knowledge_articles.id"))
    version_number = Column(String(20))
    content = Column(String(5000))
    created_at = Column(DateTime(timezone=True), server_default=func.now())