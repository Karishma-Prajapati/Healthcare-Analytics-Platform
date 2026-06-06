from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    filename,
    name,
    age,
    disease,
    risk
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Healthcare Risk Assessment Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Patient Name: {name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Age: {age}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Disease Checked: {disease}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Percentage: {risk*100:.2f}%",
            styles["Normal"]
        )
    )

    if risk > 0.5:

        status = "HIGH RISK"

    else:

        status = "LOW RISK"

    content.append(
        Paragraph(
            f"Status: {status}",
            styles["Normal"]
        )
    )

    doc.build(content)

    return filename