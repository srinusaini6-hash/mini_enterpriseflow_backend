from pydantic import BaseModel


class ApprovalCreate(BaseModel):

    request_type: str

    reason: str

    amount: int


class ApprovalAction(BaseModel):

    comment: str
