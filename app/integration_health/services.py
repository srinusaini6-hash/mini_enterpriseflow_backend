from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.integration_health.repository import (
    create_integration_health,
    get_all_integration_health,
    get_integration_health_by_id,
    update_integration_health,
    delete_integration_health,
)

from app.integration_health.schemas import (
    IntegrationHealthCreate,
    IntegrationHealthUpdate,
)

from app.tenant_integrations.models import TenantIntegration


def create_integration_health_service(
    db: Session,
    health: IntegrationHealthCreate,
):
    integration = (
        db.query(TenantIntegration)
        .filter(
            TenantIntegration.id == health.integration_id
        )
        .first()
    )

    if not integration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tenant integration not found."
        )

    return create_integration_health(
        db,
        health,
    )


def get_all_integration_health_service(
    db: Session,
):
    return get_all_integration_health(db)


def get_integration_health_service(
    db: Session,
    health_id: int,
):
    health = get_integration_health_by_id(
        db,
        health_id,
    )

    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Integration health record not found."
        )

    return health


def update_integration_health_service(
    db: Session,
    health_id: int,
    health: IntegrationHealthUpdate,
):
    updated_health = update_integration_health(
        db,
        health_id,
        health,
    )

    if not updated_health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Integration health record not found."
        )

    return updated_health


def delete_integration_health_service(
    db: Session,
    health_id: int,
):
    deleted_health = delete_integration_health(
        db,
        health_id,
    )

    if not deleted_health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Integration health record not found."
        )

    return {
        "message": "Integration health record deleted successfully."
    }