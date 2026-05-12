import os

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.documents.models import Document

from app.auth.dependencies import get_current_user

from app.users.models import User


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    document = Document(
        file_name=file.filename,
        file_path=file_location,
        uploaded_by=current_user.id
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    return {
        "message": "File uploaded successfully",
        "file_id": document.id
    }


@router.get("/download/{document_id}")
def download_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return FileResponse(
        path=document.file_path,
        filename=document.file_name
    )


@router.get("/")
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    documents = db.query(Document).all()

    return documents
