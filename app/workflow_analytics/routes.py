from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_analytics.services import WorkflowAnalyticsService

router = APIRouter(
    prefix="/workflow-analytics",
    tags=["Workflow Analytics"]
)


@router.get("/templates")
def analytics_templates(
    db: Session = Depends(get_db)
):
    return WorkflowAnalyticsService.template_usage(db)


@router.get("/executions")
def analytics_executions(
    db: Session = Depends(get_db)
):
    return WorkflowAnalyticsService.execution_stats(db)


@router.get("/approvers")
def analytics_approvers(
    db: Session = Depends(get_db)
):
    return WorkflowAnalyticsService.approver_workload(db)


@router.get("/completion-time")
def analytics_completion_time(
    db: Session = Depends(get_db)
):
    return WorkflowAnalyticsService.completion_time(db)