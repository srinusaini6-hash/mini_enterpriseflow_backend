from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_analytics.service import (
    template_usage,
    execution_stats,
    approver_workload,
    completion_time
)

router = APIRouter(
    prefix="/workflow-analytics",
    tags=["Workflow Analytics"]
)


@router.get("/templates")
def analytics_templates(
    db: Session = Depends(get_db)
):
    return template_usage(db)


@router.get("/executions")
def analytics_executions(
    db: Session = Depends(get_db)
):
    return execution_stats(db)


@router.get("/approvers")
def analytics_approvers(
    db: Session = Depends(get_db)
):
    return approver_workload(db)


@router.get("/completion-time")
def analytics_completion_time(
    db: Session = Depends(get_db)
):
    return completion_time(db)