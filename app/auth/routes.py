from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.users.models import User

from app.auth.dependencies import (
    get_current_user
)

from app.auth.schemas import (
    RegisterSchema,
    LoginSchema
)

from app.auth.services import (
    register_user_service,
    login_user_service,
    refresh_token_service
)

from app.middleware.rate_limit import (
    limiter
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# REGISTER
@router.post("/register")
def register(
    user: RegisterSchema,
    db: Session = Depends(get_db)
):

    new_user = register_user_service(
        db,
        user
    )

    if not new_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User registered successfully"
    }


# LOGIN
@router.post("/login")
@limiter.limit("5/minute")
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user_data = LoginSchema(
        email=form_data.username,
        password=form_data.password
    )

    result = login_user_service(
        db,
        user_data
    )

    if result == "USER_NOT_FOUND":
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if result == "INVALID_PASSWORD":
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    return result

# REFRESH TOKEN
@router.post("/refresh")
def refresh_token_api(
    refresh_token: str
):

    result = refresh_token_service(
        refresh_token
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    return result


# GET PROFILE
@router.get("/me")
def get_profile(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    }

    