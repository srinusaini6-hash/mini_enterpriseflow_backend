from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.users.models import User

from app.auth.dependencies import get_current_user

from app.admin.models import (
    Department,
    AuditLog
)

from app.admin.schemas import (
    DepartmentCreate
)


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


def admin_only(user):

    if user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )


@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    users = db.query(User).all()

    return users


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)

    log = AuditLog(
        action=f"Deleted user {user.email}",
        performed_by=current_user.id
    )

    db.add(log)

    db.commit()

    return {
        "message": "User deleted successfully"
    }


@router.post("/departments")
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    new_department = Department(
        name=department.name
    )

    db.add(new_department)

    log = AuditLog(
        action=f"Created department {department.name}",
        performed_by=current_user.id
    )

    db.add(log)

    db.commit()

    return {
        "message": "Department created"
    }


@router.get("/audit-logs")
def get_audit_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    logs = db.query(AuditLog).all()

    return logs
