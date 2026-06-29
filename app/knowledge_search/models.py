from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database.database import Base


class KnowledgeSearch(Base):
    __tablename__ = "knowledge_search"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)