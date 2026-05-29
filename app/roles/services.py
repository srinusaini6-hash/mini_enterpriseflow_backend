from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.roles.models import Role


# ---------------- CREATE ROLE ----------------

def create_role_service(
    db: Session,
    data
):

    existing_role = db.execute(
        select(Role).where(
            Role.name == data.name
        )
    ).scalars().first()

    if existing_role:

        return None

    role = Role(
        name=data.name,
        description=data.description
    )

    db.add(role)

    db.commit()

    db.refresh(role)

    return role


# ---------------- GET ALL ROLES ----------------

def get_roles_service(
    db: Session
):

    query = select(Role)

    return paginate(
        db,
        query
    )


# ---------------- GET SINGLE ROLE ----------------

def get_single_role_service(
    db: Session,
    role_id: int
):

    role = db.execute(
        select(Role).where(
            Role.id == role_id
        )
    ).scalars().first()

    return role


# ---------------- UPDATE ROLE ----------------

def update_role_service(
    db: Session,
    role_id: int,
    data
):

    role = db.execute(
        select(Role).where(
            Role.id == role_id
        )
    ).scalars().first()

    if not role:

        return None

    role.name = data.name

    role.description = data.description

    db.commit()

    db.refresh(role)

    return role


# ---------------- DELETE ROLE ----------------

def delete_role_service(
    db: Session,
    role_id: int
):

    role = db.execute(
        select(Role).where(
            Role.id == role_id
        )
    ).scalars().first()

    if not role:

        return False

    db.delete(role)

    db.commit()

    return True