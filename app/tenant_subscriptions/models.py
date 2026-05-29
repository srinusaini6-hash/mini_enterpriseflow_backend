from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class TenantSubscription(Base):

    __tablename__ = "tenant_subscriptions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id")
    )

    plan_id: Mapped[int] = mapped_column(
        ForeignKey("subscription_plans.id")
    )

    billing_cycle: Mapped[str] = mapped_column(
        String(50)
    )

    start_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    end_date: Mapped[datetime] = mapped_column(
        DateTime
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )