from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.delegations.schemas import (
    ApprovalDelegationCreate,
    ApprovalDelegationResponse
)

from app.delegations import services


router = APIRouter(
    prefix="/approval-delegations",
    tags=["Approval Delegations"]
)


# ---------------- CREATE DELEGATION ----------------

@router.post("/")
def create_delegation(
    data: ApprovalDelegationCreate,
    db: Session = Depends(get_db)
):

    return services.create_delegation_service(
        data,
        db
    )


# ---------------- GET ALL DELEGATIONS ----------------

@router.get(
    "/",
    response_model=Page[ApprovalDelegationResponse]
)
def get_delegations(
    db: Session = Depends(get_db)
):

    return services.get_delegations_service(
        db
    )


# ---------------- GET ACTIVE DELEGATIONS ----------------

@router.get(
    "/active",
    response_model=Page[ApprovalDelegationResponse]
)
def get_active_delegations(
    db: Session = Depends(get_db)
):

    return services.get_active_delegations_service(
        db
    )


# ---------------- EXPIRE DELEGATION ----------------

@router.put("/{delegation_id}/expire")
def expire_delegation(
    delegation_id: int,
    db: Session = Depends(get_db)
):

    return services.expire_delegation_service(
        delegation_id,
        db
    )