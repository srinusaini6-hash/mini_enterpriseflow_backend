from typing import Optional

from sqlalchemy.orm import Session

from sqlalchemy import select

from fastapi_pagination.ext.sqlalchemy import paginate

from app.tenants.models import Tenant

from app.users.models import User


# ---------------- CREATE TENANT ----------------

def create_tenant_service(
    db: Session,
    data
):

    existing = db.execute(
        select(Tenant).where(
            Tenant.slug == data.slug
        )
    ).scalars().first()

    if existing:

        return None

    tenant = Tenant(
        name=data.name,
        slug=data.slug,
        contact_email=data.contact_email,
        phone=data.phone,
        address=data.address,
        industry=data.industry
    )

    db.add(tenant)

    db.commit()

    db.refresh(tenant)

    return tenant


# ---------------- GET ALL TENANTS ----------------

def get_tenants_service(
    db: Session,
    industry: Optional[str] = None,
    status: Optional[str] = None
):

    query = select(Tenant)

    if industry:

        query = query.where(
            Tenant.industry == industry
        )

    if status:

        query = query.where(
            Tenant.status == status
        )

    return paginate(
        db,
        query
    )


# ---------------- GET SINGLE TENANT ----------------

def get_single_tenant_service(
    db: Session,
    tenant_id: int
):

    tenant = db.execute(
        select(Tenant).where(
            Tenant.id == tenant_id
        )
    ).scalars().first()

    return tenant


# ---------------- UPDATE TENANT ----------------

def update_tenant_service(
    db: Session,
    tenant_id: int,
    data
):

    tenant = db.execute(
        select(Tenant).where(
            Tenant.id == tenant_id
        )
    ).scalars().first()

    if not tenant:

        return None

    tenant.name = data.name
    tenant.slug = data.slug
    tenant.contact_email = data.contact_email
    tenant.phone = data.phone
    tenant.address = data.address
    tenant.industry = data.industry

    db.commit()

    db.refresh(tenant)

    return tenant


# ---------------- DELETE TENANT ----------------

def delete_tenant_service(
    db: Session,
    tenant_id: int
):

    tenant = db.execute(
        select(Tenant).where(
            Tenant.id == tenant_id
        )
    ).scalars().first()

    if not tenant:

        return False

    db.delete(tenant)

    db.commit()

    return True


# ---------------- GET TENANT USERS ----------------

def get_tenant_users_service(
    db: Session,
    tenant_id: int
):

    tenant = db.execute(
        select(Tenant).where(
            Tenant.id == tenant_id
        )
    ).scalars().first()

    if not tenant:

        return None

    users = db.execute(
        select(User).where(
            User.tenant_id == tenant_id
        )
    ).scalars().all()

    user_data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "tenant_id": user.tenant_id
        }
        for user in users
    ]

    return {
        "tenant": tenant.name,
        "users": user_data
    }