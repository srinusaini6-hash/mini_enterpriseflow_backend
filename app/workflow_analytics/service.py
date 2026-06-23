from sqlalchemy.orm import Session
from sqlalchemy import select

from app.workflow_templates.models import WorkflowTemplate

from app.workflow_instances.models import WorkflowInstance

from app.workflow_instances.workflow_instance_steps.models import (
    WorkflowInstanceStep
)


def template_usage(
    db: Session
):
    stmt = select(WorkflowTemplate)

    result = db.execute(stmt)

    templates = result.scalars().all()

    return [
        {
            "name": template.name,
            "count": 1
        }
        for template in templates
    ]


def execution_stats(
    db: Session
):
    stmt = select(WorkflowInstance)

    result = db.execute(stmt)

    executions = result.scalars().all()

    return {
        "total_executions": len(executions)
    }


def approver_workload(
    db: Session
):
    stmt = select(WorkflowInstanceStep)

    result = db.execute(stmt)

    steps = result.scalars().all()

    return {
        "assigned_steps": len(steps)
    }


def completion_time(
    db: Session
):
    stmt = select(WorkflowInstance).where(
        WorkflowInstance.status == "Completed"
    )

    result = db.execute(stmt)

    completed = result.scalars().all()

    return {
        "completed_workflows": len(completed)
    }