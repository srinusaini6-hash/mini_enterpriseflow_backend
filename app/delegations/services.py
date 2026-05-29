from fastapi import HTTPException

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.delegations.models import (
    ApprovalDelegation
)


# ---------------- CREATE DELEGATION ----------------

def create_delegation_service(
    data,
    db
):

    delegation = ApprovalDelegation(
        delegator_id=data.delegator_id,
        delegatee_id=data.delegatee_id,
        start_date=data.start_date,
        end_date=data.end_date,
        reason=data.reason,
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

def get_delegations_service(
    db
):

    query = select(
        ApprovalDelegation
    )

    return paginate(
        db,
        query
    )


# ---------------- GET ACTIVE DELEGATIONS ----------------

def get_active_delegations_service(
    db
):

    query = select(
        ApprovalDelegation
    ).where(
        ApprovalDelegation.is_active == True
    )

    return paginate(
        db,
        query
    )


# ---------------- EXPIRE DELEGATION ----------------

def expire_delegation_service(
    delegation_id,
    db
):

    delegation = db.execute(
        select(
            ApprovalDelegation
        ).where(
            ApprovalDelegation.id == delegation_id
        )
    ).scalars().first()

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