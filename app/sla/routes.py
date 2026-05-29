from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.users.models import User

from app.sla.schemas import (
    SLARuleCreate,
    SLARuleResponse,
    SLATrackingResponse
)

from app.sla import services


router = APIRouter(
    prefix="/sla-rules",
    tags=["SLA Rules"]
)


# ---------------- CREATE SLA RULE ----------------

@router.post("/")
def create_sla_rule(
    data: SLARuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.create_sla_rule_service(
        db,
        data,
        current_user
    )


# ---------------- GET ALL SLA RULES ----------------

@router.get(
    "/",
    response_model=Page[SLARuleResponse]
)
def get_sla_rules(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.get_sla_rules_service(
        db
    )


# ---------------- GET SINGLE SLA RULE ----------------

@router.get(
    "/{sla_id}",
    response_model=SLARuleResponse
)
def get_sla_rule(
    sla_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.get_sla_rule_service(
        sla_id,
        db
    )


# ---------------- START TASK SLA TRACKING ----------------

@router.post("/tracking/tasks/{task_id}")
def start_task_sla(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.start_task_sla_service(
        task_id,
        db
    )


# ---------------- GET ACTIVE SLA RECORDS ----------------

@router.get(
    "/tracking/active",
    response_model=Page[SLATrackingResponse]
)
def get_active_sla(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.get_active_sla_service(
        db
    )


# ---------------- COMPLETE SLA ----------------

@router.put("/tracking/{tracking_id}/complete")
def complete_sla(
    tracking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.complete_sla_service(
        tracking_id,
        db
    )


# ---------------- DELETE SLA RULE ----------------

@router.delete("/{sla_id}")
def delete_sla_rule(
    sla_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return services.delete_sla_rule_service(
        sla_id,
        db
    )