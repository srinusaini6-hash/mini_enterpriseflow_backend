from datetime import date, datetime
from typing import Optional

from sqlalchemy import Date, DateTime, ForeignKey, Index, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class AnalyticsSnapshot(Base):
    __tablename__ = "analytics_snapshots"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    snapshot_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True
    )
    # Example:
    # TASK
    # APPROVAL
    # SLA
    # DOCUMENT
    # PRODUCTIVITY

    snapshot_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True
    )

    data_json: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    __table_args__ = (
        Index(
            "idx_snapshot_tenant_type_date",
            "tenant_id",
            "snapshot_type",
            "snapshot_date",
        ),
    )