from pydantic import BaseModel, Field


# ---------------- CREATE APPROVAL ----------------

class ApprovalCreate(BaseModel):

    request_type: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    reason: str = Field(
        ...,
        min_length=5,
        max_length=500
    )

    amount: int = Field(
        ...,
        gt=0
    )


# ---------------- APPROVAL ACTION ----------------

class ApprovalAction(BaseModel):

    comment: str = Field(
        ...,
        min_length=3,
        max_length=300
    )


# ---------------- APPROVAL RESPONSE ----------------

class ApprovalResponse(BaseModel):

    id: int
    request_type: str
    reason: str
    amount: int
    status: str
    submitted_by: int

    class Config:

        from_attributes = True