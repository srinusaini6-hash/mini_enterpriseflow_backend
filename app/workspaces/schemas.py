from pydantic import BaseModel


class WorkspaceCreate(BaseModel):
    name: str
    slug: str
    description: str
    visibility: str


class WorkspaceUpdate(BaseModel):
    name: str
    description: str
    visibility: str