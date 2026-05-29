from fastapi import HTTPException

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from fastapi_pagination import paginate

from app.users.models import User
from app.users.schemas import UserCreate

from app.tenants.models import Tenant


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ---------------- CREATE USER ----------------

def create_user_service(
    db: Session,
    data: UserCreate
):

    existing_user = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    tenant = db.query(Tenant).filter(
        Tenant.id == data.tenant_id
    ).first()

    if not tenant:
        raise HTTPException(
            status_code=404,
            detail="Tenant not found"
        )

    hashed_password = pwd_context.hash(
        data.password
    )

    user = User(
        name=data.name,
        email=data.email,
        password=hashed_password,
        role=data.role,
        tenant_id=data.tenant_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# ---------------- GET USERS ----------------

def get_users_service(
    db: Session
):

    users = db.query(User).all()

    return paginate(users)


# ---------------- GET SINGLE USER ----------------

def get_user_by_id_service(
    db: Session,
    user_id: int
):

    return db.query(User).filter(
        User.id == user_id
    ).first()


# ---------------- DELETE USER ----------------

def delete_user_service(
    db: Session,
    user_id: int
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return False

    db.delete(user)
    db.commit()

    return True