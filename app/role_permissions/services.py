from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.role_permissions.models import RolePermission

from app.roles.models import Role

from app.permissions.models import Permission


# ---------------- ASSIGN PERMISSION ----------------

def assign_permission_service(
    db: Session,
    data
):

    role = db.execute(
        select(Role).where(
            Role.id == data.role_id
        )
    ).scalars().first()

    if not role:

        return "ROLE_NOT_FOUND"

    permission = db.execute(
        select(Permission).where(
            Permission.id == data.permission_id
        )
    ).scalars().first()

    if not permission:

        return "PERMISSION_NOT_FOUND"

    existing = db.execute(
        select(RolePermission).where(
            RolePermission.role_id == data.role_id,
            RolePermission.permission_id == data.permission_id
        )
    ).scalars().first()

    if existing:

        return "ALREADY_ASSIGNED"

    role_permission = RolePermission(
        role_id=data.role_id,
        permission_id=data.permission_id
    )

    db.add(role_permission)

    db.commit()

    db.refresh(role_permission)

    return role_permission


# ---------------- GET ALL ROLE PERMISSIONS ----------------

def get_role_permissions_service(
    db: Session
):

    query = select(RolePermission)

    return paginate(
        db,
        query
    )


# ---------------- DELETE ROLE PERMISSION ----------------

def delete_role_permission_service(
    db: Session,
    role_permission_id: int
):

    role_permission = db.execute(
        select(RolePermission).where(
            RolePermission.id == role_permission_id
        )
    ).scalars().first()

    if not role_permission:

        return False

    db.delete(role_permission)

    db.commit()

    return True