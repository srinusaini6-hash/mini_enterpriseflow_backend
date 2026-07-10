from io import BytesIO
from typing import List, Dict

from fastapi.responses import StreamingResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
)

from reportlab.lib import colors
from reportlab.lib.units import inch


def export_pdf(
    data: List[Dict],
    filename: str = "report.pdf",
):
    """
    Export report data to PDF.
    """

    output = BytesIO()

    document = SimpleDocTemplate(
        output,
        pagesize=(11 * inch, 8.5 * inch),
    )

    table_data = []

    if data:

        headers = list(data[0].keys())
        table_data.append(headers)

        for row in data:
            table_data.append(
                list(row.values())
            )

    else:

        table_data.append(
            ["No Data Available"]
        )

    table = Table(table_data)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ]
        )
    )

    document.build([table])

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        },
    )