from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.workflow_dashboard.service import (
    get_dashboard_summary,
    get_pending,
    get_completed,
    get_rejected,
    get_overdue
)

router = APIRouter(
    prefix="/workflow-dashboard",
    tags=["Workflow Dashboard"]
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):
    return get_dashboard_summary(db)


@router.get("/pending")
def pending_workflows(
    db: Session = Depends(get_db)
):
    return get_pending(db)


@router.get("/completed")
def completed_workflows(
    db: Session = Depends(get_db)
):
    return get_completed(db)


@router.get("/rejected")
def rejected_workflows(
    db: Session = Depends(get_db)
):
    return get_rejected(db)


@router.get("/overdue")
def overdue_workflows(
    db: Session = Depends(get_db)
):
    return get_overdue(db)