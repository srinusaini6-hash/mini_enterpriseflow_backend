from pydantic import BaseModel
from typing import List


class DocumentSummary(BaseModel):
    total_documents: int
    total_downloads: int
    total_storage_mb: float


class DocumentDownload(BaseModel):
    document_id: int
    file_name: str
    download_count: int


class DocumentActivity(BaseModel):
    document_id: int
    file_name: str
    uploaded_by: int
    download_count: int


class DocumentSummaryResponse(BaseModel):
    success: bool = True
    message: str
    data: DocumentSummary


class DocumentDownloadsResponse(BaseModel):
    success: bool = True
    message: str
    data: List[DocumentDownload]


class DocumentActivityResponse(BaseModel):
    success: bool = True
    message: str
    data: List[DocumentActivity]