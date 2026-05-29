from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.permissions.models import Permission


# ---------------- CREATE PERMISSION ----------------

def create_permission_service(
    db: Session,
    data
):

    existing_permission = db.execute(
        select(Permission).where(
            Permission.name == data.name
        )
    ).scalars().first()

    if existing_permission:

        return None

    permission = Permission(
        name=data.name,
        description=data.description
    )

    db.add(permission)

    db.commit()

    db.refresh(permission)

    return permission


# ---------------- GET ALL PERMISSIONS ----------------

def get_permissions_service(
    db: Session
):

    query = select(Permission)

    return paginate(
        db,
        query
    )


# ---------------- GET SINGLE PERMISSION ----------------

def get_single_permission_service(
    db: Session,
    permission_id: int
):

    permission = db.execute(
        select(Permission).where(
            Permission.id == permission_id
        )
    ).scalars().first()

    return permission


# ---------------- UPDATE PERMISSION ----------------

def update_permission_service(
    db: Session,
    permission_id: int,
    data
):

    permission = db.execute(
        select(Permission).where(
            Permission.id == permission_id
        )
    ).scalars().first()

    if not permission:

        return None

    permission.name = data.name

    permission.description = data.description

    db.commit()

    db.refresh(permission)

    return permission


# ---------------- DELETE PERMISSION ----------------

def delete_permission_service(
    db: Session,
    permission_id: int
):

    permission = db.execute(
        select(Permission).where(
            Permission.id == permission_id
        )
    ).scalars().first()

    if not permission:

        return False

    db.delete(permission)

    db.commit()

    return True