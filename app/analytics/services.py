from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.approvals.models import ApprovalRequest


class ApprovalAnalyticsService:

    @staticmethod
    def get_approval_summary(db: Session):

        total_approvals = db.scalar(
            select(func.count(ApprovalRequest.id))
        )

        pending_approvals = db.scalar(
            select(func.count(ApprovalRequest.id)).where(
                ApprovalRequest.status == "PENDING"
            )
        )

        approved_approvals = db.scalar(
            select(func.count(ApprovalRequest.id)).where(
                ApprovalRequest.status == "FINAL_APPROVED"
            )
        )

        rejected_approvals = db.scalar(
            select(func.count(ApprovalRequest.id)).where(
                ApprovalRequest.status == "REJECTED"
            )
        )

        escalated_approvals = db.scalar(
            select(func.count(ApprovalRequest.id)).where(
                ApprovalRequest.is_escalated.is_(True)
            )
        )

        return {
            "total_approvals": total_approvals or 0,
            "pending_approvals": pending_approvals or 0,
            "approved_approvals": approved_approvals or 0,
            "rejected_approvals": rejected_approvals or 0,
            "escalated_approvals": escalated_approvals or 0,
            "average_turnaround_time_days": 0
        }

    @staticmethod
    def get_approval_bottlenecks(db: Session):

        result = db.execute(
            select(
                ApprovalRequest.current_approver,
                func.count(ApprovalRequest.id).label("pending_count")
            )
            .where(
                ApprovalRequest.status == "PENDING"
            )
            .group_by(
                ApprovalRequest.current_approver
            )
            .order_by(
                func.count(ApprovalRequest.id).desc()
            )
        )

        rows = result.all()

        return [
            {
                "approver": row.current_approver,
                "pending_count": row.pending_count
            }
            for row in rows
        ]

    @staticmethod
    def get_approval_trends(db: Session):

        result = db.execute(
            select(
                func.date(ApprovalRequest.created_at).label("date"),
                func.count(ApprovalRequest.id).label("count")
            )
            .group_by(
                func.date(ApprovalRequest.created_at)
            )
            .order_by(
                func.date(ApprovalRequest.created_at)
            )
        )

        rows = result.all()

        return [
            {
                "date": str(row.date),
                "total_approvals": row.count
            }
            for row in rows
        ]

    @staticmethod
    def get_average_turnaround_time(db: Session):

        return 0