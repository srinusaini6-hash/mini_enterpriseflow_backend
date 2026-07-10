from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, Query

from app.database.database import get_db
from app.auth.dependencies import get_current_user

from app.tasks.models import Task

from app.report_exports.csv_export import export_csv
from app.report_exports.excel_export import export_excel
from app.report_exports.pdf_export import export_pdf


router = APIRouter(
    prefix="/reports/export",
    tags=["Report Exports"],
)


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def get_report_data(
    db: Session,
    report_type: str,
):
    """
    Fetch report data based on report type.
    """

    if report_type == "tasks":

        tasks = db.execute(
            select(Task)
        ).scalars().all()

        return [
            {
                "id": task.id,
                "title": task.title,
                "status": task.status,
                "priority": task.priority,
                "assigned_to": task.assigned_to,
                "created_by": task.created_by,
            }
            for task in tasks
        ]

    return []


# ---------------------------------------------------------
# Export CSV
# ---------------------------------------------------------

@router.get("/csv")
def export_csv_report(
    report_type: str = Query(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    data = get_report_data(db, report_type)

    return export_csv(
        data,
        filename=f"{report_type}_report.csv",
    )


# ---------------------------------------------------------
# Export Excel
# ---------------------------------------------------------

@router.get("/excel")
def export_excel_report(
    report_type: str = Query(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    data = get_report_data(db, report_type)

    return export_excel(
        data,
        filename=f"{report_type}_report.xlsx",
    )


# ---------------------------------------------------------
# Export PDF
# ---------------------------------------------------------

@router.get("/pdf")
def export_pdf_report(
    report_type: str = Query(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    data = get_report_data(db, report_type)

    return export_pdf(
        data,
        filename=f"{report_type}_report.pdf",
    )