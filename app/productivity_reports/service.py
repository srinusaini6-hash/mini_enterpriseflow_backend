from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.tasks.models import Task
from app.users.models import User

from app.productivity_reports.schemas import (
    ProductivitySummary,
    UserProductivity,
    DepartmentProductivity,
    ProductivityReportResponse,
)


class ProductivityReportService:

    def __init__(self, db: Session):
        self.db = db

    # ---------------------------------------------------------
    # Overall Productivity Report
    # ---------------------------------------------------------
    def overall_report(self) -> ProductivityReportResponse:

        total_tasks = self.db.scalar(
            select(func.count(Task.id))
        ) or 0

        completed_tasks = self.db.scalar(
            select(func.count(Task.id)).where(
                Task.status.in_(["DONE", "Completed", "completed"])
            )
        ) or 0

        pending_tasks = self.db.scalar(
            select(func.count(Task.id)).where(
                Task.status.in_(["TODO", "Pending", "pending"])
            )
        ) or 0

        overdue_tasks = self.db.scalar(
            select(func.count(Task.id)).where(
                Task.status.in_(["OVERDUE", "Overdue", "overdue"])
            )
        ) or 0

        completion_rate = (
            round((completed_tasks / total_tasks) * 100, 2)
            if total_tasks
            else 0
        )

        summary = ProductivitySummary(
            total_tasks=total_tasks,
            completed_tasks=completed_tasks,
            pending_tasks=pending_tasks,
            overdue_tasks=overdue_tasks,
            average_completion_rate=completion_rate,
        )

        return ProductivityReportResponse(
            summary=summary,
            users=self.user_productivity(),
        )

    # ---------------------------------------------------------
    # User Productivity
    # ---------------------------------------------------------
    def user_productivity(self):

        users = self.db.execute(
            select(User)
        ).scalars().all()

        response = []

        for user in users:

            total = self.db.scalar(
                select(func.count(Task.id)).where(
                    Task.assigned_to == user.id
                )
            ) or 0

            completed = self.db.scalar(
                select(func.count(Task.id)).where(
                    Task.assigned_to == user.id,
                    Task.status.in_(["DONE", "Completed", "completed"])
                )
            ) or 0

            pending = self.db.scalar(
                select(func.count(Task.id)).where(
                    Task.assigned_to == user.id,
                    Task.status.in_(["TODO", "Pending", "pending"])
                )
            ) or 0

            overdue = self.db.scalar(
                select(func.count(Task.id)).where(
                    Task.assigned_to == user.id,
                    Task.status.in_(["OVERDUE", "Overdue", "overdue"])
                )
            ) or 0

            rate = (
                round((completed / total) * 100, 2)
                if total
                else 0
            )

            response.append(
                UserProductivity(
                    user_id=user.id,
                    user_name=user.name,
                    total_tasks=total,
                    completed_tasks=completed,
                    pending_tasks=pending,
                    overdue_tasks=overdue,
                    completion_rate=rate,
                )
            )

        return response

    # ---------------------------------------------------------
    # Department Productivity
    # ---------------------------------------------------------
    def department_productivity(self):

        departments = self.db.execute(
            select(
                User.role,
                func.count(Task.id)
            )
            .join(
                Task,
                Task.assigned_to == User.id,
                isouter=True,
            )
            .group_by(User.role)
        ).all()

        response = []

        for role, total in departments:

            completed = self.db.scalar(
                select(func.count(Task.id))
                .join(User, User.id == Task.assigned_to)
                .where(
                    User.role == role,
                    Task.status.in_(["DONE", "Completed", "completed"])
                )
            ) or 0

            rate = (
                round((completed / total) * 100, 2)
                if total
                else 0
            )

            response.append(
                DepartmentProductivity(
                    department=role,
                    total_tasks=total,
                    completed_tasks=completed,
                    completion_rate=rate,
                )
            )

        return response

    # ---------------------------------------------------------
    # Team Productivity
    # ---------------------------------------------------------
    def team_productivity(self):
        return self.department_productivity()