from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.users.models import User
from app.auth.dependencies import get_current_user

from app.auth.schemas import (
    RegisterSchema,
    LoginSchema
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token
)

from app.middleware.rate_limit import limiter


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ------------------- REGISTER -------------------

@router.post("/register")
def register(
    user: RegisterSchema,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# ------------------- LOGIN -------------------

@router.post("/login")
@limiter.limit("5/minute")
def login(
    request: Request,
    user: LoginSchema,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        user.password,
        existing_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={
            "user_id": existing_user.id,
            "role": existing_user.role
        }
    )

    refresh_token = create_refresh_token(
        data={
            "user_id": existing_user.id
        }
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# ------------------- REFRESH TOKEN -------------------

@router.post("/refresh")
def refresh_token_api(
    refresh_token: str
):

    try:

        payload = decode_token(refresh_token)

        if not payload:

            raise HTTPException(
                status_code=401,
                detail="Invalid refresh token"
            )

        new_access_token = create_access_token(
            data={
                "user_id": payload.get("user_id")
            }
        )

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )


# ------------------- GET PROFILE -------------------

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