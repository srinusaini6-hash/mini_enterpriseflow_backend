from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)
from sqlalchemy.sql import func

from app.database.database import Base


class SyncJob(Base):
    __tablename__ = "sync_jobs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    integration_id = Column(
        Integer,
        ForeignKey(
            "tenant_integrations.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    job_name = Column(
        String(100),
        nullable=False
    )

    sync_type = Column(
        String(50),
        nullable=False
    )

    status = Column(
        String(50),
        default="PENDING",
        nullable=False
    )

    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )