from pydantic import BaseModel
from typing import List


# ---------------------------------------------------------
# Productivity Summary
# ---------------------------------------------------------
class ProductivitySummary(BaseModel):
    total_tasks: int
    completed_tasks: int
    pending_tasks: int
    overdue_tasks: int
    average_completion_rate: float

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# User Productivity
# ---------------------------------------------------------
class UserProductivity(BaseModel):
    user_id: int
    user_name: str
    total_tasks: int
    completed_tasks: int
    pending_tasks: int
    overdue_tasks: int
    completion_rate: float

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# Department Productivity
# ---------------------------------------------------------
class DepartmentProductivity(BaseModel):
    department: str
    total_tasks: int
    completed_tasks: int
    completion_rate: float

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# Team Productivity
# ---------------------------------------------------------
class TeamProductivity(BaseModel):
    team_name: str
    total_tasks: int
    completed_tasks: int
    completion_rate: float

    class Config:
        from_attributes = True


# ---------------------------------------------------------
# Overall Productivity Report
# ---------------------------------------------------------
class ProductivityReportResponse(BaseModel):
    summary: ProductivitySummary
    users: List[UserProductivity]

    class Config:
        from_attributes = True