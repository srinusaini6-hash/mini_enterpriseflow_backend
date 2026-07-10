from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.dependencies import get_current_user

from app.productivity_reports.service import ProductivityReportService
from app.productivity_reports.schemas import (
    ProductivityReportResponse,
    UserProductivity,
    DepartmentProductivity,
)

router = APIRouter(
    prefix="/reports/productivity",
    tags=["Productivity Reports"],
)


# ---------------------------------------------------------
# Overall Productivity Report
# ---------------------------------------------------------
@router.get(
    "",
    response_model=ProductivityReportResponse,
    summary="Overall Productivity Report",
)
def overall_productivity_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = ProductivityReportService(db)
    return service.overall_report()


# ---------------------------------------------------------
# User Productivity Report
# ---------------------------------------------------------
@router.get(
    "/users",
    response_model=list[UserProductivity],
    summary="User Productivity Report",
)
def user_productivity_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = ProductivityReportService(db)
    return service.user_productivity()


# ---------------------------------------------------------
# Department Productivity Report
# ---------------------------------------------------------
@router.get(
    "/departments",
    response_model=list[DepartmentProductivity],
    summary="Department Productivity Report",
)
def department_productivity_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = ProductivityReportService(db)
    return service.department_productivity()


# ---------------------------------------------------------
# Team Productivity Report
# ---------------------------------------------------------
@router.get(
    "/teams",
    response_model=list[DepartmentProductivity],
    summary="Team Productivity Report",
)
def team_productivity_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = ProductivityReportService(db)
    return service.team_productivity()