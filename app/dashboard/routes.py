from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.dependencies import get_current_user

from app.users.models import User
from app.tasks.models import Task
from app.approvals.models import ApprovalRequest


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # ---------------- EMPLOYEE DASHBOARD ----------------
    if current_user.role == "employee":

        total_tasks = db.query(Task).filter(
            Task.assigned_to == current_user.id
        ).count()

        completed_tasks = db.query(Task).filter(
            Task.assigned_to == current_user.id,
            Task.status == "DONE"
        ).count()

        pending_tasks = db.query(Task).filter(
            Task.assigned_to == current_user.id,
            Task.status != "DONE"
        ).count()

        requests_submitted = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.submitted_by == current_user.id
        ).count()

        return {
            "role": "employee",
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "requests_submitted": requests_submitted
        }

    # ---------------- MANAGER DASHBOARD ----------------
    elif current_user.role == "manager":

        total_tasks = db.query(Task).count()

        in_progress_tasks = db.query(Task).filter(
            Task.status == "IN_PROGRESS"
        ).count()

        review_tasks = db.query(Task).filter(
            Task.status == "REVIEW"
        ).count()

        pending_approvals = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.current_approver == "manager"
        ).count()

        return {
            "role": "manager",
            "total_tasks": total_tasks,
            "in_progress_tasks": in_progress_tasks,
            "review_tasks": review_tasks,
            "pending_approvals": pending_approvals
        }

    # ---------------- ADMIN DASHBOARD ----------------
    elif current_user.role == "admin":

        total_users = db.query(User).count()

        total_tasks = db.query(Task).count()

        completed_tasks = db.query(Task).filter(
            Task.status == "DONE"
        ).count()

        pending_requests = db.query(
            ApprovalRequest
        ).filter(
            ApprovalRequest.status == "PENDING"
        ).count()

        return {
            "role": "admin",
            "total_users": total_users,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_requests": pending_requests
        }

    # ---------------- INVALID ROLE ----------------
    raise HTTPException(
        status_code=403,
        detail="Invalid role"
    )