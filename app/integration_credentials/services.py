from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.integration_credentials.repository import (
    IntegrationCredentialRepository,
)

from app.integration_credentials.schemas import (
    IntegrationCredentialCreate,
    IntegrationCredentialUpdate,
)

from app.tenant_integrations.models import TenantIntegration
from app.tenants.models import Tenant


class IntegrationCredentialService:

    @staticmethod
    def create_credential(
        db: Session,
        credential_data: IntegrationCredentialCreate,
    ):

        tenant = (
            db.query(Tenant)
            .filter(Tenant.id == credential_data.tenant_id)
            .first()
        )

        if not tenant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant not found.",
            )

        integration = (
            db.query(TenantIntegration)
            .filter(
                TenantIntegration.id
                == credential_data.integration_id
            )
            .first()
        )

        if not integration:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant integration not found.",
            )

        return IntegrationCredentialRepository.create(
            db,
            credential_data,
        )

    @staticmethod
    def get_all_credentials(
        db: Session,
    ):

        return IntegrationCredentialRepository.get_all(db)

    @staticmethod
    def get_credential(
        db: Session,
        credential_id: int,
    ):

        credential = IntegrationCredentialRepository.get_by_id(
            db,
            credential_id,
        )

        if not credential:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Credential not found.",
            )

        return credential

    @staticmethod
    def update_credential(
        db: Session,
        credential_id: int,
        credential_data: IntegrationCredentialUpdate,
    ):

        credential = IntegrationCredentialRepository.get_by_id(
            db,
            credential_id,
        )

        if not credential:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Credential not found.",
            )

        return IntegrationCredentialRepository.update(
            db,
            credential,
            credential_data,
        )

    @staticmethod
    def delete_credential(
        db: Session,
        credential_id: int,
    ):

        credential = IntegrationCredentialRepository.get_by_id(
            db,
            credential_id,
        )

        if not credential:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Credential not found.",
            )

        IntegrationCredentialRepository.delete(
            db,
            credential,
        )

        return {
            "message": "Integration credential deleted successfully."
        }