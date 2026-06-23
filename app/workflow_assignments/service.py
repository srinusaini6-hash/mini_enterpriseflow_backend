from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_assignments.models import WorkflowAssignment

from app.workflow_instances.models import WorkflowInstance


def get_assignees(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowAssignment).where(
        WorkflowAssignment.execution_id == execution_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def reassign_workflow(
    db: Session,
    execution_id: int,
    assigned_to: str,
    assigned_by: str
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    execution = result.scalar_one_or_none()

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
    stmt = select(WorkflowAssignment).where(
        WorkflowAssignment.execution_id == execution_id
    )

    result = db.execute(stmt)

    return result.scalars().all()