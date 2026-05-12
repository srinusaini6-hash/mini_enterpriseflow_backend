import os

from fastapi.responses import FileResponse
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.attachments.models import Attachment
from app.auth.dependencies import get_current_user
from app.users.models import User


router = APIRouter(
    prefix="/attachments",
    tags=["Attachments"]
)


UPLOAD_FOLDER = "uploads"


@router.post("/upload")
async def upload_file(
    task_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    attachment = Attachment(
        task_id=task_id,
        filename=file.filename,
        file_path=file_location,
        file_size=os.path.getsize(file_location),
        mime_type=file.content_type,
        uploaded_by=current_user.id
    )

    db.add(attachment)
    db.commit()

    return {
        "message": "File uploaded successfully"
    }

@router.get("/download/{attachment_id}")
def download_file(
    attachment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    attachment = db.query(Attachment).filter(
        Attachment.id == attachment_id
    ).first()

    if not attachment:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return FileResponse(
        path=attachment.file_path,
        filename=attachment.filename,
        media_type=attachment.mime_type
    )

@router.delete("/{attachment_id}")
def delete_file(
    attachment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    attachment = db.query(Attachment).filter(
        Attachment.id == attachment_id
    ).first()

    if not attachment:
        raise HTTPException(
            status_code=404,
            detail="Attachment not found"
        )

    if os.path.exists(attachment.file_path):
        os.remove(attachment.file_path)

    db.delete(attachment)
    db.commit()

    return {
        "message": "File deleted successfully"
    }