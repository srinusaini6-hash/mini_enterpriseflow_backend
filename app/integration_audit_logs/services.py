from sqlalchemy.orm import Session

from app.integration_audit_logs.repository import (
    get_all_audit_logs,
    get_audit_log_by_id,
    create_audit_log,
    update_audit_log,
    delete_audit_log,
)

from app.integration_audit_logs.schemas import (
    IntegrationAuditLogCreate,
    IntegrationAuditLogUpdate,
)


def get_all_audit_logs_service(db: Session):
    return get_all_audit_logs(db)


def get_audit_log_by_id_service(
    db: Session,
    audit_log_id: int,
):
    return get_audit_log_by_id(
        db,
        audit_log_id,
    )


def create_audit_log_service(
    db: Session,
    audit_log: IntegrationAuditLogCreate,
):
    return create_audit_log(
        db,
        audit_log,
    )


def update_audit_log_service(
    db: Session,
    audit_log_id: int,
    audit_log: IntegrationAuditLogUpdate,
):
    return update_audit_log(
        db,
        audit_log_id,
        audit_log,
    )


def delete_audit_log_service(
    db: Session,
    audit_log_id: int,
):
    return delete_audit_log(
        db,
        audit_log_id,
    )