from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from datetime import datetime

from app.database.database import get_db

from app.delegations.models import (
    ApprovalDelegation
)

router = APIRouter(
    prefix="/approval-delegations",
    tags=["Approval Delegations"]
)


# ---------------- CREATE DELEGATION ----------------
@router.post("/")
def create_delegation(
    delegator_id: int,
    delegatee_id: int,
    start_date: datetime,
    end_date: datetime,
    reason: str,
    db: Session = Depends(get_db)
):

    delegation = ApprovalDelegation(
        delegator_id=delegator_id,
        delegatee_id=delegatee_id,
        start_date=start_date,
        end_date=end_date,
        reason=reason,
        is_active=True
    )

    db.add(delegation)

    db.commit()

    db.refresh(delegation)

    return {
        "message": "Delegation created successfully",
        "data": delegation
    }


# ---------------- GET ALL DELEGATIONS ----------------
@router.get("/")
def get_delegations(
    db: Session = Depends(get_db)
):

    delegations = db.query(
        ApprovalDelegation
    ).all()

    return delegations


# ---------------- GET ACTIVE DELEGATIONS ----------------
@router.get("/active")
def get_active_delegations(
    db: Session = Depends(get_db)
):

    active_delegations = db.query(
        ApprovalDelegation
    ).filter(
        ApprovalDelegation.is_active == True
    ).all()

    return active_delegations


# ---------------- EXPIRE DELEGATION ----------------
@router.put("/{delegation_id}/expire")
def expire_delegation(
    delegation_id: int,
    db: Session = Depends(get_db)
):

    delegation = db.query(
        ApprovalDelegation
    ).filter(
        ApprovalDelegation.id == delegation_id
    ).first()

    if not delegation:

        raise HTTPException(
            status_code=404,
            detail="Delegation not found"
        )

    delegation.is_active = False

    db.commit()

    db.refresh(delegation)

    return {
        "message": "Delegation expired successfully",
        "data": delegation
    }