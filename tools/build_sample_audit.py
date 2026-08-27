from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "bay-state-auto-growth-sample-shop-audit.pdf"
BEFORE_SCREENSHOT = ROOT / "output" / "playwright" / "audit-package" / "before-desktop.png"
AFTER_SCREENSHOT = ROOT / "output" / "playwright" / "audit-package" / "after-desktop.png"

CHARCOAL = colors.HexColor("#171815")
INK = colors.HexColor("#272823")
WARM_WHITE = colors.HexColor("#F6F1E7")
PAPER = colors.HexColor("#FFFDF8")
ORANGE = colors.HexColor("#F15A24")
MUTED = colors.HexColor("#6B6B63")
LINE = colors.HexColor("#DDD5C8")
PALE_ORANGE = colors.HexColor("#FFF0E7")


class NumberBadge(Flowable):
    def __init__(self, number: str, size: float = 22):
        super().__init__()
        self.number = number
        self.width = size
        self.height = size
        self.size = size

    def draw(self):
        self.canv.setFillColor(ORANGE)
        self.canv.roundRect(0, 0, self.size, self.size, 5, fill=1, stroke=0)
        self.canv.setFillColor(colors.white)
        self.canv.setFont("Helvetica-Bold", 9)
        text_width = stringWidth(self.number, "Helvetica-Bold", 9)
        self.canv.drawString((self.size - text_width) / 2, 7, self.number)


def page_background(canvas, doc):
    width, height = letter
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, height - 1.3 * inch, width, 1.3 * inch, fill=1, stroke=0)
    canvas.setFillColor(ORANGE)
    canvas.rect(0, height - 1.3 * inch, 7, 1.3 * inch, fill=1, stroke=0)
    canvas.setFillColor(CHARCOAL)
    canvas.rect(0, 0, width, 0.34 * inch, fill=1, stroke=0)
    canvas.restoreState()


