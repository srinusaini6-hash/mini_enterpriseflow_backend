from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_instances.models import WorkflowInstance

from app.workflow_instances.workflow_instance_steps.models import (
    WorkflowInstanceStep
)

from app.workflow_steps.models import WorkflowStep


def start_workflow(
    db: Session,
    workflow_template_id: int,
    request_id: int
):
    workflow_instance = WorkflowInstance(
        workflow_template_id=workflow_template_id,
        request_id=request_id,
        status="Pending"
    )

    db.add(workflow_instance)
    db.commit()
    db.refresh(workflow_instance)

    stmt = (
        select(WorkflowStep)
        .where(
            WorkflowStep.workflow_template_id
            == workflow_template_id
        )
        .order_by(
            WorkflowStep.step_order
        )
    )

    result = db.execute(stmt)

    workflow_steps = result.scalars().all()

    for step in workflow_steps:

        instance_step = WorkflowInstanceStep(
            workflow_instance_id=workflow_instance.id,
            workflow_step_id=step.id,
            assigned_to=None,
            status="Pending"
        )

        db.add(instance_step)

    db.commit()

    return workflow_instance


def get_execution(
    db: Session,
    execution_id: int
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.id == execution_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def get_pending_executions(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Pending"
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_completed_executions(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Completed"
    )

    result = db.execute(stmt)

    return result.scalars().all()


def get_rejected_executions(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Rejected"
    )

    result = db.execute(stmt)

    return result.scalars().all()