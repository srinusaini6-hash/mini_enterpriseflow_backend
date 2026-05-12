from pydantic import BaseModel


class CommentCreate(BaseModel):
    task_id: int
    comment_text: str


class ReplyCreate(BaseModel):
    comment_id: int
    reply_text: str