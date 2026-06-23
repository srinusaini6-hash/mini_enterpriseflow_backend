from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_instances.models import WorkflowInstance


def get_dashboard_summary(
    db: Session
):
    stmt = select(WorkflowInstance)

    result = db.execute(stmt)

    workflows = result.scalars().all()

    total = len(workflows)

    pending = len(
        [w for w in workflows if w.status == "Pending"]
    )

    completed = len(
        [w for w in workflows if w.status == "Completed"]
    )

    rejected = len(
        [w for w in workflows if w.status == "Rejected"]
    )

    overdue = len(
        [w for w in workflows if w.status == "Overdue"]
    )

    return {
        "total_workflows": total,
        "pending": pending,
        "completed": completed,
        "rejected": rejected,
        "overdue": overdue
    }


def get_pending(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Pending"
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_completed(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Completed"
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_rejected(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Rejected"
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_overdue(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Overdue"
    )

    result = db.execute(stmt)

    return result.scalars().all()