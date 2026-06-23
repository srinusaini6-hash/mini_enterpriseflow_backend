from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_instances.models import WorkflowInstance


def get_summary(
    db: Session
):
    stmt = select(WorkflowInstance)

    result = db.execute(stmt)

    workflows = result.scalars().all()

    total = len(workflows)

    completed = len(
        [w for w in workflows if w.status == "Completed"]
    )

    pending = len(
        [w for w in workflows if w.status == "Pending"]
    )

    rejected = len(
        [w for w in workflows if w.status == "Rejected"]
    )

    return {
        "total_workflows": total,
        "completed": completed,
        "pending": pending,
        "rejected": rejected
    }


def get_by_status(
    db: Session,
    status: str
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == status
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_by_execution(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()