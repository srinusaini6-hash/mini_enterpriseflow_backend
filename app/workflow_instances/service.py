from sqlalchemy.orm import Session

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

    workflow_steps = (
        db.query(WorkflowStep)
        .filter(
            WorkflowStep.workflow_template_id
            == workflow_template_id
        )
        .order_by(WorkflowStep.step_order)
        .all()
    )

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
    return (
        db.query(WorkflowInstance)
        .filter(
            WorkflowInstance.id == execution_id
        )
        .first()
    )


def get_pending_executions(
    db: Session
):
    return (
        db.query(WorkflowInstance)
        .filter(
            WorkflowInstance.status == "Pending"
        )
        .all()
    )


def get_completed_executions(
    db: Session
):
    return (
        db.query(WorkflowInstance)
        .filter(
            WorkflowInstance.status == "Completed"
        )
        .all()
    )


def get_rejected_executions(
    db: Session
):
    return (
        db.query(WorkflowInstance)
        .filter(
            WorkflowInstance.status == "Rejected"
        )
        .all()
    )