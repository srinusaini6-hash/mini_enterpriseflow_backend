from sqlalchemy import select
from sqlalchemy.orm import Session

from app.workflow_templates.models import WorkflowTemplate
from app.workflow_instances.models import WorkflowInstance
from app.workflow_steps.models import WorkflowStep


class WorkflowAnalyticsService:

    @staticmethod
    def template_usage(db: Session):

        result = db.execute(
            select(WorkflowTemplate)
        )

        templates = result.scalars().all()

        return [
            {
                "name": template.name,
                "count": 1
            }
            for template in templates
        ]

    @staticmethod
    def execution_stats(db: Session):

        result = db.execute(
            select(WorkflowInstance)
        )

        executions = result.scalars().all()

        return {
            "total_executions": len(executions)
        }

    @staticmethod
    def approver_workload(db: Session):

        result = db.execute(
            select(WorkflowStep)
        )

        steps = result.scalars().all()

        return {
            "assigned_steps": len(steps)
        }

    @staticmethod
    def completion_time(db: Session):

        result = db.execute(
            select(WorkflowInstance).where(
                WorkflowInstance.status == "Completed"
            )
        )

        completed = result.scalars().all()

        return {
            "completed_workflows": len(completed)
        }