from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.sla.models import SLATracking


class SLAAnalyticsService:

    @staticmethod
    def get_sla_summary(db: Session):

        total = db.scalar(
            select(func.count(SLATracking.id))
        ) or 0

        active = db.scalar(
            select(func.count(SLATracking.id))
            .where(SLATracking.status == "ACTIVE")
        ) or 0

        completed = db.scalar(
            select(func.count(SLATracking.id))
            .where(SLATracking.status == "COMPLETED")
        ) or 0

        breached = db.scalar(
            select(func.count(SLATracking.id))
            .where(SLATracking.status == "BREACHED")
        ) or 0

        escalated = db.scalar(
            select(func.count(SLATracking.id))
            .where(SLATracking.status == "ESCALATED")
        ) or 0

        compliance = 0

        if total > 0:
            compliance = round((completed / total) * 100, 2)

        return {
            "total_sla_records": total,
            "active_sla_records": active,
            "completed_within_sla": completed,
            "breached_sla_count": breached,
            "escalated_sla_count": escalated,
            "average_resolution_time": 0,
            "sla_compliance_percentage": compliance
        }

    @staticmethod
    def get_sla_breaches(db: Session):

        result = db.execute(
            select(SLATracking).where(
                SLATracking.status == "BREACHED"
            )
        )

        rows = result.scalars().all()

        return [
            {
                "record_id": row.record_id,
                "module_name": row.module_name,
                "sla_rule_id": row.sla_rule_id,
                "status": row.status,
                "breach_reason": row.breach_reason,
                "start_time": row.start_time,
                "due_time": row.due_time,
                "completed_time": row.completed_time,
                "created_at": row.created_at
            }
            for row in rows
        ]

    @staticmethod
    def get_sla_trends(db: Session):

        breached = db.execute(
            select(
                func.date(SLATracking.created_at).label("date"),
                func.count().label("count")
            )
            .where(
                SLATracking.status == "BREACHED"
            )
            .group_by(
                func.date(SLATracking.created_at)
            )
            .order_by(
                func.date(SLATracking.created_at)
            )
        ).all()

        completed = db.execute(
            select(
                func.date(SLATracking.created_at).label("date"),
                func.count().label("count")
            )
            .where(
                SLATracking.status == "COMPLETED"
            )
            .group_by(
                func.date(SLATracking.created_at)
            )
            .order_by(
                func.date(SLATracking.created_at)
            )
        ).all()

        data = {}

        for row in breached:
            data[str(row.date)] = {
                "date": str(row.date),
                "breached": row.count,
                "completed": 0
            }

        for row in completed:
            if str(row.date) not in data:
                data[str(row.date)] = {
                    "date": str(row.date),
                    "breached": 0,
                    "completed": row.count
                }
            else:
                data[str(row.date)]["completed"] = row.count

        return list(data.values())