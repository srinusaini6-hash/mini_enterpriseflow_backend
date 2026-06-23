from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_instances.workflow_instance_steps.models import (
    WorkflowInstanceStep
)


def create_instance_step(
    db: Session,
    workflow_instance_id: int,
    workflow_step_id: int,
    assigned_to: int = None
):
    step = WorkflowInstanceStep(
        workflow_instance_id=workflow_instance_id,
        workflow_step_id=workflow_step_id,
        assigned_to=assigned_to,
        status="Pending"
    )

    db.add(step)
    db.commit()
    db.refresh(step)

    return step


def get_instance_steps(
    db: Session,
    workflow_instance_id: int
):
    stmt = select(WorkflowInstanceStep).where(
        WorkflowInstanceStep.workflow_instance_id
        == workflow_instance_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_instance_step(
    db: Session,
    step_id: int
):
    stmt = select(WorkflowInstanceStep).where(
        WorkflowInstanceStep.id == step_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def update_instance_step_status(
    db: Session,
    step_id: int,
    status: str
):
    stmt = select(WorkflowInstanceStep).where(
        WorkflowInstanceStep.id == step_id
    )

    result = db.execute(stmt)

    step = result.scalar_one_or_none()

    if not step:
        return None

    step.status = status

    db.commit()
    db.refresh(step)

    return step


def delete_instance_step(
    db: Session,
    step_id: int
):
    stmt = select(WorkflowInstanceStep).where(
        WorkflowInstanceStep.id == step_id
    )

    result = db.execute(stmt)

    step = result.scalar_one_or_none()

    if not step:
        return None

    db.delete(step)
    db.commit()

    return True