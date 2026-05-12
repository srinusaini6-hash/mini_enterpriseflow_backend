from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.tasks.models import Task

from app.approvals.models import ApprovalRequest

from app.auth.dependencies import get_current_user

from app.users.models import User

import csv

from io import StringIO


router = APIRouter(
    prefix="/exports",
    tags=["Exports"]
)


# ---------------- EXPORT TASKS CSV ----------------
@router.get("/tasks")
def export_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    tasks = db.query(Task).all()

    output = StringIO()

    writer = csv.writer(output)

    # CSV Header
    writer.writerow([
        "ID",
        "Title",
        "Description",
        "Status",
        "Priority"
    ])

    # CSV Data
    for task in tasks:

        writer.writerow([
            task.id,
            task.title,
            task.description,
            task.status,
            task.priority
        ])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=tasks.csv"
        }
    )


# ---------------- EXPORT APPROVALS CSV ----------------
@router.get("/approvals")
def export_approvals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    approvals = db.query(ApprovalRequest).all()

    output = StringIO()

    writer = csv.writer(output)

    # CSV Header
    writer.writerow([
        "ID",
        "Status",
        "Current Approver",
        "Submitted By"
    ])

    # CSV Data
    for approval in approvals:

        writer.writerow([
            approval.id,
            approval.status,
            approval.current_approver,
            approval.submitted_by
        ])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=approvals.csv"
        }
    )