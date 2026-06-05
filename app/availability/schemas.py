from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class AvailabilityCheckRequest(BaseModel):
    user_ids: list[int] = Field(..., min_length=1)
    start_time: datetime
    end_time: datetime

    @model_validator(mode="after")
    def validate_times(self):
        if self.end_time <= self.start_time:
            raise ValueError(
                "end_time must be greater than start_time"
            )
        return self