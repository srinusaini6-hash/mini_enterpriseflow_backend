from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.database.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    file_name = Column(String(255))

    file_path = Column(String(500))

    version = Column(Integer, default=1)

    uploaded_by = Column(Integer)
