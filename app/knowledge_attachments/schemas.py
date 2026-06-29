from datetime import datetime

from pydantic import BaseModel


class KnowledgeAttachmentCreate(BaseModel):
    article_id: int
    file_name: str
    file_path: str


class KnowledgeAttachmentResponse(BaseModel):
    id: int
    article_id: int
    file_name: str
    file_path: str
    uploaded_at: datetime

    model_config = {
        "from_attributes": True
    }