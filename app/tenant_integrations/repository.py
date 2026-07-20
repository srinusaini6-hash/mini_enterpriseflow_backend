from sqlalchemy.orm import Session

from app.tenant_integrations.models import TenantIntegration
from app.tenant_integrations.schemas import (
    TenantIntegrationCreate,
    TenantIntegrationUpdate,
)


class TenantIntegrationRepository:

    @staticmethod
    def create(
        db: Session,
        integration: TenantIntegrationCreate,
    ) -> TenantIntegration:

        db_integration = TenantIntegration(
            tenant_id=integration.tenant_id,
            provider_id=integration.provider_id,
            integration_name=integration.integration_name,
            status=integration.status,
            config_json=integration.config_json,
            connected_by=integration.connected_by,
        )

        db.add(db_integration)
        db.commit()
        db.refresh(db_integration)

        return db_integration

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(TenantIntegration)
            .order_by(TenantIntegration.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        integration_id: int,
    ):
        return (
            db.query(TenantIntegration)
            .filter(TenantIntegration.id == integration_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        integration: TenantIntegration,
        integration_data: TenantIntegrationUpdate,
    ):

        update_data = integration_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(integration, key, value)

        db.commit()
        db.refresh(integration)

        return integration

    @staticmethod
    def disable(
        db: Session,
        integration: TenantIntegration,
    ):

        integration.status = "DISABLED"

        db.commit()
        db.refresh(integration)

        return integration

    @staticmethod
    def delete(
        db: Session,
        integration: TenantIntegration,
    ):

        db.delete(integration)
        db.commit()