from pydantic import BaseModel

class SLARuleCreate(BaseModel):
    module_name: str
    priority: str
    allowed_hours: int
    escalation_enabled: bool
    escalation_after_hours: int