from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.dependencies import get_current_user

from app.users.models import User


router = APIRouter(
    prefix="/background",
    tags=["Background Tasks"]
)


# ---------------- SEND EMAIL FUNCTION ----------------
def send_email_background(
    email: str,
    subject: str,
    message: str
):

    print("Sending email...")
    print(f"To: {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")

    import time
    time.sleep(5)

    print("Email sent successfully")


# ---------------- BACKGROUND EMAIL API ----------------
@router.post("/send-email")
def send_email(
    email: str,
    subject: str,
    message: str,
    background_tasks: BackgroundTasks,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)
):

    background_tasks.add_task(
        send_email_background,
        email,
        subject,
        message
    )

    return {
        "message": "Email is being sent in background"
    }