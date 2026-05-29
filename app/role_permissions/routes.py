from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.role_permissions.schemas import (
    RolePermissionCreate,
    RolePermissionResponse
)

from app.role_permissions.services import (
    assign_permission_service,
    get_role_permissions_service,
    delete_role_permission_service
)


router = APIRouter(
    prefix="/role-permissions",
    tags=["Role Permissions"]
)


# ---------------- ASSIGN PERMISSION ----------------

@router.post(
    "/",
    response_model=RolePermissionResponse
)
def assign_permission(
    data: RolePermissionCreate,
    db: Session = Depends(get_db)
):

    result = assign_permission_service(
        db=db,
        data=data
    )

    if result == "ROLE_NOT_FOUND":

        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    elif result == "PERMISSION_NOT_FOUND":

        raise HTTPException(
            status_code=404,
            detail="Permission not found"
        )

    elif result == "ALREADY_ASSIGNED":

        raise HTTPException(
            status_code=400,
            detail="Permission already assigned"
        )

    return result


# ---------------- GET ALL ROLE PERMISSIONS ----------------

@router.get(
    "/",
    response_model=Page[RolePermissionResponse]
)
def get_role_permissions(
    db: Session = Depends(get_db)
):

    return get_role_permissions_service(
        db=db
    )


# ---------------- DELETE ROLE PERMISSION ----------------

@router.delete(
    "/{role_permission_id}"
)
def delete_role_permission(
    role_permission_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_role_permission_service(
        db=db,
        role_permission_id=role_permission_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Role permission not found"
        )

    return {
        "message": "Role permission deleted successfully"
    }