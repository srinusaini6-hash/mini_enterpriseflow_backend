from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.document_analytics.service import DocumentAnalyticsService

router = APIRouter(
    prefix="/analytics/documents",
    tags=["Document Analytics"],
)


# ---------------------------------------------------------
# Document Summary
# ---------------------------------------------------------
@router.get("")
def get_document_summary(
    db: Session = Depends(get_db),
):
    return DocumentAnalyticsService.get_document_summary(db)


# ---------------------------------------------------------
# Document Downloads
# ---------------------------------------------------------
@router.get("/downloads")
def get_document_downloads(
    db: Session = Depends(get_db),
):
    return DocumentAnalyticsService.get_document_downloads(db)


# ---------------------------------------------------------
# Document Activity
# ---------------------------------------------------------
@router.get("/activity")
def get_document_activity(
    db: Session = Depends(get_db),
):
    return DocumentAnalyticsService.get_document_activity(db)