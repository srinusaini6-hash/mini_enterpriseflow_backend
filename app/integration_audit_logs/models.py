from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class IntegrationAuditLog(Base):
    __tablename__ = "integration_audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    integration_id = Column(
        Integer,
        ForeignKey("tenant_integrations.id", ondelete="CASCADE"),
        nullable=False
    )

    action = Column(
        String(100),
        nullable=False
    )

    performed_by = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="SUCCESS"
    )

    remarks = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    integration = relationship(
        "TenantIntegration",
        back_populates="audit_logs"
    )