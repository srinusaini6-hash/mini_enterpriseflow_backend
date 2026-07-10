from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.dependencies import get_current_user

from app.ai_insights.service import AIInsightService
from app.ai_insights.schemas import (
    AIInsightResponse,
    DashboardResponse,
)

router = APIRouter(
    prefix="/ai-insights",
    tags=["AI Insights"],
)


# ---------------------------------------------------------
# Get All AI Insights
# ---------------------------------------------------------
@router.get(
    "",
    response_model=list[AIInsightResponse],
    summary="List AI Insights",
)
def get_ai_insights(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = AIInsightService(db)

    return service.get_all()


# ---------------------------------------------------------
# Generate AI Insights
# ---------------------------------------------------------
@router.post(
    "/generate",
    response_model=list[AIInsightResponse],
    summary="Generate Rule-Based AI Insights",
)
def generate_ai_insights(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = AIInsightService(db)

    return service.generate(current_user.id)


# ---------------------------------------------------------
# Dashboard Summary
# ---------------------------------------------------------
@router.get(
    "/dashboard",
    response_model=DashboardResponse,
    summary="AI Dashboard Summary",
)
def ai_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = AIInsightService(db)

    return service.dashboard()