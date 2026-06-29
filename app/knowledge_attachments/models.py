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


class KnowledgeAttachment(Base):
    __tablename__ = "knowledge_attachments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    article_id: Mapped[int] = mapped_column(
        ForeignKey("knowledge_articles.id")
    )

    file_name: Mapped[str] = mapped_column(
        String(255)
    )

    file_path: Mapped[str] = mapped_column(
        String(500)
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )