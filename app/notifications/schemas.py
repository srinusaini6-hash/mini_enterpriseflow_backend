from pydantic import BaseModel


# ---------------- NOTIFICATION RESPONSE ----------------

class NotificationResponse(BaseModel):

    id: int

    message: str

    is_read: bool

    class Config:

        from_attributes = True