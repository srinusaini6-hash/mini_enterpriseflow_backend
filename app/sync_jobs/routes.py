from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.sync_jobs.schemas import (
    SyncJobCreate,
    SyncJobUpdate,
    SyncJobResponse,
)

from app.sync_jobs.services import (
    create_sync_job_service,
    get_all_sync_jobs_service,
    get_sync_job_service,
    update_sync_job_service,
    delete_sync_job_service,
)

router = APIRouter(
    prefix="/sync-jobs",
    tags=["Sync Jobs"],
)


# Create Sync Job
@router.post(
    "",
    response_model=SyncJobResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_sync_job(
    job: SyncJobCreate,
    db: Session = Depends(get_db),
):
    return create_sync_job_service(
        db,
        job,
    )


# Get All Sync Jobs
@router.get(
    "",
    response_model=list[SyncJobResponse],
)
def get_all_sync_jobs(
    db: Session = Depends(get_db),
):
    return get_all_sync_jobs_service(db)


# Get Sync Job By ID
@router.get(
    "/{job_id}",
    response_model=SyncJobResponse,
)
def get_sync_job(
    job_id: int,
    db: Session = Depends(get_db),
):
    return get_sync_job_service(
        db,
        job_id,
    )


# Update Sync Job
@router.put(
    "/{job_id}",
    response_model=SyncJobResponse,
)
def update_sync_job(
    job_id: int,
    job: SyncJobUpdate,
    db: Session = Depends(get_db),
):
    return update_sync_job_service(
        db,
        job_id,
        job,
    )


# Delete Sync Job
@router.delete(
    "/{job_id}",
)
def delete_sync_job(
    job_id: int,
    db: Session = Depends(get_db),
):
    return delete_sync_job_service(
        db,
        job_id,
    )