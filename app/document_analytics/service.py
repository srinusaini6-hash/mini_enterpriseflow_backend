from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.knowledge_attachments.models import KnowledgeAttachment


class DocumentAnalyticsService:

    @staticmethod
    def get_document_summary(db: Session):

        total_documents = db.scalar(
            select(func.count(KnowledgeAttachment.id))
        ) or 0

        return {
            "success": True,
            "message": "Document summary fetched successfully",
            "data": {
                "total_documents": total_documents,
                "total_downloads": 0,
                "total_storage_mb": 0
            }
        }

    @staticmethod
    def get_document_downloads(db: Session):

        attachments = db.execute(
            select(KnowledgeAttachment)
        ).scalars().all()

        data = []

        for attachment in attachments:
            data.append(
                {
                    "document_id": attachment.id,
                    "file_name": attachment.file_name,
                    "download_count": 0
                }
            )

        return {
            "success": True,
            "message": "Document downloads fetched successfully",
            "data": data
        }

    @staticmethod
    def get_document_activity(db: Session):

        attachments = db.execute(
            select(KnowledgeAttachment)
        ).scalars().all()

        data = []

        for attachment in attachments:
            data.append(
                {
                    "document_id": attachment.id,
                    "file_name": attachment.file_name,
                    "uploaded_by": attachment.article_id,
                    "download_count": 0
                }
            )

        return {
            "success": True,
            "message": "Document activity fetched successfully",
            "data": data
        }
