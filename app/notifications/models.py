from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base  


class Notification(Base):

    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    message = Column(String(255))

    user_id = Column(Integer)

    is_read = Column(Boolean, default=False)