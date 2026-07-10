from io import BytesIO
from typing import List, Dict

from fastapi.responses import StreamingResponse
from openpyxl import Workbook


def export_excel(
    data: List[Dict],
    filename: str = "report.xlsx"
):
    """
    Export report data to Excel (.xlsx)
    """

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Report"

    if data:

        # Header Row
        worksheet.append(list(data[0].keys()))

        # Data Rows
        for row in data:
            worksheet.append(list(row.values()))

    else:

        worksheet.append(["No Data Available"])

    output = BytesIO()

    workbook.save(output)

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        },
    )