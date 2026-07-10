from sqlalchemy import select, func
from sqlalchemy.orm import Session
from app.approvals.models import ApprovalRequest

from app.ai_insights.models import AIInsight
from app.ai_insights.schemas import (
    AIInsightCreate,
    DashboardSummary,
    DashboardResponse,
)

from app.tasks.models import Task
from app.approvals.models import ApprovalRequest


class AIInsightService:

    def __init__(self, db: Session):
        self.db = db

    # ---------------------------------------------------------
    # List AI Insights
    # ---------------------------------------------------------
    def get_all(self):

        return self.db.execute(
            select(AIInsight).order_by(
                AIInsight.generated_at.desc()
            )
        ).scalars().all()

    # ---------------------------------------------------------
    # Generate Rule-Based AI Insights
    # ---------------------------------------------------------
    def generate(self, user_id: int):

        insights = []

        # High Priority Pending Tasks
        pending_high = self.db.scalar(
            select(func.count(Task.id)).where(
                Task.priority.in_(["HIGH", "High"]),
                Task.status.in_(["TODO", "Pending"])
            )
        ) or 0

        if pending_high > 0:

            insight = AIInsight(
                insight_type="TASK",
                title="High Priority Pending Tasks",
                description=f"There are {pending_high} high priority tasks pending.",
                severity="HIGH",
                generated_by=user_id,
            )

            self.db.add(insight)

            insights.append(insight)

        # Pending Approvals
        pending_approvals = self.db.scalar(
            select(func.count(ApprovalRequest.id)).where(
                ApprovalRequest.status == "PENDING"
            )
        ) or 0

        if pending_approvals > 0:

            insight = AIInsight(
                insight_type="APPROVAL",
                title="Pending Approvals",
                description=f"{pending_approvals} approval requests are pending.",
                severity="MEDIUM",
                generated_by=user_id,
            )

            self.db.add(insight)

            insights.append(insight)

        self.db.commit()

        return insights

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------
    def dashboard(self):

        total = self.db.scalar(
            select(func.count(AIInsight.id))
        ) or 0

        high = self.db.scalar(
            select(func.count(AIInsight.id)).where(
                AIInsight.severity == "HIGH"
            )
        ) or 0

        medium = self.db.scalar(
            select(func.count(AIInsight.id)).where(
                AIInsight.severity == "MEDIUM"
            )
        ) or 0

        low = self.db.scalar(
            select(func.count(AIInsight.id)).where(
                AIInsight.severity == "LOW"
            )
        ) or 0

        critical = self.db.scalar(
            select(func.count(AIInsight.id)).where(
                AIInsight.severity == "CRITICAL"
            )
        ) or 0

        summary = DashboardSummary(
            total_insights=total,
            high_severity=high,
            medium_severity=medium,
            low_severity=low,
            critical_severity=critical,
        )

        insights = self.get_all()

        return DashboardResponse(
            summary=summary,
            insights=insights,
        )