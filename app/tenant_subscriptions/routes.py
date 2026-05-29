from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.tenant_subscriptions.schemas import (
    TenantSubscriptionCreate,
    TenantSubscriptionResponse
)

from app.tenant_subscriptions.services import (
    assign_subscription_service,
    get_subscriptions_service,
    get_single_subscription_service,
    cancel_subscription_service
)


router = APIRouter(
    prefix="/tenant-subscriptions",
    tags=["Tenant Subscriptions"]
)


# ---------------- ASSIGN SUBSCRIPTION ----------------

@router.post(
    "/",
    response_model=TenantSubscriptionResponse
)
def assign_subscription(
    data: TenantSubscriptionCreate,
    db: Session = Depends(get_db)
):

    subscription = assign_subscription_service(
        db,
        data
    )

    return subscription


# ---------------- GET ALL SUBSCRIPTIONS ----------------

@router.get(
    "/",
    response_model=Page[TenantSubscriptionResponse]
)
def get_subscriptions(
    db: Session = Depends(get_db)
):

    return get_subscriptions_service(db)


# ---------------- GET SINGLE SUBSCRIPTION ----------------

@router.get(
    "/{subscription_id}",
    response_model=TenantSubscriptionResponse
)
def get_single_subscription(
    subscription_id: int,
    db: Session = Depends(get_db)
):

    subscription = get_single_subscription_service(
        db,
        subscription_id
    )

    if not subscription:

        raise HTTPException(
            status_code=404,
            detail="Subscription not found"
        )

    return subscription


# ---------------- CANCEL SUBSCRIPTION ----------------

@router.put(
    "/{subscription_id}/cancel",
    response_model=TenantSubscriptionResponse
)
def cancel_subscription(
    subscription_id: int,
    db: Session = Depends(get_db)
):

    subscription = cancel_subscription_service(
        db,
        subscription_id
    )

    if not subscription:

        raise HTTPException(
            status_code=404,
            detail="Subscription not found"
        )

    return subscription