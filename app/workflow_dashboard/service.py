from sqlalchemy.orm import Session

from app.workflow_instances.models import WorkflowInstance


def get_dashboard_summary(db: Session):

    workflows = db.query(
        WorkflowInstance
    ).all()

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


def get_pending(db: Session):
    return db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Pending"
    ).all()


def get_completed(db: Session):
    return db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Completed"
    ).all()


def get_rejected(db: Session):
    return db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Rejected"
    ).all()


def get_overdue(db: Session):
    return db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Overdue"
    ).all()