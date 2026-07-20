from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Text,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class IntegrationCredential(Base):
    __tablename__ = "integration_credentials"

    id = Column(Integer, primary_key=True, index=True)

    tenant_id = Column(
        Integer,
        ForeignKey("tenants.id", ondelete="CASCADE"),
        nullable=False,
    )

    integration_id = Column(
        Integer,
        ForeignKey("tenant_integrations.id", ondelete="CASCADE"),
        nullable=False,
    )

    access_token = Column(
        Text,
        nullable=False,
    )

    refresh_token = Column(
        Text,
        nullable=True,
    )

    api_key = Column(
        Text,
        nullable=True,
    )

    expires_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    tenant = relationship(
        "Tenant",
        backref="integration_credentials",
    )

    integration = relationship(
        "TenantIntegration",
        backref="credentials",
    )