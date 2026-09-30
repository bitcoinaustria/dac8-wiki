"""Render the adjacent authoritative Markdown memorandum as a sober A4 PDF.

Requires reportlab. No network calls. The source text and hyperlinks are retained.
Run: python3 render-finanzdatenprofile.py [--source /path/to/report.md]
"""

from html import escape
from pathlib import Path
import argparse
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
)


DIRECTORY = Path(__file__).resolve().parent
SOURCE = DIRECTORY / "argumentationsvermerk-finanzdatenprofile-2026-09-30.md"
DESTINATION = SOURCE.with_suffix(".pdf")
FONT_DIRECTORY = Path("/System/Library/Fonts/Supplemental")
FONTS = {
    "Memo": "Arial.ttf",
    "Memo-Bold": "Arial Bold.ttf",
    "Memo-Italic": "Arial Italic.ttf",
    "Memo-BoldItalic": "Arial Bold Italic.ttf",
}
for font_name, filename in FONTS.items():
    pdfmetrics.registerFont(TTFont(font_name, str(FONT_DIRECTORY / filename)))
pdfmetrics.registerFontFamily(
    "Memo", normal="Memo", bold="Memo-Bold", italic="Memo-Italic",
    boldItalic="Memo-BoldItalic",
)

BODY = ParagraphStyle(
    "Body", fontName="Memo", fontSize=10.4, leading=14.2,
    alignment=TA_LEFT, spaceAfter=6, allowWidows=0, allowOrphans=0,
)
TITLE = ParagraphStyle(
    "Title", parent=BODY, fontName="Memo-Bold", fontSize=19,
    leading=23, spaceAfter=8, keepWithNext=True,
)
HEADING = ParagraphStyle(
    "Heading", parent=BODY, fontName="Memo-Bold", fontSize=13.2,
    leading=17, spaceBefore=11, spaceAfter=6, keepWithNext=True,
)
SUBHEADING = ParagraphStyle(
    "Subheading", parent=BODY, fontName="Memo-Bold", fontSize=11,
    leading=14.5, spaceBefore=7, spaceAfter=5, keepWithNext=True,
)
CELL = ParagraphStyle("Cell", parent=BODY, fontSize=9.4, leading=12.2, spaceAfter=0)
HEADER_CELL = ParagraphStyle("HeaderCell", parent=CELL, fontName="Memo-Bold")
LIST = ParagraphStyle(
    "List", parent=BODY, leftIndent=15, firstLineIndent=0,
    bulletIndent=0, spaceAfter=6,
)


def inline(text):
    """Convert the small Markdown subset used here to ReportLab paragraph XML."""
    text = text.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    tokens = []

    def link(match):
        label, target = match.groups()
        if not target.startswith("https://"):
            raise ValueError(f"Unsupported PDF link: {target}")
        tokens.append(
            f'<link href="{escape(target, quote=True)}" color="#145596">'
            f"<u>{escape(label)}</u></link>"
        )
        return f"LINKTOKEN{len(tokens) - 1}END"

    text = re.sub(r"\[([^\]]+)\]\((https://[^\s]+?)\)", link, text)
    text = escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    for index, token in enumerate(tokens):
        text = text.replace(f"LINKTOKEN{index}END", token)
    return text


def markdown_story(text, width):
    if not text.startswith("---\n"):
        raise ValueError("Expected report frontmatter")
    _, _, body = text.split("---", 2)
    lines = body.strip().splitlines()
    story, index = [], 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith("|"):
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                    rows.append(cells)
                index += 1
            column_count = len(rows[0])
            if any(len(row) != column_count for row in rows):
                raise ValueError("Nonrectangular Markdown table")
            proportions = {
                2: [0.34, 0.66],
                3: [0.25, 0.39, 0.36],
                4: [0.18, 0.38, 0.22, 0.22],
            }[column_count]
            data = [
                [Paragraph(inline(cell), HEADER_CELL if row_index == 0 else CELL)
                 for cell in row]
                for row_index, row in enumerate(rows)
            ]
            table = Table(data, colWidths=[width * p for p in proportions], repeatRows=1)
            table.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
                ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.HexColor("#777777")),
                ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#cccccc")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.extend([table, Spacer(1, 8)])
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), TITLE))
        elif line.startswith("## "):
            story.append(Paragraph(inline(line[3:]), HEADING))
        elif line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), SUBHEADING))
        elif re.match(r"\d+\. ", line):
            number, content = line.split(". ", 1)
            story.append(Paragraph(inline(content), LIST, bulletText=f"{number}."))
        else:
            paragraph = [line]
            while index + 1 < len(lines):
                next_line = lines[index + 1].strip()
                if not next_line or next_line.startswith(("#", "|")) or re.match(r"\d+\. ", next_line):
                    break
                index += 1
                paragraph.append(next_line)
            story.append(Paragraph(inline(" ".join(paragraph)), BODY))
        index += 1
    return story


def footer(canvas, document):
    canvas.saveState()
    canvas.setFont("Memo", 9)
    canvas.setFillColor(colors.HexColor("#444444"))
    canvas.drawCentredString(A4[0] / 2, 28, str(document.page))
    canvas.restoreState()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--subject", default="Source-backed legal argumentation material")
    arguments = parser.parse_args()
    source = arguments.source.resolve()
    if source.suffix != ".md" or source.parent != DIRECTORY:
        parser.error("Source must be a Markdown report in this output project")
    destination = source.with_suffix(".pdf")
    source_text = source.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", source_text, flags=re.MULTILINE).group(1)
    document = SimpleDocTemplate(
        str(destination), pagesize=A4, leftMargin=52, rightMargin=52,
        topMargin=43, bottomMargin=47, title=title,
        author="LLM Wiki", subject=arguments.subject,
    )
    document.build(
        markdown_story(source_text, document.width),
        onFirstPage=footer, onLaterPages=footer,
    )
    print(destination)
