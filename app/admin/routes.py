from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from sqlalchemy import (
    select,
    delete
)

from app.database.database import get_db

from app.users.models import User

from app.auth.dependencies import get_current_user

from app.admin.models import (
    Department,
    AuditLog
)

from app.comments.models import (
    Comment,
    CommentReply
)

from app.admin.schemas import (
    DepartmentCreate,
    UserResponse
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# ---------------- ADMIN ACCESS ----------------

def admin_only(user: User):

    if user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )


# ---------------- GET ALL USERS ----------------

@router.get(
    "/users",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    users = db.execute(
        select(User)
    ).scalars().all()

    return users


# ---------------- DELETE USER ----------------

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    user = db.execute(
        select(User).where(
            User.id == user_id
        )
    ).scalars().first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # DELETE USER COMMENT REPLIES
    db.execute(
        delete(CommentReply).where(
            CommentReply.user_id == user_id
        )
    )

    # DELETE USER COMMENTS
    db.execute(
        delete(Comment).where(
            Comment.user_id == user_id
        )
    )

    # CREATE AUDIT LOG
    log = AuditLog(
        module_name="USER",
        action_type="DELETE",
        record_id=user.id,
        old_data=user.email
    )

    db.add(log)

    # DELETE USER
    db.delete(user)

    db.commit()

    return {
        "message": "User deleted successfully"
    }


# ---------------- CREATE DEPARTMENT ----------------

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

    # CREATE AUDIT LOG
    log = AuditLog(
        module_name="DEPARTMENT",
        action_type="CREATE",
        new_data=department.name
    )

    db.add(log)

    db.commit()

    return {
        "message": "Department created successfully"
    }


# ---------------- GET AUDIT LOGS ----------------

@router.get("/audit-logs")
def get_audit_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    admin_only(current_user)

    logs = db.execute(
        select(AuditLog)
    ).scalars().all()

    return logs