from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class WebhookEvent(Base):
    __tablename__ = "webhook_events"

    id = Column(Integer, primary_key=True, index=True)

    integration_id = Column(
        Integer,
        ForeignKey("tenant_integrations.id", ondelete="CASCADE"),
        nullable=False
    )

    event_type = Column(
        String(100),
        nullable=False
    )

    payload = Column(
        JSON,
        nullable=False
    )

    status = Column(
        String(50),
        default="PENDING",
        nullable=False
    )

    received_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    processed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    integration = relationship(
        "TenantIntegration",
        back_populates="webhook_events"
    )