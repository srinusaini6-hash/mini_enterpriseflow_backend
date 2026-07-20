from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)
from sqlalchemy.sql import func

from app.database.database import Base


class IntegrationHealth(Base):
    __tablename__ = "integration_health"

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

    health_status = Column(
        String(50),
        nullable=False,
        default="HEALTHY"
    )

    response_time = Column(
        Integer,
        nullable=False
    )

    last_checked = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    remarks = Column(
        String(255),
        nullable=True
    )