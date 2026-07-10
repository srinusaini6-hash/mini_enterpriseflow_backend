from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.dependencies import get_current_user
from app.users.models import User

from app.sla_analytics.services import SLAAnalyticsService
from app.sla_analytics.schemas import SLAAnalyticsResponse


router = APIRouter(
    prefix="/analytics/sla",
    tags=["SLA Analytics"]
)


@router.get(
    "",
    response_model=SLAAnalyticsResponse
)
def get_sla_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return SLAAnalyticsService.get_sla_summary(db)


@router.get("/breaches")
def get_sla_breaches(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return SLAAnalyticsService.get_sla_breaches(db)


@router.get("/trends")
def get_sla_trends(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return SLAAnalyticsService.get_sla_trends(db)