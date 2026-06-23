from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_instances.models import WorkflowInstance


def approve_workflow(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    workflow = result.scalar_one_or_none()

    if not workflow:
        return None

    workflow.status = "Completed"

    db.commit()
    db.refresh(workflow)

    return workflow


def reject_workflow(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    workflow = result.scalar_one_or_none()

    if not workflow:
        return None

    workflow.status = "Rejected"

    db.commit()
    db.refresh(workflow)

    return workflow


def hold_workflow(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    workflow = result.scalar_one_or_none()

    if not workflow:
        return None

    workflow.status = "On Hold"

    db.commit()
    db.refresh(workflow)

    return workflow


def resume_workflow(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    workflow = result.scalar_one_or_none()

    if not workflow:
        return None

    workflow.status = "Pending"

    db.commit()
    db.refresh(workflow)

    return workflow


def cancel_workflow(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    workflow = result.scalar_one_or_none()

    if not workflow:
        return None

    workflow.status = "Cancelled"

    db.commit()
    db.refresh(workflow)

    return workflow