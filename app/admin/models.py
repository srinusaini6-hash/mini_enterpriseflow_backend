from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.database.database import Base


class Department(Base):

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True)

class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    action = Column(String(255))

    performed_by = Column(Integer)    