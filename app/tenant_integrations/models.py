from datetime import datetime
from typing import Optional
from sqlalchemy.orm import relationship

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.database import Base


class TenantIntegration(Base):
    __tablename__ = "tenant_integrations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[int] = mapped_column(
        ForeignKey("integration_providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    integration_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="CONNECTED",
        nullable=False,
        index=True,
    )

    config_json: Mapped[Optional[dict]] = mapped_column(
        JSONB,
        nullable=True,
    )

    connected_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    connected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    last_sync_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    webhook_events = relationship(
        "WebhookEvent",
        back_populates="integration",
        cascade="all, delete-orphan",
    )

    audit_logs = relationship(
    "IntegrationAuditLog",
    back_populates="integration",
    cascade="all, delete-orphan"
)   