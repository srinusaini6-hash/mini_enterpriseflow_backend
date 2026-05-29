from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.subscriptions.schemas import (
    SubscriptionPlanCreate,
    SubscriptionPlanResponse
)

from app.subscriptions.services import (
    create_plan_service,
    get_plans_service
)


router = APIRouter(
    prefix="/subscription-plans",
    tags=["Subscription Plans"]
)


# ---------------- CREATE PLAN ----------------

@router.post(
    "/",
    response_model=SubscriptionPlanResponse
)
def create_plan(
    data: SubscriptionPlanCreate,
    db: Session = Depends(get_db)
):

    return create_plan_service(
        db,
        data
    )


# ---------------- GET ALL PLANS ----------------

@router.get(
    "/",
    response_model=Page[SubscriptionPlanResponse]
)
def get_plans(
    db: Session = Depends(get_db)
):

    return get_plans_service(
        db
    )