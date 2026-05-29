from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.escalations.schemas import (
    ApprovalEscalationCreate,
    ApprovalEscalationResponse
)

from app.escalations import services


router = APIRouter(
    prefix="/approval-escalations",
    tags=["Approval Escalations"]
)


# ---------------- CREATE ESCALATION ----------------

@router.post("/")
def create_escalation(
    data: ApprovalEscalationCreate,
    db: Session = Depends(get_db)
):

    return services.create_escalation_service(
        data,
        db
    )


# ---------------- GET ALL ESCALATIONS ----------------

@router.get(
    "/",
    response_model=Page[ApprovalEscalationResponse]
)
def get_escalations(
    db: Session = Depends(get_db)
):

    return services.get_escalations_service(
        db
    )


# ---------------- GET PENDING ESCALATIONS ----------------

@router.get(
    "/pending",
    response_model=Page[ApprovalEscalationResponse]
)
def get_pending_escalations(
    db: Session = Depends(get_db)
):

    return services.get_pending_escalations_service(
        db
    )


# ---------------- RESOLVE ESCALATION ----------------

@router.put("/{escalation_id}/resolve")
def resolve_escalation(
    escalation_id: int,
    db: Session = Depends(get_db)
):

    return services.resolve_escalation_service(
        escalation_id,
        db
    )