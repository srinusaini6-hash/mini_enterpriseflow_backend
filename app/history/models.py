from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.database import Base


class TaskHistory(Base):

    __tablename__ = "task_history"

    id = Column(Integer, primary_key=True, index=True)

    task_id = Column(Integer)

    changed_by = Column(Integer)

    field_name = Column(String(100))

    old_value = Column(String(255))

    new_value = Column(String(255))

    changed_at = Column(
        DateTime,
        default=datetime.utcnow
    )