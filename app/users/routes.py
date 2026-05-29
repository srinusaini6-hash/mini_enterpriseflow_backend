from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from fastapi_pagination import Page

from app.database.database import get_db

from app.users.schemas import (
    UserCreate,
    UserResponse
)

from app.users.services import (
    create_user_service,
    get_users_service,
    get_user_by_id_service,
    delete_user_service
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ---------------- CREATE USER ----------------

@router.post(
    "/",
    response_model=UserResponse
)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user_service(
        db,
        data
    )


# ---------------- GET USERS ----------------

@router.get(
    "/",
    response_model=Page[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):

    return get_users_service(
        db
    )


# ---------------- GET SINGLE USER ----------------

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id_service(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# ---------------- DELETE USER ----------------

@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_user_service(
        db,
        user_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }