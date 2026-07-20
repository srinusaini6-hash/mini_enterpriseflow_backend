from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.integration_health.schemas import (
    IntegrationHealthCreate,
    IntegrationHealthUpdate,
    IntegrationHealthResponse,
)

from app.integration_health.services import (
    create_integration_health_service,
    get_all_integration_health_service,
    get_integration_health_service,
    update_integration_health_service,
    delete_integration_health_service,
)

router = APIRouter(
    prefix="/integration-health",
    tags=["Integration Health"],
)


# Create Integration Health
@router.post(
    "",
    response_model=IntegrationHealthResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_integration_health(
    health: IntegrationHealthCreate,
    db: Session = Depends(get_db),
):
    return create_integration_health_service(
        db,
        health,
    )


# Get All Integration Health
@router.get(
    "",
    response_model=list[IntegrationHealthResponse],
)
def get_all_integration_health(
    db: Session = Depends(get_db),
):
    return get_all_integration_health_service(db)


# Get Integration Health By ID
@router.get(
    "/{health_id}",
    response_model=IntegrationHealthResponse,
)
def get_integration_health(
    health_id: int,
    db: Session = Depends(get_db),
):
    return get_integration_health_service(
        db,
        health_id,
    )


# Update Integration Health
@router.put(
    "/{health_id}",
    response_model=IntegrationHealthResponse,
)
def update_integration_health(
    health_id: int,
    health: IntegrationHealthUpdate,
    db: Session = Depends(get_db),
):
    return update_integration_health_service(
        db,
        health_id,
        health,
    )


# Delete Integration Health
@router.delete(
    "/{health_id}",
)
def delete_integration_health(
    health_id: int,
    db: Session = Depends(get_db),
):
    return delete_integration_health_service(
        db,
        health_id,
    )