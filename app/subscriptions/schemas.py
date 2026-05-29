from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict
)


# ---------------- CREATE PLAN ----------------

class SubscriptionPlanCreate(BaseModel):

    name: str

    monthly_price: float

    yearly_price: float

    max_users: int

    max_projects: int

    max_storage_mb: int

    max_ai_requests: int

    max_workflows: int


# ---------------- RESPONSE PLAN ----------------

class SubscriptionPlanResponse(BaseModel):

    id: int

    name: str

    monthly_price: float

    yearly_price: float

    max_users: int

    max_projects: int

    max_storage_mb: int

    max_ai_requests: int

    max_workflows: int

    is_active: bool

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# ---------------- ASSIGN SUBSCRIPTION ----------------

class SubscriptionAssign(BaseModel):

    plan_id: int

    billing_cycle: str

    end_date: str