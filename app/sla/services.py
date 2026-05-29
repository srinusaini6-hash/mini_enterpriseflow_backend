from datetime import (
    datetime,
    timedelta
)

from fastapi import HTTPException

from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.sla.models import (
    SLARule,
    SLATracking
)

from app.tasks.models import Task

from app.users.models import User


# ---------------- CREATE SLA RULE ----------------

def create_sla_rule_service(
    db: Session,
    data,
    current_user: User
):

    sla_rule = SLARule(
        module_name=data.module_name,
        priority=data.priority,
        allowed_hours=data.allowed_hours,
        escalation_enabled=data.escalation_enabled,
        escalation_after_hours=data.escalation_after_hours,
        created_by=current_user.id
    )

    db.add(sla_rule)

    db.commit()

    db.refresh(sla_rule)

    return {
        "message": "SLA Rule created successfully",
        "data": sla_rule
    }


# ---------------- GET ALL SLA RULES ----------------

def get_sla_rules_service(
    db: Session
):

    query = select(SLARule)

    return paginate(
        db,
        query
    )


# ---------------- GET SINGLE SLA RULE ----------------

def get_sla_rule_service(
    sla_id: int,
    db: Session
):

    rule = db.execute(
        select(SLARule).where(
            SLARule.id == sla_id
        )
    ).scalars().first()

    if not rule:

        raise HTTPException(
            status_code=404,
            detail="SLA Rule not found"
        )

    return rule


# ---------------- START TASK SLA TRACKING ----------------

def start_task_sla_service(
    task_id: int,
    db: Session
):

    task = db.execute(
        select(Task).where(
            Task.id == task_id,
            Task.is_deleted == False
        )
    ).scalars().first()

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    sla_rule = db.execute(
        select(SLARule).where(
            SLARule.module_name == "TASKS",
            SLARule.priority == task.priority,
            SLARule.is_active == True
        )
    ).scalars().first()

    if not sla_rule:

        raise HTTPException(
            status_code=404,
            detail="SLA Rule not found for this task priority"
        )

    start_time = datetime.utcnow()

    due_time = start_time + timedelta(
        hours=sla_rule.allowed_hours
    )

    tracking = SLATracking(
        module_name="TASKS",
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

def get_active_sla_service(
    db: Session
):

    query = select(SLATracking).where(
        SLATracking.status == "ACTIVE"
    )

    return paginate(
        db,
        query
    )


# ---------------- COMPLETE SLA ----------------

def complete_sla_service(
    tracking_id: int,
    db: Session
):

    tracking = db.execute(
        select(SLATracking).where(
            SLATracking.id == tracking_id
        )
    ).scalars().first()

    if not tracking:

        raise HTTPException(
            status_code=404,
            detail="Tracking record not found"
        )

    tracking.status = "COMPLETED"

    tracking.completed_time = datetime.utcnow()

    db.commit()

    db.refresh(tracking)

    return {
        "message": "SLA completed successfully"
    }


# ---------------- DELETE SLA RULE ----------------

def delete_sla_rule_service(
    sla_id: int,
    db: Session
):

    rule = db.execute(
        select(SLARule).where(
            SLARule.id == sla_id
        )
    ).scalars().first()

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