from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.tenants.schemas import (
    TenantCreate,
    TenantResponse
)

from app.tenants.services import (
    create_tenant_service,
    get_tenants_service,
    get_single_tenant_service,
    update_tenant_service,
    delete_tenant_service,
    get_tenant_users_service
)


router = APIRouter(
    prefix="/tenants",
    tags=["Tenants"]
)


# ---------------- CREATE TENANT ----------------

@router.post(
    "/",
    response_model=TenantResponse
)
def create_tenant(
    data: TenantCreate,
    db: Session = Depends(get_db)
):

    tenant = create_tenant_service(
        db,
        data
    )

    if not tenant:

        raise HTTPException(
            status_code=400,
            detail="Tenant slug already exists"
        )

    return tenant


# ---------------- GET TENANTS ----------------

@router.get(
    "/",
    response_model=Page[TenantResponse]
)
def get_tenants(
    industry: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):

    return get_tenants_service(
        db,
        industry,
        status
    )


# ---------------- GET SINGLE TENANT ----------------

@router.get(
    "/{tenant_id}",
    response_model=TenantResponse
)
def get_single_tenant(
    tenant_id: int,
    db: Session = Depends(get_db)
):

    tenant = get_single_tenant_service(
        db,
        tenant_id
    )

    if not tenant:

        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    return tenant


# ---------------- UPDATE TENANT ----------------

@router.put(
    "/{tenant_id}",
    response_model=TenantResponse
)
def update_tenant(
    tenant_id: int,
    data: TenantCreate,
    db: Session = Depends(get_db)
):

    tenant = update_tenant_service(
        db,
        tenant_id,
        data
    )

    if not tenant:

        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    return tenant


# ---------------- DELETE TENANT ----------------

@router.delete("/{tenant_id}")
def delete_tenant(
    tenant_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_tenant_service(
        db,
        tenant_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    return {
        "message": "Tenant deleted successfully"
    }


# ---------------- GET TENANT USERS ----------------

@router.get("/{tenant_id}/users")
def get_tenant_users(
    tenant_id: int,
    db: Session = Depends(get_db)
):

    result = get_tenant_users_service(
        db,
        tenant_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    return result