import csv
from io import StringIO
from typing import List, Dict

from fastapi.responses import StreamingResponse


def export_csv(
    data: List[Dict],
    filename: str = "report.csv"
):
    """
    Export report data as CSV.
    """

    output = StringIO()

    if data:

        writer = csv.DictWriter(
            output,
            fieldnames=data[0].keys()
        )

        writer.writeheader()

        writer.writerows(data)

    else:

        writer = csv.writer(output)
        writer.writerow(["No Data Available"])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )