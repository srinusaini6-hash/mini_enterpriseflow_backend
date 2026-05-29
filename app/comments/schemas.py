from pydantic import BaseModel


# ---------------- CREATE COMMENT ----------------

class CommentCreate(BaseModel):

    task_id: int

    comment_text: str


# ---------------- REPLY COMMENT ----------------

class ReplyCreate(BaseModel):

    comment_id: int

    reply_text: str


# ---------------- COMMENT RESPONSE ----------------

class CommentResponse(BaseModel):

    id: int

    task_id: int

    user_id: int

    comment_text: str

    class Config:

        from_attributes = True