def finding(number, title, observed, why, action, styles):
    copy = (
        f"<b>What a customer sees:</b> {observed}<br/>"
        f"<b>Why it matters:</b> {why}<br/>"
        f"<b>Recommended fix:</b> {action}"
    )
    row = Table(
        [[NumberBadge(number), Paragraph(title, styles["finding_title"]), Paragraph(copy, styles["finding_body"])]],
        colWidths=[0.38 * inch, 1.67 * inch, 4.92 * inch],
        hAlign="LEFT",
    )
    row.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LINEBELOW", (0, 0), (-1, -1), 0.7, LINE),
            ]
        )
    )
    return row


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.38 * inch,
        bottomMargin=0.44 * inch,
        title="Sample Local Trust and Calls Audit - Bay and Beacon Auto Care",
        author="Alpha Barrie, Bay State Auto Growth",
        subject="Fictional sample auto shop online trust audit",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="main",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates(PageTemplate(id="audit", frames=[frame], onPage=page_background))

    base = getSampleStyleSheet()
    styles = {
        "brand": ParagraphStyle(
            "Brand", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10,
            leading=12, textColor=colors.white, spaceAfter=3,
        ),
        "title": ParagraphStyle(
            "Title", parent=base["Title"], fontName="Helvetica-Bold", fontSize=23,
            leading=25, textColor=colors.white, alignment=TA_LEFT,
        ),
        "meta": ParagraphStyle(
            "Meta", parent=base["Normal"], fontName="Helvetica", fontSize=8.5,
            leading=11, textColor=colors.HexColor("#D8D3C9"),
        ),
        "label": ParagraphStyle(
            "Label", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7.5,
            leading=9, textColor=ORANGE, uppercase=True,
        ),
        "opportunity": ParagraphStyle(
            "Opportunity", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=13,
            leading=16, textColor=INK,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontName="Helvetica", fontSize=8.6,
            leading=11.2, textColor=INK,
        ),
        "finding_title": ParagraphStyle(
            "FindingTitle", parent=base["Heading3"], fontName="Helvetica-Bold", fontSize=10.5,
            leading=12.5, textColor=INK, spaceAfter=0,
        ),
        "finding_body": ParagraphStyle(
            "FindingBody", parent=base["BodyText"], fontName="Helvetica", fontSize=7.8,
            leading=10.1, textColor=INK,
        ),
        "evidence_label_before": ParagraphStyle(
            "EvidenceLabelBefore", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8,
            leading=10, textColor=colors.white, alignment=TA_CENTER,
        ),
        "evidence_label_after": ParagraphStyle(
            "EvidenceLabelAfter", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8,
            leading=10, textColor=CHARCOAL, alignment=TA_CENTER,
        ),
        "quick": ParagraphStyle(
            "Quick", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=12,
            leading=15, textColor=INK,
        ),
        "quote": ParagraphStyle(
            "Quote", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10,
            leading=13, textColor=INK,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["Normal"], fontName="Helvetica", fontSize=7.2,
            leading=9, textColor=MUTED,
        ),
        "cta": ParagraphStyle(
            "CTA", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9,
            leading=11, textColor=colors.white, alignment=TA_CENTER,
        ),
    }

    header = Table(
        [[
            [Paragraph("BAY STATE AUTO GROWTH", styles["brand"]), Paragraph("Sample Local Trust &amp; Calls Audit", styles["title"])],
        ]],
        colWidths=[7.0 * inch],
        rowHeights=[0.8 * inch],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    meta = Table(
        [[
            Paragraph("<b>SHOP</b><br/>Bay &amp; Beacon Auto Care", styles["meta"]),
            Paragraph("<b>LOCATION</b><br/>East Boston, MA", styles["meta"]),
            Paragraph("<b>PREPARED BY</b><br/>Alpha Barrie", styles["meta"]),
            Paragraph("<b>STATUS</b><br/>Fictional sample", styles["meta"]),
        ]],
        colWidths=[2.0 * inch, 1.6 * inch, 1.75 * inch, 1.65 * inch],
    )
    meta.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CHARCOAL),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )

    opportunity = Table(
        [[
            Paragraph("CLEAREST OPPORTUNITY", styles["label"]),
            Paragraph(
                "The shop may already do trustworthy work, but its online experience does not quickly show customers why they should call or what to do next.",
                styles["opportunity"],
            ),
        ]],
        colWidths=[1.42 * inch, 5.58 * inch],
    )

    if not BEFORE_SCREENSHOT.exists() or not AFTER_SCREENSHOT.exists():
        raise FileNotFoundError("Capture the before and after browser screenshots before building the PDF")

    before_image = Image(str(BEFORE_SCREENSHOT), width=3.42 * inch, height=1.92 * inch)
    after_image = Image(str(AFTER_SCREENSHOT), width=3.42 * inch, height=1.92 * inch)
    evidence = Table(
        [
            [
                Paragraph("SAMPLE BEFORE - INTENTIONALLY FLAWED", styles["evidence_label_before"]),
                Paragraph("IMPROVED FICTIONAL DEMO", styles["evidence_label_after"]),
            ],
            [before_image, after_image],
        ],
        colWidths=[3.5 * inch, 3.5 * inch],
        hAlign="LEFT",
    )
    evidence.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#9D2925")),
                ("BACKGROUND", (1, 0), (1, 0), ORANGE),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.8, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, 0), 5),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
                ("TOPPADDING", (0, 1), (-1, 1), 3),
                ("BOTTOMPADDING", (0, 1), (-1, 1), 3),
            ]
        )
    )
    opportunity.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE_ORANGE),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#F8CDBA")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )

    quick_copy = (
        "<b>Use this first-screen message:</b><br/>"
        '"Clear answers. Reliable repairs."<br/>'
        "Independent auto repair in East Boston with straightforward recommendations, clear communication, and service you can approve before work begins."
    )
    quick = Table(
        [[
            Paragraph("ONE IMPROVEMENT TO MAKE NOW", styles["label"]),
            Paragraph(quick_copy, styles["quote"]),
            Paragraph("PRIMARY BUTTON<br/><b>Request service</b>", styles["body"]),
        ]],
        colWidths=[1.55 * inch, 4.15 * inch, 1.3 * inch],
    )
    quick.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0ECE3")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LINEBEFORE", (2, 0), (2, 0), 1, LINE),
            ]
        )
    )

    cta = Table(
        [[
            Paragraph(
                "If you want help putting these fixes in place, the Local Trust &amp; Calls Setup is $297 for the first three founding shops, with a seven-business-day target.",
                styles["body"],
            ),
            Paragraph("REQUEST A FREE AUDIT<br/>garage-growth-solutions.pages.dev/#audit", styles["cta"]),
        ]],
        colWidths=[4.55 * inch, 2.45 * inch],
    )
    cta.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), PALE_ORANGE),
                ("BACKGROUND", (1, 0), (1, 0), ORANGE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 11),
                ("RIGHTPADDING", (0, 0), (-1, -1), 11),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story = [
        header,
        meta,
        Spacer(1, 0.12 * inch),
        opportunity,
        Spacer(1, 0.08 * inch),
        evidence,
        Spacer(1, 0.05 * inch),
        finding(
            "01",
            "First impression is too generic",
            "The sample before says only that the shop is trusted and provides quality service. East Boston, the repair approach, and a useful next step are missing.",
            "A customer may keep comparing because the shop does not feel clearly relevant yet.",
            "The improved demo leads with East Boston, a clear service promise, Request service, and Call the shop.",
            styles,
        ),
        finding(
            "02",
            "Mobile contact path breaks down",
            "At 375 pixels, the sample before remains 1,080 pixels wide, forces horizontal scrolling, and keeps the phone action out of view.",
            "A ready-to-book customer should not have to search for the next step.",
            "The improved demo fits the screen without overflow and keeps a large Call the shop action visible.",
            styles,
        ),
        finding(
            "03",
            "Trust and contact proof arrive too late",
            "The sample before has no visible review, warranty, certification, or approval process, and contact details are buried near the footer.",
            "Customers must take the shop's generic claims on faith and work too hard to verify the basics.",
            "The improved demo combines labeled sample proof, a clear repair process, visible hours, and repeated contact actions.",
            styles,
        ),
        Spacer(1, 0.08 * inch),
        quick,
        Spacer(1, 0.08 * inch),
        cta,
        Spacer(1, 0.05 * inch),
        Paragraph(
            "Demonstration only: Bay &amp; Beacon Auto Care, the sample before, and the improved demo are fictional. This is not an actual client transformation or a complete SEO audit. No ranking, call, lead, booking, or revenue result is guaranteed.",
            styles["small"],
        ),
    ]
    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
