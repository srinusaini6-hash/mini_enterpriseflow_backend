from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.integration_providers.schemas import (
    IntegrationProviderCreate,
    IntegrationProviderUpdate,
    IntegrationProviderResponse,
    IntegrationProviderMessage,
)

from app.integration_providers.services import (
    IntegrationProviderService,
)

router = APIRouter(
    prefix="/integrations/providers",
    tags=["Integration Providers"],
)


# ---------------------------------------------------------
# Create Integration Provider
# ---------------------------------------------------------
@router.post(
    "",
    response_model=IntegrationProviderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_provider(
    provider: IntegrationProviderCreate,
    db: Session = Depends(get_db),
):
    try:
        return IntegrationProviderService.create_provider(
            db,
            provider,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ---------------------------------------------------------
# List Integration Providers
# ---------------------------------------------------------
@router.get(
    "",
    response_model=list[IntegrationProviderResponse],
)
def get_all_providers(
    db: Session = Depends(get_db),
):
    return IntegrationProviderService.get_all_providers(db)


# ---------------------------------------------------------
# Get Provider By ID
# ---------------------------------------------------------
@router.get(
    "/{provider_id}",
    response_model=IntegrationProviderResponse,
)
def get_provider(
    provider_id: int,
    db: Session = Depends(get_db),
):
    try:
        return IntegrationProviderService.get_provider_by_id(
            db,
            provider_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# ---------------------------------------------------------
# Update Provider
# ---------------------------------------------------------
@router.put(
    "/{provider_id}",
    response_model=IntegrationProviderResponse,
)
def update_provider(
    provider_id: int,
    provider: IntegrationProviderUpdate,
    db: Session = Depends(get_db),
):
    try:
        return IntegrationProviderService.update_provider(
            db,
            provider_id,
            provider,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ---------------------------------------------------------
# Disable Provider
# ---------------------------------------------------------
@router.patch(
    "/{provider_id}/disable",
    response_model=IntegrationProviderMessage,
)
def disable_provider(
    provider_id: int,
    db: Session = Depends(get_db),
):
    try:
        IntegrationProviderService.disable_provider(
            db,
            provider_id,
        )

        return IntegrationProviderMessage(
            success=True,
            message="Integration provider disabled successfully.",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# ---------------------------------------------------------
# Delete Provider
# ---------------------------------------------------------
@router.delete(
    "/{provider_id}",
    response_model=IntegrationProviderMessage,
)
def delete_provider(
    provider_id: int,
    db: Session = Depends(get_db),
):
    try:
        IntegrationProviderService.delete_provider(
            db,
            provider_id,
        )

        return IntegrationProviderMessage(
            success=True,
            message="Integration provider deleted successfully.",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )