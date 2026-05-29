from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi import HTTPException

from fastapi_pagination.ext.sqlalchemy import paginate

from app.subscriptions.models import (
    TenantSubscription,
    SubscriptionPlan
)

from app.tenants.models import Tenant


# ---------------- ASSIGN SUBSCRIPTION ----------------

def assign_subscription_service(
    db: Session,
    data
):

    tenant = db.execute(
        select(Tenant).where(
            Tenant.id == data.tenant_id
        )
    ).scalars().first()

    if not tenant:

        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    plan = db.execute(
        select(SubscriptionPlan).where(
            SubscriptionPlan.id == data.plan_id
        )
    ).scalars().first()

    if not plan:

        raise HTTPException(
            status_code=404,
            detail="Subscription plan not found"
        )

    subscription = TenantSubscription(
        tenant_id=data.tenant_id,
        plan_id=data.plan_id,
        billing_cycle=data.billing_cycle,
        end_date=data.end_date,
        status="ACTIVE",
        auto_renew=True
    )

    db.add(subscription)

    db.commit()

    db.refresh(subscription)

    return subscription


# ---------------- GET ALL SUBSCRIPTIONS ----------------

def get_subscriptions_service(
    db: Session
):

    query = select(
        TenantSubscription
    )

    return paginate(
        db,
        query
    )


# ---------------- GET SINGLE SUBSCRIPTION ----------------

def get_single_subscription_service(
    db: Session,
    subscription_id: int
):

    subscription = db.execute(
        select(TenantSubscription).where(
            TenantSubscription.id == subscription_id
        )
    ).scalars().first()

    return subscription


# ---------------- CANCEL SUBSCRIPTION ----------------

def cancel_subscription_service(
    db: Session,
    subscription_id: int
):

    subscription = db.execute(
        select(TenantSubscription).where(
            TenantSubscription.id == subscription_id
        )
    ).scalars().first()

    if not subscription:

        return None

    subscription.status = "CANCELLED"

    db.commit()

    db.refresh(subscription)

    return subscription