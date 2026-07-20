from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.integration_credentials.schemas import (
    IntegrationCredentialCreate,
    IntegrationCredentialUpdate,
    IntegrationCredentialResponse,
)

from app.integration_credentials.services import (
    IntegrationCredentialService,
)

router = APIRouter(
    prefix="/integration-credentials",
    tags=["Integration Credentials"],
)


# ---------------------------------------------------------
# Create Integration Credential
# ---------------------------------------------------------
@router.post(
    "",
    response_model=IntegrationCredentialResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_credential(
    credential: IntegrationCredentialCreate,
    db: Session = Depends(get_db),
):
    return IntegrationCredentialService.create_credential(
        db,
        credential,
    )


# ---------------------------------------------------------
# Get All Integration Credentials
# ---------------------------------------------------------
@router.get(
    "",
    response_model=list[IntegrationCredentialResponse],
)
def get_all_credentials(
    db: Session = Depends(get_db),
):
    return IntegrationCredentialService.get_all_credentials(db)


# ---------------------------------------------------------
# Get Integration Credential By ID
# ---------------------------------------------------------
@router.get(
    "/{credential_id}",
    response_model=IntegrationCredentialResponse,
)
def get_credential(
    credential_id: int,
    db: Session = Depends(get_db),
):
    return IntegrationCredentialService.get_credential(
        db,
        credential_id,
    )


# ---------------------------------------------------------
# Update Integration Credential
# ---------------------------------------------------------
@router.put(
    "/{credential_id}",
    response_model=IntegrationCredentialResponse,
)
def update_credential(
    credential_id: int,
    credential: IntegrationCredentialUpdate,
    db: Session = Depends(get_db),
):
    return IntegrationCredentialService.update_credential(
        db,
        credential_id,
        credential,
    )


# ---------------------------------------------------------
# Delete Integration Credential
# ---------------------------------------------------------
@router.delete(
    "/{credential_id}",
)
def delete_credential(
    credential_id: int,
    db: Session = Depends(get_db),
):
    return IntegrationCredentialService.delete_credential(
        db,
        credential_id,
    )