from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from app.database.database import Base


class ChannelMember(Base):

    __tablename__ = "channel_members"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    channel_id = Column(
        Integer,
        ForeignKey("channels.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )