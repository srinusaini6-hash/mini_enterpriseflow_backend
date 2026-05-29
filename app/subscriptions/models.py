from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Float
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.database import Base


class SubscriptionPlan(Base):

    __tablename__ = "subscription_plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    monthly_price: Mapped[float] = mapped_column(
        Float
    )

    yearly_price: Mapped[float] = mapped_column(
        Float
    )

    max_users: Mapped[int] = mapped_column(
        Integer
    )

    max_projects: Mapped[int] = mapped_column(
        Integer
    )

    max_storage_mb: Mapped[int] = mapped_column(
        Integer
    )

    max_ai_requests: Mapped[int] = mapped_column(
        Integer
    )

    max_workflows: Mapped[int] = mapped_column(
        Integer
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


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

    status: Mapped[str] = mapped_column(
        String(50),
        default="ACTIVE"
    )

    auto_renew: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    start_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    end_date: Mapped[datetime] = mapped_column(
        DateTime
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )