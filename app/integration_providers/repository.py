from sqlalchemy import select
from sqlalchemy.orm import Session

from app.integration_providers.models import IntegrationProvider
from app.integration_providers.schemas import (
    IntegrationProviderCreate,
    IntegrationProviderUpdate,
)


class IntegrationProviderRepository:

    @staticmethod
    def create(
        db: Session,
        provider: IntegrationProviderCreate,
    ) -> IntegrationProvider:

        db_provider = IntegrationProvider(
            name=provider.name,
            provider_code=provider.provider_code,
            provider_type=provider.provider_type,
            auth_type=provider.auth_type,
            base_url=provider.base_url,
        )

        db.add(db_provider)
        db.commit()
        db.refresh(db_provider)

        return db_provider

    @staticmethod
    def get_all(db: Session):

        return (
            db.execute(
                select(IntegrationProvider).order_by(IntegrationProvider.id)
            )
            .scalars()
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        provider_id: int,
    ):

        return db.execute(
            select(IntegrationProvider).where(
                IntegrationProvider.id == provider_id
            )
        ).scalar_one_or_none()

    @staticmethod
    def get_by_provider_code(
        db: Session,
        provider_code: str,
    ):

        return db.execute(
            select(IntegrationProvider).where(
                IntegrationProvider.provider_code == provider_code
            )
        ).scalar_one_or_none()

    @staticmethod
    def update(
        db: Session,
        db_provider: IntegrationProvider,
        provider: IntegrationProviderUpdate,
    ):

        update_data = provider.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_provider, key, value)

        db.commit()
        db.refresh(db_provider)

        return db_provider

    @staticmethod
    def disable(
        db: Session,
        db_provider: IntegrationProvider,
    ):

        db_provider.is_active = False

        db.commit()
        db.refresh(db_provider)

        return db_provider

    @staticmethod
    def delete(
        db: Session,
        db_provider: IntegrationProvider,
    ):

        db.delete(db_provider)
        db.commit()

        return True