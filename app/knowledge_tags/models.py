from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class KnowledgeTag(Base):
    __tablename__ = "knowledge_tags"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    article_id: Mapped[int] = mapped_column(
        ForeignKey("knowledge_articles.id"),
        nullable=False
    )

    tag_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )