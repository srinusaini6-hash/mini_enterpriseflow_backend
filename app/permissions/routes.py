from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.permissions.schemas import (
    PermissionCreate,
    PermissionResponse
)

from app.permissions.services import (
    create_permission_service,
    get_permissions_service,
    get_single_permission_service,
    update_permission_service,
    delete_permission_service
)


router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"]
)


# ---------------- CREATE PERMISSION ----------------

@router.post(
    "/",
    response_model=PermissionResponse
)
def create_permission(
    data: PermissionCreate,
    db: Session = Depends(get_db)
):

    permission = create_permission_service(
        db,
        data
    )

    if not permission:

        raise HTTPException(
            status_code=400,
            detail="Permission already exists"
        )

    return permission


# ---------------- GET ALL PERMISSIONS ----------------

@router.get(
    "/",
    response_model=Page[PermissionResponse]
)
def get_permissions(
    db: Session = Depends(get_db)
):

    return get_permissions_service(
        db
    )


# ---------------- GET SINGLE PERMISSION ----------------

@router.get(
    "/{permission_id}",
    response_model=PermissionResponse
)
def get_single_permission(
    permission_id: int,
    db: Session = Depends(get_db)
):

    permission = get_single_permission_service(
        db,
        permission_id
    )

    if not permission:

        raise HTTPException(
            status_code=404,
            detail="Permission not found"
        )

    return permission


# ---------------- UPDATE PERMISSION ----------------

@router.put(
    "/{permission_id}",
    response_model=PermissionResponse
)
def update_permission(
    permission_id: int,
    data: PermissionCreate,
    db: Session = Depends(get_db)
):

    permission = update_permission_service(
        db,
        permission_id,
        data
    )

    if not permission:

        raise HTTPException(
            status_code=404,
            detail="Permission not found"
        )

    return permission


# ---------------- DELETE PERMISSION ----------------

@router.delete(
    "/{permission_id}"
)
def delete_permission(
    permission_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_permission_service(
        db,
        permission_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Permission not found"
        )

    return {
        "message": "Permission deleted successfully"
    }