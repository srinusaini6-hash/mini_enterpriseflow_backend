from datetime import (
    datetime,
    timedelta
)

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.sla.models import (
    SLARule,
    SLATracking
)

from app.tasks.models import Task

from app.schemas.sla_schema import (
    SLARuleCreate
)


router = APIRouter(
    prefix="/sla-rules",
    tags=["SLA Rules"]
)


# ---------------- CREATE SLA RULE ----------------
@router.post("/")
def create_sla_rule(
    data: SLARuleCreate,
    db: Session = Depends(get_db)
):

    sla_rule = SLARule(
        module_name=data.module_name,
        priority=data.priority,
        allowed_hours=data.allowed_hours,
        escalation_enabled=data.escalation_enabled,
        escalation_after_hours=data.escalation_after_hours
    )

    db.add(sla_rule)

    db.commit()

    db.refresh(sla_rule)

    return {
        "message": "SLA Rule created successfully",
        "data": sla_rule
    }


# ---------------- GET ALL SLA RULES ----------------
@router.get("/")
def get_sla_rules(
    db: Session = Depends(get_db)
):

    rules = db.query(SLARule).all()

    return rules


# ---------------- GET SINGLE SLA RULE ----------------
@router.get("/{sla_id}")
def get_sla_rule(
    sla_id: int,
    db: Session = Depends(get_db)
):

    rule = db.query(SLARule).filter(
        SLARule.id == sla_id
    ).first()

    if not rule:

        raise HTTPException(
            status_code=404,
            detail="SLA Rule not found"
        )

    return rule


# ---------------- START TASK SLA TRACKING ----------------
@router.post("/tracking/tasks/{task_id}")
def start_task_sla(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    sla_rule = db.query(SLARule).filter(
        SLARule.module_name == "tasks"
    ).first()

    if not sla_rule:

        raise HTTPException(
            status_code=404,
            detail="SLA Rule not found"
        )

    start_time = datetime.utcnow()

    due_time = start_time + timedelta(
        hours=sla_rule.allowed_hours
    )

    tracking = SLATracking(
        module_name="tasks",
        record_id=task.id,
        sla_rule_id=sla_rule.id,
        start_time=start_time,
        due_time=due_time,
        status="ACTIVE"
    )

    db.add(tracking)

    # UPDATE TASK SLA STATUS
    task.sla_status = "ACTIVE"

    task.sla_due_time = due_time

    db.commit()

    db.refresh(tracking)

    return {
        "message": "Task SLA started successfully",
        "data": tracking
    }


# ---------------- GET ACTIVE SLA RECORDS ----------------
@router.get("/tracking/active")
def get_active_sla(
    db: Session = Depends(get_db)
):

    records = db.query(SLATracking).filter(
        SLATracking.status == "ACTIVE"
    ).all()

    return records


# ---------------- COMPLETE SLA ----------------
@router.put("/tracking/{tracking_id}/complete")
def complete_sla(
    tracking_id: int,
    db: Session = Depends(get_db)
):

    tracking = db.query(SLATracking).filter(
        SLATracking.id == tracking_id
    ).first()

    if not tracking:

        raise HTTPException(
            status_code=404,
            detail="Tracking record not found"
        )

    tracking.status = "COMPLETED"

    tracking.completed_time = datetime.utcnow()

    db.commit()

    return {
        "message": "SLA completed successfully"
    }


# ---------------- DELETE SLA RULE ----------------
@router.delete("/{sla_id}")
def delete_sla_rule(
    sla_id: int,
    db: Session = Depends(get_db)
):

    rule = db.query(SLARule).filter(
        SLARule.id == sla_id
    ).first()

    if not rule:

        raise HTTPException(
            status_code=404,
            detail="SLA Rule not found"
        )

    db.delete(rule)

    db.commit()

    return {
        "message": "SLA Rule deleted successfully"
    }