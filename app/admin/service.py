from fastapi import HTTPException

from sqlalchemy.orm import Session

from sqlalchemy import (
    select,
    delete
)

from fastapi_pagination.ext.sqlalchemy import paginate

from app.users.models import User

from app.comments.models import (
    Comment,
    CommentReply
)

from app.admin.models import (
    Department,
    AuditLog
)


# ---------------- ADMIN ACCESS ----------------

def admin_only(user: User):

    if user.role != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )


# ---------------- GET ALL USERS ----------------

def get_all_users_service(
    db: Session
):

    users = db.execute(
        select(User)
    ).scalars().all()

    return users


# ---------------- DELETE USER ----------------

def delete_user_service(
    user_id: int,
    db: Session,
    current_user: User
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

def create_department_service(
    department,
    db: Session,
    current_user: User
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

    db.refresh(new_department)

    return new_department


# ---------------- GET AUDIT LOGS ----------------

def get_audit_logs_service(
    db: Session,
    current_user: User
):

    admin_only(current_user)

    query = select(AuditLog)

    return paginate(
        db,
        query
    )
