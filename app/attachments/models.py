from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True, index=True)

    task_id = Column(Integer, nullable=True)

    filename = Column(String(255))

    file_path = Column(String(500))

    file_size = Column(Integer)

    mime_type = Column(String(100))

    uploaded_by = Column(Integer)

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )