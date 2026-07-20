from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.tenant_integrations.models import TenantIntegration
from app.tenant_integrations.repository import TenantIntegrationRepository
from app.tenant_integrations.schemas import (
    TenantIntegrationCreate,
    TenantIntegrationUpdate,
)


class TenantIntegrationService:

    @staticmethod
    def create_integration(
        db: Session,
        integration_data: TenantIntegrationCreate,
    ) -> TenantIntegration:

        return TenantIntegrationRepository.create(
            db,
            integration_data,
        )

    @staticmethod
    def get_all_integrations(
        db: Session,
    ):

        return TenantIntegrationRepository.get_all(db)

    @staticmethod
    def get_integration(
        db: Session,
        integration_id: int,
    ):

        integration = TenantIntegrationRepository.get_by_id(
            db,
            integration_id,
        )

        if not integration:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant integration not found.",
            )

        return integration

    @staticmethod
    def update_integration(
        db: Session,
        integration_id: int,
        integration_data: TenantIntegrationUpdate,
    ):

        integration = TenantIntegrationRepository.get_by_id(
            db,
            integration_id,
        )

        if not integration:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant integration not found.",
            )

        return TenantIntegrationRepository.update(
            db,
            integration,
            integration_data,
        )

    @staticmethod
    def disable_integration(
        db: Session,
        integration_id: int,
    ):

        integration = TenantIntegrationRepository.get_by_id(
            db,
            integration_id,
        )

        if not integration:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant integration not found.",
            )

        return TenantIntegrationRepository.disable(
            db,
            integration,
        )

    @staticmethod
    def delete_integration(
        db: Session,
        integration_id: int,
    ):

        integration = TenantIntegrationRepository.get_by_id(
            db,
            integration_id,
        )

        if not integration:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant integration not found.",
            )

        TenantIntegrationRepository.delete(
            db,
            integration,
        )

        return {
            "message": "Tenant integration deleted successfully."
        }