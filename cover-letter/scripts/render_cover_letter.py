#!/usr/bin/env python3
"""Render an application JSON to PDF and verify its complete extracted text."""

import argparse
import json
import re
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape, quoteattr

import pdfplumber
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter as LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


ASSETS = Path(__file__).resolve().parents[1] / "assets"
DASHES = str.maketrans({"\u2010": "-", "\u2011": "-", "\u2013": "-", "\u2014": "-"})
STYLE_KEYS = {
    "page_size", "accent", "font_regular", "font_bold", "body_size", "leading",
    "paragraph_spacing", "margin_x", "margin_y", "name_size", "contact_size",
}


def text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    return " ".join(value.translate(DASHES).split())


def lines(value, label):
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a nonempty list")
    return [text(item, f"{label}[{index}]") for index, item in enumerate(value)]


def normalized(value):
    return " ".join(unicodedata.normalize("NFKC", value).split())


def positive(style, key, default, allow_zero=False):
    value = style.get(key, default)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"style.{key} must be a number")
    if not (0 <= value < 1000 if allow_zero else 0 < value < 1000):
        raise ValueError(f"style.{key} is outside the supported range")
    return value


def parse_source(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("The application source must be a JSON object")
    fields = {key: text(data.get(key), key) for key in ("name", "date", "company", "role")}
    fields["recipient"] = lines(data.get("recipient"), "recipient")
    fields["paragraphs"] = lines(data.get("paragraphs"), "paragraphs")
    default_subject = "Application for " + fields["role"]
    if data.get("reference"):
        default_subject += " | " + text(data["reference"], "reference")
    for key, default in (
        ("subject", default_subject), ("salutation", "Dear Hiring Team,"),
        ("closing", "Sincerely,"), ("signature", fields["name"]),
    ):
        fields[key] = text(data.get(key, default), key)

    contact_lines = data.get("contact_lines", [])
    if not isinstance(contact_lines, list):
        raise ValueError("contact_lines must be a list of contact rows")
    fields["contacts"] = []
    for row in contact_lines:
        if not isinstance(row, list) or not row:
            raise ValueError("Each contact row must be a nonempty list")
        plain_row, marked_row = [], []
        for item in row:
            if not isinstance(item, dict):
                raise ValueError("Each contact must contain text and optional href")
            label = text(item.get("text"), "contact text")
            markup = escape(label)
            if "href" in item:
                href = item["href"]
                if not isinstance(href, str) or urlparse(href).scheme.lower() not in {"http", "https", "mailto", "tel"}:
                    raise ValueError("Contact links must use http, https, mailto or tel")
                markup = f"<link href={quoteattr(href)}>{markup}</link>"
            plain_row.append(label)
            marked_row.append(markup)
        fields["contacts"].append((" | ".join(plain_row), " | ".join(marked_row)))

    style = data.get("style", {})
    if not isinstance(style, dict) or set(style) - STYLE_KEYS:
        raise ValueError(f"style must be an object using these keys: {', '.join(sorted(STYLE_KEYS))}")
    return fields, style


def render(fields, style, source_dir, path):
    size_name = style.get("page_size", "A4")
    if size_name not in {"A4", "Letter"}:
        raise ValueError("style.page_size must be A4 or Letter")
    page_size = A4 if size_name == "A4" else LETTER
    accent = style.get("accent", "#333333")
    if not isinstance(accent, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", accent):
        raise ValueError("style.accent must be a six-digit hex colour")
    accent = colors.HexColor(accent)
    if bool(style.get("font_regular")) != bool(style.get("font_bold")):
        raise ValueError("Supply both font_regular and font_bold")

    font_paths = []
    for weight, filename in (("regular", "SourceSans3-Regular.ttf"), ("bold", "SourceSans3-Bold.ttf")):
        selected = style.get("font_" + weight)
        font_path = Path(selected) if selected else ASSETS / filename
        if not font_path.is_absolute():
            font_path = source_dir / font_path
        font_path = font_path.resolve(strict=True)
        font_paths.append(font_path)
        pdfmetrics.registerFont(TTFont("Cover-" + weight, str(font_path)))
    pdfmetrics.registerFontFamily("Cover-regular", normal="Cover-regular", bold="Cover-bold")

    expected = [
        fields["name"], *(plain for plain, _ in fields["contacts"]), fields["date"],
        *fields["recipient"], fields["subject"], fields["salutation"],
        *fields["paragraphs"], fields["closing"], fields["signature"],
    ]
    required_chars = set("".join(expected)) - set(" \n\t\r")
    for face in ("Cover-regular", "Cover-bold"):
        missing = sorted(character for character in required_chars if ord(character) not in pdfmetrics.getFont(face).face.charToGlyph)
        if missing:
            raise ValueError(f"{face} lacks glyphs for {''.join(missing)!r}; supply a font covering this language")

    margin_x = positive(style, "margin_x", 50)
    margin_y = positive(style, "margin_y", 42)
    width, height = page_size
    if width - 2 * margin_x < 180 or height - 2 * margin_y < 180:
        raise ValueError("Margins leave too little space for the letter")
    body_size = positive(style, "body_size", 11.5)
    leading = positive(style, "leading", 15.5)
    if leading < body_size:
        raise ValueError("Leading must be at least the body font size")
    paragraph_spacing = positive(style, "paragraph_spacing", 10, allow_zero=True)
    name_size = positive(style, "name_size", 24)
    contact_size = positive(style, "contact_size", 10.25)
    body = ParagraphStyle("Body", fontName="Cover-regular", fontSize=body_size,
                          leading=leading, spaceAfter=paragraph_spacing,
                          textColor=colors.HexColor("#202020"), splitLongWords=False,
                          allowWidows=0, allowOrphans=0)
    heading = ParagraphStyle("Name", parent=body, fontName="Cover-bold", fontSize=name_size,
                             leading=name_size + 4, textColor=accent, spaceAfter=5)
    contact = ParagraphStyle("Contact", parent=body, fontSize=contact_size,
                             leading=contact_size + 3.25, textColor=accent, spaceAfter=0)
    small = ParagraphStyle("Small", parent=body, fontSize=10.5, leading=14, spaceAfter=0)
    subject = ParagraphStyle("Subject", parent=body, fontName="Cover-bold", spaceAfter=13)
    signature = ParagraphStyle("Signature", parent=body, spaceAfter=0)

    doc = SimpleDocTemplate(str(path), pagesize=page_size, leftMargin=margin_x,
                            rightMargin=margin_x, topMargin=margin_y, bottomMargin=margin_y,
                            title=f'{fields["name"]} | {fields["company"]} | {fields["role"]}',
                            author=fields["name"], subject=fields["subject"], pageCompression=1)
    story = [Paragraph(escape(fields["name"]), heading)]
    story.extend(Paragraph(markup, contact) for _, markup in fields["contacts"])
    story.extend([
        Spacer(1, 11),
        HRFlowable(width="100%", thickness=0.7, color=accent, spaceAfter=14),
        Paragraph(escape(fields["date"]), small), Spacer(1, 11),
        Paragraph("<br/>".join(escape(line) for line in fields["recipient"]), small),
        Spacer(1, 13), Paragraph(escape(fields["subject"]), subject),
        Paragraph(escape(fields["salutation"]), body),
    ])
    isolated = []
    for number, paragraph in enumerate(fields["paragraphs"], 1):
        flowable = Paragraph(escape(paragraph), body)
        flowable.wrap(width - 2 * margin_x - 12, height)
        wrapped = flowable.blPara
        if wrapped.kind == 0 and len(wrapped.lines) > 1 and len(wrapped.lines[-1][1]) == 1:
            isolated.append(number)
        story.append(flowable)
    story.append(Paragraph(escape(fields["closing"]) + "<br/>" + escape(fields["signature"]), signature))
    doc.build(story)
    return expected, isolated, margin_x, margin_y, font_paths


def verify(path, expected, max_pages, margin_x, margin_y):
    reader = PdfReader(path)
    if reader.is_encrypted:
        raise ValueError("Generated PDF is unexpectedly encrypted")
    if not 1 <= len(reader.pages) <= max_pages:
        raise ValueError(f"PDF has {len(reader.pages)} pages; allowed maximum is {max_pages}. Revise content or layout, or intentionally change --max-pages.")
    extracted = {"pypdf": "\n".join(page.extract_text() or "" for page in reader.pages)}
    with pdfplumber.open(path) as pdf:
        extracted["pdfplumber"] = "\n".join(page.extract_text() or "" for page in pdf.pages)
        for number, page in enumerate(pdf.pages, 1):
            if not page.chars:
                raise ValueError(f"Page {number} has no selectable text")
            for char in page.chars:
                if (char["x0"] < margin_x - 1 or char["x1"] > page.width - margin_x + 1
                        or char["top"] < margin_y - 1 or char["bottom"] > page.height - margin_y + 1):
                    raise ValueError(f"Text exceeds the intended margins on page {number}")
    wanted = normalized("\n".join(expected))
    for engine, actual in extracted.items():
        if normalized(actual) != wanted:
            raise ValueError(f"{engine} extraction does not match complete expected content in reading order")
    return {"pages": len(reader.pages), "characters": len(extracted["pypdf"]),
            "content_verified": list(extracted)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Per-application JSON file")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-pages", type=int, default=1)
    parser.add_argument("--overwrite", action="store_true", help="Replace an intended revision after it passes verification")
    args = parser.parse_args()
    try:
        if args.max_pages < 1:
            raise ValueError("--max-pages must be positive")
        source = args.source.resolve(strict=True)
        output = args.output.resolve()
        if output.suffix.lower() != ".pdf":
            raise ValueError("--output must end in .pdf")
        if output.exists() and not args.overwrite:
            raise ValueError("Output already exists; use a separate filename or --overwrite for an intended revision")
        fields, style = parse_source(source)
        output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".cover-letter-", dir=output.parent) as temporary:
            candidate = Path(temporary) / "letter.pdf"
            expected, isolated, margin_x, margin_y, fonts = render(fields, style, source.parent, candidate)
            report = verify(candidate, expected, args.max_pages, margin_x, margin_y)
            if args.overwrite:
                candidate.replace(output)
            else:
                with output.open("xb") as destination:
                    destination.write(candidate.read_bytes())
        report.update({"pdf": str(output), "fonts": [str(font) for font in fonts],
                       "isolated_final_word_paragraphs": isolated, "visual_review": "required"})
        print(json.dumps(report, ensure_ascii=False))
        return 0
    except Exception as error:
        print(f"Cover letter not published: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
