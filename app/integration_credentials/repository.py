from sqlalchemy.orm import Session

from app.integration_credentials.models import IntegrationCredential
from app.integration_credentials.schemas import (
    IntegrationCredentialCreate,
    IntegrationCredentialUpdate,
)


class IntegrationCredentialRepository:

    @staticmethod
    def create(
        db: Session,
        credential_data: IntegrationCredentialCreate,
    ) -> IntegrationCredential:

        credential = IntegrationCredential(
            **credential_data.model_dump()
        )

        db.add(credential)
        db.commit()
        db.refresh(credential)

        return credential

    @staticmethod
    def get_all(
        db: Session,
    ):

        return (
            db.query(IntegrationCredential)
            .order_by(IntegrationCredential.id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        credential_id: int,
    ):

        return (
            db.query(IntegrationCredential)
            .filter(
                IntegrationCredential.id == credential_id
            )
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        credential: IntegrationCredential,
        credential_data: IntegrationCredentialUpdate,
    ) -> IntegrationCredential:

        update_data = credential_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(credential, key, value)

        db.commit()
        db.refresh(credential)

        return credential

    @staticmethod
    def delete(
        db: Session,
        credential: IntegrationCredential,
    ):

        db.delete(credential)
        db.commit()