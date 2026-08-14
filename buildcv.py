#!/usr/bin/env python3
"""
CV build script.
Usage:
    python3 build_cv.py            -> builds the full Master CV (all bullets, no filtering)
    python3 build_cv.py A          -> builds variant A only (filters bullets by tag)

Reads master_cv.json (single source of truth) and writes a clean,
single-column, ATS-safe PDF to the output path.
"""

import json
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)
from reportlab.lib import colors

DATA_FILE = "master_cv.json"


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="CVName", fontName="Helvetica-Bold", fontSize=18,
        leading=22, spaceAfter=2, alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="CVTitle", fontName="Helvetica", fontSize=11.5,
        leading=14, spaceAfter=2, textColor=colors.HexColor("#333333")
    ))
    styles.add(ParagraphStyle(
        name="CVContact", fontName="Helvetica", fontSize=9.5,
        leading=12, spaceAfter=10, textColor=colors.HexColor("#333333")
    ))
    styles.add(ParagraphStyle(
        name="SectionHeading", fontName="Helvetica-Bold", fontSize=12,
        leading=14, spaceBefore=12, spaceAfter=4,
        textColor=colors.HexColor("#111111")
    ))
    styles.add(ParagraphStyle(
        name="CVBody", fontName="Helvetica", fontSize=10, leading=13.5,
        spaceAfter=4, alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="RoleHeading", fontName="Helvetica-Bold", fontSize=10.5,
        leading=13, spaceBefore=6, spaceAfter=1
    ))
    styles.add(ParagraphStyle(
        name="OrgDates", fontName="Helvetica-Oblique", fontSize=9.5,
        leading=12, spaceAfter=3, textColor=colors.HexColor("#444444")
    ))
    styles.add(ParagraphStyle(
        name="CVBullet", fontName="Helvetica", fontSize=9.7, leading=13,
        spaceAfter=2, leftIndent=0
    ))
    return styles


def esc(text):
    """Escape raw text so ReportLab's mini-XML parser doesn't choke on & < >."""
    if text is None:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def filter_bullets(bullets, variant):
    if variant is None:
        return [esc(b["text"]) for b in bullets]
    return [esc(b["text"]) for b in bullets if variant in b.get("tags", [])]


def build_pdf(data, variant, out_path):
    styles = build_styles()
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        topMargin=16 * mm, bottomMargin=16 * mm,
        leftMargin=18 * mm, rightMargin=18 * mm,
        title=f"{data['header']['name']} - CV"
    )

    story = []
    h = data["header"]

    # Header
    story.append(Paragraph(esc(h["name"]), styles["CVName"]))
    story.append(Paragraph(esc(h["title"]), styles["CVTitle"]))

    contact_bits = [h["location"], h["email"], h["phone"]]
    contact_bits += [l["url"] for l in h.get("links", [])]
    story.append(Paragraph(" | ".join(esc(c) for c in contact_bits), styles["CVContact"]))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#999999")))

    # Profile
    story.append(Paragraph("PROFESSIONAL PROFILE", styles["SectionHeading"]))
    story.append(Paragraph(esc(data["profile"]), styles["CVBody"]))

    # Core competencies
    story.append(Paragraph("CORE COMPETENCIES", styles["SectionHeading"]))
    comp_text = " &nbsp;&middot;&nbsp; ".join(esc(c) for c in data["core_competencies"])
    story.append(Paragraph(comp_text, styles["CVBody"]))

    # Generic repeating sections (Professional Experience, Projects, Teaching, Leadership, ...)
    for section in data.get("sections", []):
        rendered_any = False
        section_story = [Paragraph(section["heading"], styles["SectionHeading"])]
        for entry in section["entries"]:
            bullets = filter_bullets(entry["bullets"], variant)
            if not bullets:
                continue
            rendered_any = True
            title_line = esc(entry["title"])
            if entry.get("subtitle"):
                title_line += f" &mdash; {esc(entry['subtitle'])}"
            section_story.append(Paragraph(title_line, styles["RoleHeading"]))
            meta_bits = [esc(b) for b in [entry.get("location"), entry.get("dates")] if b]
            if meta_bits:
                section_story.append(Paragraph(" | ".join(meta_bits), styles["OrgDates"]))
            items = [ListItem(Paragraph(b, styles["CVBullet"]), leftIndent=12, bulletColor=colors.black)
                     for b in bullets]
            section_story.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=10))
        if rendered_any:
            story.extend(section_story)

    # Education
    story.append(Paragraph("EDUCATION", styles["SectionHeading"]))
    for ed in data["education"]:
        story.append(Paragraph(f"{esc(ed['credential'])} &mdash; {esc(ed['institution'])}", styles["RoleHeading"]))
        story.append(Paragraph(esc(ed['dates']), styles["OrgDates"]))
        if ed.get("notes"):
            story.append(Paragraph(esc(ed["notes"]), styles["CVBody"]))

    # Research & Publications
    if data.get("research_publications"):
        story.append(Paragraph("RESEARCH & PUBLICATIONS", styles["SectionHeading"]))
        items = [ListItem(Paragraph(esc(p), styles["CVBullet"]), leftIndent=12) for p in data["research_publications"]]
        story.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=10))

    # Certifications
    if data.get("certifications"):
        story.append(Paragraph("CERTIFICATIONS & LICENCES", styles["SectionHeading"]))
        items = [ListItem(Paragraph(esc(c), styles["CVBullet"]), leftIndent=12) for c in data["certifications"]]
        story.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=10))

    # Technical Skills
    if data.get("technical_skills"):
        story.append(Paragraph("TECHNICAL SKILLS", styles["SectionHeading"]))
        for cat in data["technical_skills"]:
            line = f"<b>{esc(cat['category'])}:</b> " + ", ".join(esc(i) for i in cat["items"])
            story.append(Paragraph(line, styles["CVBody"]))

    # Languages
    if data.get("languages"):
        story.append(Paragraph("LANGUAGES", styles["SectionHeading"]))
        story.append(Paragraph(" &nbsp;&middot;&nbsp; ".join(esc(l) for l in data["languages"]), styles["CVBody"]))

    doc.build(story)


if __name__ == "__main__":
    variant = sys.argv[1] if len(sys.argv) > 1 else None
    data = load_data()
    suffix = f"_variant_{variant}" if variant else "_master"
    out_path = f"Brian_Lembuss_CV{suffix}.pdf"
    build_pdf(data, variant, out_path)
    print(f"Built: {out_path}")