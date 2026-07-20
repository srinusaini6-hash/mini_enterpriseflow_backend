from sqlalchemy.orm import Session

from app.sync_jobs.models import SyncJob
from app.sync_jobs.schemas import (
    SyncJobCreate,
    SyncJobUpdate,
)


def create_sync_job(
    db: Session,
    job: SyncJobCreate
):
    db_job = SyncJob(
        integration_id=job.integration_id,
        job_name=job.job_name,
        sync_type=job.sync_type,
        status=job.status,
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def get_all_sync_jobs(
    db: Session
):
    return db.query(SyncJob).all()


def get_sync_job_by_id(
    db: Session,
    job_id: int
):
    return (
        db.query(SyncJob)
        .filter(SyncJob.id == job_id)
        .first()
    )


def update_sync_job(
    db: Session,
    job_id: int,
    job: SyncJobUpdate
):
    db_job = (
        db.query(SyncJob)
        .filter(SyncJob.id == job_id)
        .first()
    )

    if not db_job:
        return None

    update_data = job.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_job, key, value)

    db.commit()
    db.refresh(db_job)

    return db_job


def delete_sync_job(
    db: Session,
    job_id: int
):
    db_job = (
        db.query(SyncJob)
        .filter(SyncJob.id == job_id)
        .first()
    )

    if not db_job:
        return None

    db.delete(db_job)
    db.commit()

    return db_job