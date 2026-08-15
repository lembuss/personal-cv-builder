#!/usr/bin/env python3
"""
Multi-Track CV Build Script (v2.0)
Usage:
    python3 build_cv.py             -> Builds full Master CV (all content, no filtering)
    python3 build_cv.py A           -> Builds Track A: Aircraft Systems & Aerospace Engineering
    python3 build_cv.py B           -> Builds Track B: Venture Building & Entrepreneurial Leadership
    python3 build_cv.py C           -> Builds Track C: Deep-Tech Research & Computational Capability
    python3 build_cv.py D           -> Builds Track D: Teaching, Mentorship & Academic Service

Reads mastercv_multitrack.json and writes a clean, single-column ATS-safe PDF.
"""

import json
import sys
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)
from reportlab.lib import colors

DATA_FILE = "mastercv_generated_multitrack.json"

TRACK_ALIASES = {
    "A": "aircraft_systems_aerospace_engineering",
    "AIRCRAFT": "aircraft_systems_aerospace_engineering",
    "B": "venture_building_entrepreneurial_leadership",
    "VENTURE": "venture_building_entrepreneurial_leadership",
    "C": "deep_tech_research_computational_capability",
    "RESEARCH": "deep_tech_research_computational_capability",
    "D": "teaching_mentorship_academic_service",
    "TEACHING": "teaching_mentorship_academic_service"
}


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="CVName", fontName="Helvetica-Bold", fontSize=18,
        leading=22, spaceAfter=2, alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="CVTitle", fontName="Helvetica-Bold", fontSize=11,
        leading=14, spaceAfter=2, textColor=colors.HexColor("#222222")
    ))
    styles.add(ParagraphStyle(
        name="CVContact", fontName="Helvetica", fontSize=9,
        leading=12, spaceAfter=8, textColor=colors.HexColor("#444444")
    ))
    styles.add(ParagraphStyle(
        name="SectionHeading", fontName="Helvetica-Bold", fontSize=11.5,
        leading=14, spaceBefore=10, spaceAfter=4,
        textColor=colors.HexColor("#111111")
    ))
    styles.add(ParagraphStyle(
        name="CVBody", fontName="Helvetica", fontSize=9.5, leading=13,
        spaceAfter=4, alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="RoleHeading", fontName="Helvetica-Bold", fontSize=10,
        leading=12.5, spaceBefore=5, spaceAfter=1
    ))
    styles.add(ParagraphStyle(
        name="SubProjectHeading", fontName="Helvetica-BoldOblique", fontSize=9.5,
        leading=12, spaceBefore=3, spaceAfter=1, textColor=colors.HexColor("#222222")
    ))
    styles.add(ParagraphStyle(
        name="OrgDates", fontName="Helvetica-Oblique", fontSize=9,
        leading=11.5, spaceAfter=3, textColor=colors.HexColor("#555555")
    ))
    styles.add(ParagraphStyle(
        name="CVBullet", fontName="Helvetica", fontSize=9, leading=12.5,
        spaceAfter=2, leftIndent=0
    ))
    return styles


def esc(text):
    """Escape raw text so ReportLab's mini-XML parser doesn't choke on & < >."""
    if text is None:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def resolve_track(arg):
    if not arg:
        return None
    cleaned = str(arg).strip().upper()
    if cleaned in TRACK_ALIASES:
        return TRACK_ALIASES[cleaned]
    lowered = str(arg).strip().lower()
    return lowered


def is_active_track(item_tracks, target_track):
    if target_track is None:
        return True
    if not item_tracks:
        return True
    return target_track in item_tracks


def build_pdf(data_root, target_track, out_path):
    styles = build_styles()
    doc_data = data_root["document"]
    c = doc_data["contact"]

    pdf = SimpleDocTemplate(
        out_path, pagesize=A4,
        topMargin=14 * mm, bottomMargin=14 * mm,
        leftMargin=15 * mm, rightMargin=15 * mm,
        title=f"{c['name']} - CV"
    )

    story = []

    # 1. Header
    story.append(Paragraph(esc(c["name"]), styles["CVName"]))
    story.append(Paragraph(esc(doc_data["title"]), styles["CVTitle"]))

    contact_bits = [c["location"], c["email"], c["phone"], c["linkedin"], c["github"]]
    contact_str = " | ".join(esc(bit) for bit in contact_bits if bit)
    story.append(Paragraph(contact_str, styles["CVContact"]))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#888888")))

    # 2. Profile
    story.append(Paragraph("PROFESSIONAL PROFILE", styles["SectionHeading"]))
    story.append(Paragraph(esc(doc_data["profile"]), styles["CVBody"]))

    # 3. Core Competencies (Filtered by track or rendered as complete 4-pillar blocks)
    story.append(Paragraph("CORE COMPETENCIES", styles["SectionHeading"]))
    for block in doc_data.get("core_competencies", []):
        if is_active_track([block.get("track")], target_track):
            label = esc(block.get("label", ""))
            items_str = ", ".join(esc(i) for i in block.get("items", []))
            story.append(Paragraph(f"<b>{label}:</b> {items_str}", styles["CVBody"]))

    # 4. Professional Experience & Sub-Projects
    story.append(Paragraph("PROFESSIONAL EXPERIENCE & SELECTED R&D PROJECTS", styles["SectionHeading"]))
    for exp in doc_data.get("experiences", []):
        if not is_active_track(exp.get("tracks", []), target_track):
            continue

        role_line = f"{esc(exp['role'])} &mdash; <b>{esc(exp['company'])}</b>"
        if exp.get("type"):
            role_line += f" ({esc(exp['type'])})"
        story.append(Paragraph(role_line, styles["RoleHeading"]))

        meta_bits = [esc(b) for b in [exp.get("location"), exp.get("dates")] if b]
        if meta_bits:
            story.append(Paragraph(" | ".join(meta_bits), styles["OrgDates"]))

        if exp.get("summary") and target_track is None:
            story.append(Paragraph(f"<i>{esc(exp['summary'])}</i>", styles["CVBody"]))

        for proj in exp.get("projects", []):
            if not is_active_track(proj.get("tracks", []), target_track):
                continue

            story.append(Paragraph(esc(proj["name"]), styles["SubProjectHeading"]))
            bullet_items = [
                ListItem(Paragraph(esc(b), styles["CVBullet"]), leftIndent=10, bulletColor=colors.black)
                for b in proj.get("bullets", [])
            ]
            if bullet_items:
                story.append(ListFlowable(bullet_items, bulletType="bullet", start="•", leftIndent=8))

    # 5. Additional Research & Academic Projects
    add_projects = [
        p for p in doc_data.get("additional_research_projects", [])
        if is_active_track(p.get("tracks", []), target_track)
    ]
    if add_projects:
        story.append(Paragraph("ADDITIONAL RESEARCH & ACADEMIC PROJECTS", styles["SectionHeading"]))
        for proj in add_projects:
            title = esc(proj["name"])
            if proj.get("institution"):
                title += f" &mdash; <i>{esc(proj['institution'])}</i>"
            story.append(Paragraph(title, styles["SubProjectHeading"]))
            if proj.get("dates"):
                story.append(Paragraph(esc(proj["dates"]), styles["OrgDates"]))

            bullet_items = [
                ListItem(Paragraph(esc(b), styles["CVBullet"]), leftIndent=10)
                for b in proj.get("bullets", [])
            ]
            if bullet_items:
                story.append(ListFlowable(bullet_items, bulletType="bullet", start="•", leftIndent=8))

    # 6. Education
    story.append(Paragraph("EDUCATION", styles["SectionHeading"]))
    for ed in doc_data.get("education", []):
        if not is_active_track(ed.get("tracks", []), target_track):
            continue
        line = f"<b>{esc(ed['degree'])}</b> &mdash; {esc(ed['institution'])}"
        if ed.get("location"):
            line += f" ({esc(ed['location'])})"
        story.append(Paragraph(line, styles["RoleHeading"]))
        story.append(Paragraph(esc(ed["dates"]), styles["OrgDates"]))
        if ed.get("status"):
            story.append(Paragraph(f"<b>Status:</b> {esc(ed['status'])}", styles["CVBody"]))

    # 7. Research & Publications
    pubs = [
        p for p in doc_data.get("publications", [])
        if is_active_track(p.get("tracks", []), target_track)
    ]
    if pubs:
        story.append(Paragraph("RESEARCH & PUBLICATIONS", styles["SectionHeading"]))
        pub_items = []
        for p in pubs:
            text = f"<b>{esc(p['role'])}</b>, <i>\"{esc(p['title'])}\"</i> &mdash; {esc(p['venue'])}"
            pub_items.append(ListItem(Paragraph(text, styles["CVBullet"]), leftIndent=10))
        story.append(ListFlowable(pub_items, bulletType="bullet", start="•", leftIndent=8))

    # 8. Teaching & Academic Experience
    teaching_entries = [
        t for t in doc_data.get("teaching", [])
        if is_active_track(t.get("tracks", []), target_track)
    ]
    if teaching_entries:
        story.append(Paragraph("TEACHING & ACADEMIC EXPERIENCE", styles["SectionHeading"]))
        for t in teaching_entries:
            title = f"<b>{esc(t['role'])}</b> &mdash; {esc(t['institution'])}"
            story.append(Paragraph(title, styles["RoleHeading"]))
            meta = " | ".join(esc(b) for b in [t.get("location"), t.get("dates")] if b)
            if meta:
                story.append(Paragraph(meta, styles["OrgDates"]))
            if t.get("details"):
                story.append(Paragraph(esc(t["details"]), styles["CVBody"]))

    # 9. Leadership & Mentorship
    leadership_entries = [
        l for l in doc_data.get("leadership", [])
        if is_active_track(l.get("tracks", []), target_track)
    ]
    if leadership_entries:
        story.append(Paragraph("LEADERSHIP & MENTORSHIP", styles["SectionHeading"]))
        for l in leadership_entries:
            title = f"<b>{esc(l['role'])}</b> &mdash; {esc(l['organisation'])}"
            story.append(Paragraph(title, styles["RoleHeading"]))
            if l.get("dates"):
                story.append(Paragraph(esc(l["dates"]), styles["OrgDates"]))
            if l.get("details"):
                story.append(Paragraph(esc(l["details"]), styles["CVBody"]))

    # 10. Certifications
    if doc_data.get("certifications"):
        story.append(Paragraph("LICENCES & CERTIFICATIONS", styles["SectionHeading"]))
        cert_items = [
            ListItem(Paragraph(esc(c), styles["CVBullet"]), leftIndent=10)
            for c in doc_data["certifications"]
        ]
        story.append(ListFlowable(cert_items, bulletType="bullet", start="•", leftIndent=8))

    # 11. Languages
    if doc_data.get("languages"):
        story.append(Paragraph("LANGUAGES", styles["SectionHeading"]))
        lang_str = " &nbsp;&middot;&nbsp; ".join(
            f"<b>{esc(l['language'])}:</b> {esc(l['level'])}" for l in doc_data["languages"]
        )
        story.append(Paragraph(lang_str, styles["CVBody"]))

    pdf.build(story)


if __name__ == "__main__":
    raw_arg = sys.argv[1] if len(sys.argv) > 1 else None
    target_track = resolve_track(raw_arg)
    data = load_data()

    suffix = f"_{raw_arg.upper()}" if raw_arg else "_Master"
    out_file = f"Brian_Lembuss_CV{suffix}.pdf"

    build_pdf(data, target_track, out_file)
    print(f"Successfully generated PDF: {out_file} (Track: {target_track or 'ALL'})")