from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text
)

from datetime import datetime

from app.database.database import Base


class SavedFilter(Base):

    __tablename__ = "saved_filters"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    filter_name = Column(String(150))

    filter_data = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )