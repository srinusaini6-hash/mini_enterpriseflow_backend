from sqlalchemy.orm import Session

from app.users.models import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token
)


# REGISTER USER
def register_user_service(
    db: Session,
    user
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return None

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


# LOGIN USER
def login_user_service(
    db: Session,
    user
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return "USER_NOT_FOUND"

    if not verify_password(
        user.password,
        existing_user.password
    ):
        return "INVALID_PASSWORD"

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


# REFRESH TOKEN
def refresh_token_service(
    refresh_token: str
):

    payload = decode_token(refresh_token)

    if not payload:
        return None

    new_access_token = create_access_token(
        data={
            "user_id": payload.get("user_id")
        }
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }