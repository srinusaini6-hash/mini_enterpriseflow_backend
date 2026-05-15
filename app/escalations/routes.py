from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from datetime import datetime

from app.database.database import get_db

from app.escalations.models import (
    ApprovalEscalation
)

router = APIRouter(
    prefix="/approval-escalations",
    tags=["Approval Escalations"]
)


# ---------------- CREATE ESCALATION ----------------
@router.post("/")
def create_escalation(
    approval_id: int,
    escalated_from: int,
    escalated_to: int,
    reason: str,
    db: Session = Depends(get_db)
):

    escalation = ApprovalEscalation(
        approval_id=approval_id,
        escalated_from=escalated_from,
        escalated_to=escalated_to,
        reason=reason,
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
@router.get("/")
def get_escalations(
    db: Session = Depends(get_db)
):

    escalations = db.query(
        ApprovalEscalation
    ).all()

    return escalations


# ---------------- GET PENDING ESCALATIONS ----------------
@router.get("/pending")
def get_pending_escalations(
    db: Session = Depends(get_db)
):

    pending = db.query(
        ApprovalEscalation
    ).filter(
        ApprovalEscalation.status == "PENDING"
    ).all()

    return pending


# ---------------- RESOLVE ESCALATION ----------------
@router.put("/{escalation_id}/resolve")
def resolve_escalation(
    escalation_id: int,
    db: Session = Depends(get_db)
):

    escalation = db.query(
        ApprovalEscalation
    ).filter(
        ApprovalEscalation.id == escalation_id
    ).first()

    if not escalation:

        raise HTTPException(
            status_code=404,
            detail="Escalation not found"
        )

    escalation.status = "RESOLVED"

    db.commit()

    return {
        "message": "Escalation resolved successfully"
    }