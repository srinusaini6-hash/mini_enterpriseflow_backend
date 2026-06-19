from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    name: str
    count: int