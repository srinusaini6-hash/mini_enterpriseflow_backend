from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.roles.schemas import (
    RoleCreate,
    RoleResponse
)

from app.roles.services import (
    create_role_service,
    get_roles_service,
    get_single_role_service,
    update_role_service,
    delete_role_service
)


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


# ---------------- CREATE ROLE ----------------

@router.post(
    "/",
    response_model=RoleResponse
)
def create_role(
    data: RoleCreate,
    db: Session = Depends(get_db)
):

    role = create_role_service(
        db,
        data
    )

    if not role:

        raise HTTPException(
            status_code=400,
            detail="Role already exists"
        )

    return role


# ---------------- GET ALL ROLES ----------------

@router.get(
    "/",
    response_model=Page[RoleResponse]
)
def get_roles(
    db: Session = Depends(get_db)
):

    return get_roles_service(
        db
    )


# ---------------- GET SINGLE ROLE ----------------

@router.get(
    "/{role_id}",
    response_model=RoleResponse
)
def get_single_role(
    role_id: int,
    db: Session = Depends(get_db)
):

    role = get_single_role_service(
        db,
        role_id
    )

    if not role:

        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


# ---------------- UPDATE ROLE ----------------

@router.put(
    "/{role_id}",
    response_model=RoleResponse
)
def update_role(
    role_id: int,
    data: RoleCreate,
    db: Session = Depends(get_db)
):

    role = update_role_service(
        db,
        role_id,
        data
    )

    if not role:

        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


# ---------------- DELETE ROLE ----------------

@router.delete(
    "/{role_id}"
)
def delete_role(
    role_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_role_service(
        db,
        role_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return {
        "message": "Role deleted successfully"
    }