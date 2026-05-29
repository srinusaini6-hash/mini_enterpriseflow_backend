from pydantic import BaseModel

from datetime import datetime


class TenantSubscriptionCreate(BaseModel):

    tenant_id: int

    plan_id: int

    billing_cycle: str

    end_date: datetime


class TenantSubscriptionResponse(BaseModel):

    id: int

    tenant_id: int

    plan_id: int

    billing_cycle: str

    status: str

    auto_renew: bool

    start_date: datetime

    end_date: datetime

    class Config:

        from_attributes = True