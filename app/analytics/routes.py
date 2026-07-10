from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.analytics.schemas import (
    ApprovalAnalyticsResponse,
    ApprovalTrendResponse,
    ApprovalBottleneckResponse
)

from app.analytics.services import (
    ApprovalAnalyticsService
)

router = APIRouter(
    prefix="/analytics/approvals",
    tags=["Approval Analytics"]
)


@router.get(
    "",
    response_model=ApprovalAnalyticsResponse
)
def get_approval_analytics(
    db: Session = Depends(get_db)
):
    return ApprovalAnalyticsService.get_approval_summary(db)


@router.get(
    "/bottlenecks",
    response_model=List[ApprovalBottleneckResponse]
)
def get_approval_bottlenecks(
    db: Session = Depends(get_db)
):
    return ApprovalAnalyticsService.get_approval_bottlenecks(db)


@router.get(
    "/trends",
    response_model=List[ApprovalTrendResponse]
)
def get_approval_trends(
    db: Session = Depends(get_db)
):
    return ApprovalAnalyticsService.get_approval_trends(db)