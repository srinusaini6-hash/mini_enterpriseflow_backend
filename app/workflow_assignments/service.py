from sqlalchemy.orm import Session

from app.workflow_assignments.models import WorkflowAssignment
from app.workflow_instances.models import WorkflowInstance


def get_assignees(
    db: Session,
    execution_id: int
):
    return db.query(
        WorkflowAssignment
    ).filter(
        WorkflowAssignment.execution_id == execution_id
    ).all()


def reassign_workflow(
    db: Session,
    execution_id: int,
    assigned_to: str,
    assigned_by: str
):
    execution = db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.id == execution_id
    ).first()

    if not execution:
        return None

    assignment = WorkflowAssignment(
        execution_id=execution_id,
        assigned_to=assigned_to,
        assigned_by=assigned_by,
        action="Reassigned"
    )

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return assignment


def get_history(
    db: Session,
    execution_id: int
):
    return db.query(
        WorkflowAssignment
    ).filter(
        WorkflowAssignment.execution_id == execution_id
    ).all()