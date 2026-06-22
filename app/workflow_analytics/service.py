from sqlalchemy.orm import Session

from app.workflow_templates.models import WorkflowTemplate

from app.workflow_instances.models import WorkflowInstance

from app.workflow_instances.workflow_instance_steps.models import (
    WorkflowInstanceStep
)


def template_usage(db: Session):

    templates = db.query(
        WorkflowTemplate
    ).all()

    return [
        {
            "name": template.name,
            "count": 1
        }
        for template in templates
    ]


def execution_stats(db: Session):

    executions = db.query(
        WorkflowInstance
    ).all()

    return {
        "total_executions": len(executions)
    }


def approver_workload(db: Session):

    steps = db.query(
        WorkflowInstanceStep
    ).all()

    return {
        "assigned_steps": len(steps)
    }


def completion_time(db: Session):

    completed = db.query(
        WorkflowInstance
    ).filter(
        WorkflowInstance.status == "Completed"
    ).count()

    return {
        "completed_workflows": completed
    }