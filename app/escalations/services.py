from datetime import datetime

from fastapi import HTTPException

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.escalations.models import (
    ApprovalEscalation
)


# ---------------- CREATE ESCALATION ----------------

def create_escalation_service(
    data,
    db
):

    escalation = ApprovalEscalation(
        approval_id=data.approval_id,
        escalated_from=data.escalated_from,
        escalated_to=data.escalated_to,
        reason=data.reason,
        escalation_level=1,
        status="PENDING",
        escalated_at=datetime.utcnow()
    )

    db.add(escalation)

    db.commit()

    db.refresh(escalation)

    return {
        "message": "Approval escalated successfully",
        "data": escalation
    }


# ---------------- GET ALL ESCALATIONS ----------------

def get_escalations_service(
    db
):

    query = select(
        ApprovalEscalation
    )

    return paginate(
        db,
        query
    )


# ---------------- GET PENDING ESCALATIONS ----------------

def get_pending_escalations_service(
    db
):

    query = select(
        ApprovalEscalation
    ).where(
        ApprovalEscalation.status == "PENDING"
    )

    return paginate(
        db,
        query
    )


# ---------------- RESOLVE ESCALATION ----------------

def resolve_escalation_service(
    escalation_id,
    db
):

    escalation = db.execute(
        select(
            ApprovalEscalation
        ).where(
            ApprovalEscalation.id == escalation_id
        )
    ).scalars().first()

    if not escalation:

        raise HTTPException(
            status_code=404,
            detail="Escalation not found"
        )

    escalation.status = "RESOLVED"

    db.commit()

    db.refresh(escalation)

    return {
        "message": "Escalation resolved successfully",
        "data": escalation
    }