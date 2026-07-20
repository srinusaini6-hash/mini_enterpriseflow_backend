from sqlalchemy.orm import Session

from app.integration_audit_logs.models import IntegrationAuditLog
from app.integration_audit_logs.schemas import (
    IntegrationAuditLogCreate,
    IntegrationAuditLogUpdate,
)


def get_all_audit_logs(db: Session):
    return db.query(IntegrationAuditLog).all()


def get_audit_log_by_id(db: Session, audit_log_id: int):
    return (
        db.query(IntegrationAuditLog)
        .filter(IntegrationAuditLog.id == audit_log_id)
        .first()
    )


def create_audit_log(
    db: Session,
    audit_log: IntegrationAuditLogCreate,
):
    db_audit_log = IntegrationAuditLog(
        integration_id=audit_log.integration_id,
        action=audit_log.action,
        performed_by=audit_log.performed_by,
        status=audit_log.status,
        remarks=audit_log.remarks,
    )

    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)

    return db_audit_log


def update_audit_log(
    db: Session,
    audit_log_id: int,
    audit_log: IntegrationAuditLogUpdate,
):
    db_audit_log = get_audit_log_by_id(
        db,
        audit_log_id,
    )

    if not db_audit_log:
        return None

    update_data = audit_log.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_audit_log,
            key,
            value,
        )

    db.commit()
    db.refresh(db_audit_log)

    return db_audit_log


def delete_audit_log(
    db: Session,
    audit_log_id: int,
):
    db_audit_log = get_audit_log_by_id(
        db,
        audit_log_id,
    )

    if not db_audit_log:
        return None

    db.delete(db_audit_log)
    db.commit()

    return True