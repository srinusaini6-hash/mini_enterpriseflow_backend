from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_steps.models import WorkflowStep


def create_workflow_step(
    db: Session,
    template_id: int,
    payload
):
    step = WorkflowStep(
        workflow_template_id=template_id,
        step_order=payload.step_order,
        approver_role=payload.approver_role,
        step_name=payload.step_name,
        is_required=payload.is_required
    )

    db.add(step)
    db.commit()
    db.refresh(step)

    return step


def get_workflow_steps(
    db: Session,
    template_id: int
):
    stmt = select(WorkflowStep).where(
        WorkflowStep.workflow_template_id == template_id
    )

    result = db.execute(stmt)

    return result.scalars().all()


def update_workflow_step(
    db: Session,
    step_id: int,
    payload
):
    stmt = select(WorkflowStep).where(
        WorkflowStep.id == step_id
    )

    result = db.execute(stmt)

    step = result.scalar_one_or_none()

    if not step:
        return None

    step.step_order = payload.step_order
    step.approver_role = payload.approver_role
    step.step_name = payload.step_name
    step.is_required = payload.is_required

    db.commit()
    db.refresh(step)

    return step


def delete_workflow_step(
    db: Session,
    step_id: int
):
    stmt = select(WorkflowStep).where(
        WorkflowStep.id == step_id
    )

    result = db.execute(stmt)

    step = result.scalar_one_or_none()

    if not step:
        return None

    db.delete(step)
    db.commit()

    return True