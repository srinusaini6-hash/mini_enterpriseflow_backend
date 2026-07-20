from sqlalchemy.orm import Session

from app.integration_providers.models import IntegrationProvider
from app.integration_providers.repository import (
    IntegrationProviderRepository,
)
from app.integration_providers.schemas import (
    IntegrationProviderCreate,
    IntegrationProviderUpdate,
)


class IntegrationProviderService:

    @staticmethod
    def create_provider(
        db: Session,
        provider: IntegrationProviderCreate,
    ) -> IntegrationProvider:

        existing_provider = (
            IntegrationProviderRepository.get_by_provider_code(
                db,
                provider.provider_code,
            )
        )

        if existing_provider:
            raise ValueError(
                "Integration provider with this provider code already exists."
            )

        return IntegrationProviderRepository.create(
            db,
            provider,
        )

    @staticmethod
    def get_all_providers(
        db: Session,
    ):

        return IntegrationProviderRepository.get_all(db)

    @staticmethod
    def get_provider_by_id(
        db: Session,
        provider_id: int,
    ) -> IntegrationProvider:

        provider = IntegrationProviderRepository.get_by_id(
            db,
            provider_id,
        )

        if not provider:
            raise ValueError("Integration provider not found.")

        return provider

    @staticmethod
    def update_provider(
        db: Session,
        provider_id: int,
        provider_data: IntegrationProviderUpdate,
    ) -> IntegrationProvider:

        provider = IntegrationProviderRepository.get_by_id(
            db,
            provider_id,
        )

        if not provider:
            raise ValueError("Integration provider not found.")

        if (
            provider_data.provider_code
            and provider_data.provider_code != provider.provider_code
        ):
            existing_provider = (
                IntegrationProviderRepository.get_by_provider_code(
                    db,
                    provider_data.provider_code,
                )
            )

            if existing_provider:
                raise ValueError(
                    "Provider code already exists."
                )

        return IntegrationProviderRepository.update(
            db,
            provider,
            provider_data,
        )

    @staticmethod
    def disable_provider(
        db: Session,
        provider_id: int,
    ) -> IntegrationProvider:

        provider = IntegrationProviderRepository.get_by_id(
            db,
            provider_id,
        )

        if not provider:
            raise ValueError("Integration provider not found.")

        return IntegrationProviderRepository.disable(
            db,
            provider,
        )

    @staticmethod
    def delete_provider(
        db: Session,
        provider_id: int,
    ):

        provider = IntegrationProviderRepository.get_by_id(
            db,
            provider_id,
        )

        if not provider:
            raise ValueError("Integration provider not found.")

        IntegrationProviderRepository.delete(
            db,
            provider,
        )

        return {
            "success": True,
            "message": "Integration provider deleted successfully."
        }