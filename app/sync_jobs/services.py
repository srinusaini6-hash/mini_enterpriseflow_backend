from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.sync_jobs.repository import (
    create_sync_job,
    get_all_sync_jobs,
    get_sync_job_by_id,
    update_sync_job,
    delete_sync_job,
)

from app.sync_jobs.schemas import (
    SyncJobCreate,
    SyncJobUpdate,
)

from app.tenant_integrations.models import TenantIntegration


def create_sync_job_service(
    db: Session,
    job: SyncJobCreate,
):
    integration = (
        db.query(TenantIntegration)
        .filter(
            TenantIntegration.id == job.integration_id
        )
        .first()
    )

    if not integration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant integration not found."
        )

    return create_sync_job(
        db,
        job,
    )


def get_all_sync_jobs_service(
    db: Session,
):
    return get_all_sync_jobs(db)


def get_sync_job_service(
    db: Session,
    job_id: int,
):
    job = get_sync_job_by_id(
        db,
        job_id,
    )

    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sync job not found."
        )

    return job


def update_sync_job_service(
    db: Session,
    job_id: int,
    job: SyncJobUpdate,
):
    updated_job = update_sync_job(
        db,
        job_id,
        job,
    )

    if not updated_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sync job not found."
        )

    return updated_job


def delete_sync_job_service(
    db: Session,
    job_id: int,
):
    deleted_job = delete_sync_job(
        db,
        job_id,
    )

    if not deleted_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sync job not found."
        )

    return {
        "message": "Sync job deleted successfully."
    }