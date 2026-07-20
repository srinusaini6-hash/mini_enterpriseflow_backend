from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.tenant_integrations.schemas import (
    TenantIntegrationCreate,
    TenantIntegrationUpdate,
    TenantIntegrationResponse,
)

from app.tenant_integrations.services import (
    TenantIntegrationService,
)

router = APIRouter(
    prefix="/tenant-integrations",
    tags=["Tenant Integrations"],
)


# ---------------------------------------------------------
# Connect Tenant Integration
# ---------------------------------------------------------
@router.post(
    "",
    response_model=TenantIntegrationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_tenant_integration(
    integration: TenantIntegrationCreate,
    db: Session = Depends(get_db),
):
    return TenantIntegrationService.create_integration(
        db,
        integration,
    )


# ---------------------------------------------------------
# List Tenant Integrations
# ---------------------------------------------------------
@router.get(
    "",
    response_model=list[TenantIntegrationResponse],
)
def get_all_tenant_integrations(
    db: Session = Depends(get_db),
):
    return TenantIntegrationService.get_all_integrations(
        db,
    )


# ---------------------------------------------------------
# Get Tenant Integration By ID
# ---------------------------------------------------------
@router.get(
    "/{integration_id}",
    response_model=TenantIntegrationResponse,
)
def get_tenant_integration(
    integration_id: int,
    db: Session = Depends(get_db),
):
    return TenantIntegrationService.get_integration(
        db,
        integration_id,
    )


# ---------------------------------------------------------
# Update Tenant Integration
# ---------------------------------------------------------
@router.put(
    "/{integration_id}",
    response_model=TenantIntegrationResponse,
)
def update_tenant_integration(
    integration_id: int,
    integration: TenantIntegrationUpdate,
    db: Session = Depends(get_db),
):
    return TenantIntegrationService.update_integration(
        db,
        integration_id,
        integration,
    )


# ---------------------------------------------------------
# Disable Tenant Integration
# ---------------------------------------------------------
@router.patch(
    "/{integration_id}/disable",
    response_model=TenantIntegrationResponse,
)
def disable_tenant_integration(
    integration_id: int,
    db: Session = Depends(get_db),
):
    return TenantIntegrationService.disable_integration(
        db,
        integration_id,
    )


# ---------------------------------------------------------
# Delete Tenant Integration
# ---------------------------------------------------------
@router.delete(
    "/{integration_id}",
)
def delete_tenant_integration(
    integration_id: int,
    db: Session = Depends(get_db),
):
    return TenantIntegrationService.delete_integration(
        db,
        integration_id,
    )