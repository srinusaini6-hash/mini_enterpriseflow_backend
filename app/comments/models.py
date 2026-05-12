from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    task_id = Column(Integer, ForeignKey("tasks.id"))

    user_id = Column(Integer, ForeignKey("users.id"))

    comment_text = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


class CommentReply(Base):
    __tablename__ = "comment_replies"

    id = Column(Integer, primary_key=True, index=True)

    comment_id = Column(Integer, ForeignKey("comments.id"))

    user_id = Column(Integer, ForeignKey("users.id"))

    reply_text = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )