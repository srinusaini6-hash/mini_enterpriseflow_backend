from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import (
    get_db
)

# USE EXISTING AUDIT MODEL
from app.admin.models import (
    AuditLog
)

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


# ---------------- CREATE AUDIT LOG ----------------
@router.post("/")
def create_audit_log(
    module_name: str,
    action_type: str,
    record_id: int = None,
    old_data: str = None,
    new_data: str = None,
    ip_address: str = None,
    user_agent: str = None,
    db: Session = Depends(get_db)
):

    audit_log = AuditLog(
        module_name=module_name,
        action_type=action_type,
        record_id=record_id,
        old_data=old_data,
        new_data=new_data,
        ip_address=ip_address,
        user_agent=user_agent
    )

    db.add(audit_log)

    db.commit()

    db.refresh(audit_log)

    return {
        "message": "Audit log created successfully",
        "data": audit_log
    }


# ---------------- GET ALL AUDIT LOGS ----------------
@router.get("/")
def get_audit_logs(
    db: Session = Depends(get_db)
):

    logs = db.query(
        AuditLog
    ).all()

    return logs


# ---------------- GET SINGLE AUDIT LOG ----------------
@router.get("/{log_id}")
def get_audit_log(
    log_id: int,
    db: Session = Depends(get_db)
):

    log = db.query(
        AuditLog
    ).filter(
        AuditLog.id == log_id
    ).first()

    if not log:

        raise HTTPException(
            status_code=404,
            detail="Audit log not found"
        )

    return log

# ---------------- FILTER AUDIT LOGS ----------------
@router.get("/filter/")
def filter_audit_logs(
    module_name: str = None,
    action_type: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(AuditLog)

    if module_name:
        query = query.filter(
            AuditLog.module_name == module_name
        )

    if action_type:
        query = query.filter(
            AuditLog.action_type == action_type
        )

    logs = query.all()

    return logs
