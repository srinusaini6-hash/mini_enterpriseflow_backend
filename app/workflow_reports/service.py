from sqlalchemy.orm import Session
from app.workflow_instances.models import WorkflowInstance


def get_summary(db: Session):
    total = db.query(WorkflowInstance).count()

    completed = db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Completed"
    ).count()

    pending = db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Pending"
    ).count()

    rejected = db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Rejected"
    ).count()

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
    return db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == status
    ).all()


def get_by_execution(
    db: Session,
    execution_id: int
):
    return db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.id == execution_id
    ).first()