from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.subscriptions.models import (
    SubscriptionPlan
)


def create_plan_service(
    db: Session,
    data
):

    plan = SubscriptionPlan(
        name=data.name,
        monthly_price=data.monthly_price,
        yearly_price=data.yearly_price,
        max_users=data.max_users,
        max_projects=data.max_projects,
        max_storage_mb=data.max_storage_mb,
        max_ai_requests=data.max_ai_requests,
        max_workflows=data.max_workflows
    )

    db.add(plan)

    db.commit()

    db.refresh(plan)

    return plan


def get_plans_service(
    db: Session
):

    query = select(SubscriptionPlan)

    return paginate(
        db,
        query
    )