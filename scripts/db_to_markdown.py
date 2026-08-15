import sqlite3
from collections import defaultdict

conn = sqlite3.connect('/mnt/user-data/uploads/dev.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

exps = {r['id']: dict(r) for r in cur.execute('SELECT * FROM Experience')}
projs = {r['id']: dict(r) for r in cur.execute('SELECT * FROM Project')}
acts = [dict(r) for r in cur.execute('SELECT * FROM Activity')]
tags = {r['id']: dict(r) for r in cur.execute('SELECT * FROM Tag')}

act_tags = defaultdict(list)
for r in cur.execute('SELECT * FROM ActivityTag'):
    act_tags[r['activityId']].append(tags[r['tagId']]['name'])

proj_tags = defaultdict(list)
for r in cur.execute('SELECT * FROM ProjectTag'):
    proj_tags[r['projectId']].append(tags[r['tagId']]['name'])

acts_by_exp = defaultdict(list)
for a in acts:
    acts_by_exp[a['experienceId']].append(a)

projs_by_exp = defaultdict(list)
for p in projs.values():
    projs_by_exp[p['experienceId']].append(p)

acts_by_proj = defaultdict(list)
for a in acts:
    if a['projectId']:
        acts_by_proj[a['projectId']].append(a)


def fmt_date(e):
    s = e['startDate'][:7] if e['startDate'] else '?'
    end = 'Present' if e['current'] else (e['endDate'][:7] if e['endDate'] else '?')
    return f"{s} – {end}"


def activity_block(a, idx):
    lines = []
    lines.append(f"**Activity {idx} — What:** {a['what']}")
    if a['how']:
        lines.append(f"**How:** {a['how']}")
    lines.append(f"**Responsibility:** {a['responsibility']}")
    if a['result']:
        lines.append(f"**Result:** {a['result']}")
    if a['problem']:
        lines.append(f"**Problem:** {a['problem']}")
    if a['diagnosis']:
        lines.append(f"**Diagnosis:** {a['diagnosis']}")
    if a['intervention']:
        lines.append(f"**Intervention:** {a['intervention']}")
    if a['interventionResult']:
        lines.append(f"**Intervention Result:** {a['interventionResult']}")
    t = act_tags.get(a['id'], [])
    if t:
        lines.append(f"**Tags:** {', '.join(sorted(t))}")
    if a['notes']:
        lines.append(f"**Notes:** {a['notes']}")
    return "\n\n".join(lines)


def project_block(p, counter_start):
    out = []
    out.append(f"#### Project: {p['name']}")
    out.append(f"- **System:** {p['system']}")
    out.append(f"- **Objective:** {p['objective']}")
    out.append(f"- **Description:** {p['description']}")
    out.append(f"- **Outcome:** {p['outcome']}")
    out.append(f"- **R&D Project:** {'Yes' if p['isRnD'] else 'No'}")
    pt = proj_tags.get(p['id'], [])
    if pt:
        out.append(f"- **Project Tags:** {', '.join(sorted(pt))}")
    if p['notes']:
        out.append(f"- **Notes:** {p['notes']}")
    out.append("")
    plist = acts_by_proj.get(p['id'], [])
    for i, a in enumerate(plist, counter_start):
        out.append(activity_block(a, i))
        out.append("")
    return "\n".join(out), counter_start + len(plist)


def experience_block(e):
    out = []
    out.append(f"### {e['organization'].strip()} — {e['title']}")
    out.append(f"*{e['role']} | {e['location']} | {fmt_date(e)}*")
    out.append("")
    out.append(e['description'])
    out.append("")
    eid = e['id']
    exp_level_acts = [a for a in acts_by_exp[eid] if not a['projectId']]
    plist = projs_by_exp.get(eid, [])
    counter = 1
    if plist:
        out.append(f"**Projects under this experience ({len(plist)}):**")
        out.append("")
        for p in plist:
            block, counter = project_block(p, counter)
            out.append(block)
    if exp_level_acts:
        out.append("**Experience-level Activities (not tied to a specific project):**")
        out.append("")
        for a in exp_level_acts:
            out.append(activity_block(a, counter))
            out.append("")
            counter += 1
    out.append("---")
    out.append("")
    return "\n".join(out)


# Order experiences by startDate DESC — fully dynamic, no hardcoding
ordered_ids = [r['id'] for r in cur.execute(
    'SELECT id FROM Experience ORDER BY startDate DESC'
)]

# --- Build tag competencies from DB ---
cats = defaultdict(list)
for t in tags.values():
    cats[t['category']].append(t['name'])

# --- Static sections 1 & 2 ---
STATIC_HEADER = """# MASTER CONTENT POOL — Brian Lembuss Kirwa
## Phase 6C — Complete Un-Pruned Career Database Compilation (v3)

*Source of truth: `dev.db` (SQLite). This document contains 100% of database content — 20 Experiences, 40 Projects, 163 Activities — with no pruning, condensing, page-limit, or omission, per CAREER-CV-ROADMAP-HANDOVER-V3.md §0, §1, §5. It is the un-pruned Master Content Pool from which all 8 downstream application tracks (industry, UAS/eVTOL/AAM, R&D, PhD admissions, TUM MSc scholarships, further education, entrepreneurial/founder-track, and teaching/academic roles) will be derived.*

---

## 1. Master Professional Profile (Four Equal-Priority Pillars)

Brian Lembuss Kirwa is an aerospace systems engineer, technical founder, and academic instructor whose career spans four equally weighted professional pillars, per the Phase 5 locked baseline (CAREER-CV-ROADMAP-HANDOVER-V3.md §4):

**Pillar 1 — Aircraft Systems & Aerospace Engineering:** End-to-end systems lifecycle ownership (requirements, functional decomposition, architecture, HW/SW integration, HIL testing, V&V, MRO, flight testing) across manned aircraft (ALS Ltd), UAV OEMs (Amazilia Aerospace, Kipepeo Aerospace), and eVTOL platforms (HORYZN).

**Pillar 2 — Venture Building & Entrepreneurial Leadership:** Technical founder capability — Kipepeo Aerospace company incorporation (BN-BGCKDY99), Pre-Incorporation Founders' Agreement (80/20 equity split, 4-year reverse vesting), $1,000 SAFE at $1M cap with Zimbu Investments, $150k Microsoft + $2k Google startup grants, 3 commercial MoUs, Jasiri Fellow (Jasiri4Africa), #MyLittleBigThing, Startup360 A2F, 2026–2027 IRP cohort, and 120 farmer validation studies (Kilimo Anga).

**Pillar 3 — Deep-Tech Research & Computational Capability:** Applied research and publication depth — AIAA 2024 co-authored UAM throughput paper, embedded C++ TDD logging with 5× compression, MBSE agricultural UAS architecture graded *Sehr gut* (A, 8 ECTS), ROS/OctoMap 3D subterranean perception, and OpenFOAM/ANSYS CFX CFD.

**Pillar 4 — Teaching, Mentorship & Academic Service:** Academic instruction and administration — TUM EC135 IFR simulator instructor/examiner, METU ASE301 Numerical Methods TA, certified SI-PASS Calculus tutoring, Young Scientists Kenya STEM mentorship (43.6% engine efficiency gain achieved by mentees), and METU ISA Secretary General managing 8 directorates.

**TUM MSc Status:** Degree completion pending — 73 ECTS completed; 17 credits and thesis remaining. Never to be represented as completed or awarded (roadmap §5, Rule 2).

---

"""

# Section 2 built from DB tags
section2 = "## 2. Core Competencies (Full Domain Taxonomy from `dev.db` Tag Library)\n\n"
for cat, label in [
    ("Lifecycle", "### Systems Engineering Lifecycle"),
    ("TechnicalDomain", "### Technical Domains"),
    ("SkillTool", "### Skills & Tools"),
    ("Other", "### Other (Venture / Governance / Teaching / Academic)"),
]:
    section2 += label + "\n\n"
    section2 += ", ".join(sorted(cats[cat])) + "\n\n"

# Section 3 — generated from DB
section3 = "## 3. Complete Professional Experience (All 20 Experiences)\n\n"
total_acts = 0
for eid in ordered_ids:
    e = exps[eid]
    section3 += experience_block(e) + "\n"
    total_acts += len(acts_by_exp[eid])

# Sections 4-9 — generated from DB where possible, static cross-references otherwise
# Section 5: Education — pulled from DB Experience descriptions
edu_roles = {"Graduate Student", "Undergraduate Student", "DAAD Scholar"}
edu_exps = [e for e in exps.values() if e['role'] in edu_roles and e['organization'] in
            {"Technical University of Munich", "Middle East Technical University", "University of Cologne"}]
edu_exps = sorted(edu_exps, key=lambda e: e['startDate'], reverse=True)

section5 = "## 5. Education\n\n"
for e in edu_exps:
    section5 += f"- **{e['title']} — {e['organization']}**, {e['location']}. {fmt_date(e)}. {e['description']}\n"
section5 += "\n"

# Section 6: Publications — cross-reference only (detail is in Section 3)
section6 = """## 6. Research & Publications

- **AIAA 2024** — Co-authored paper on Urban Air Mobility (UAM) throughput. Full activity-level detail in Section 3 under TUM MSc → Generic Modeling of Slotneutral UAM Throughput.
- **Geotourism journal article** — activity-level detail in Section 3 under TUM MSc → Geospatial Analysis & Cartography.
- **TUM UAM Thesis** — in progress, pending submission (see Section 5, TUM MSc status).
- **MBSE Agricultural UAS Architecture** — graded *Sehr gut* (A), 8 ECTS. Detail in Section 3 under University of Cologne → LEAD! Leadership for Africa.

*Full narrative and citation-level detail for each publication is embedded in its source Activity/Project block in Section 3.*

"""

# Section 7: Teaching — pulled from DB
teaching_keywords = ["Instructor", "Assistant", "SI-PASS", "Mentor"]
teaching_exps = [e for e in exps.values()
                 if any(k in e['title'] for k in teaching_keywords)]
teaching_exps = sorted(teaching_exps, key=lambda e: e['startDate'], reverse=True)

section7 = "## 7. Teaching & Academic Experience\n\nConsolidated cross-reference (full detail in Section 3):\n"
for e in teaching_exps:
    n_acts = len(acts_by_exp[e['id']])
    section7 += f"- **{e['organization'].strip()} — {e['title']}** ({fmt_date(e)}) — {n_acts} activities.\n"
section7 += "\n"

# Section 8: Leadership — pulled from DB
leadership_keywords = ["President", "Secretary", "Vice President", "Project Manager", "Founding CEO"]
leadership_exps = [e for e in exps.values()
                   if any(k in e['title'] for k in leadership_keywords)]
leadership_exps = sorted(leadership_exps, key=lambda e: e['startDate'], reverse=True)

section8 = "## 8. Leadership & Mentorship\n\nConsolidated cross-reference (full detail in Section 3):\n"
for e in leadership_exps:
    n_acts = len(acts_by_exp[e['id']])
    section8 += f"- **{e['organization'].strip()} — {e['title']}** ({fmt_date(e)}) — {n_acts} activities.\n"
section8 += "\n"

# Section 9: Licences from DB + skills taxonomy from tags
licence_exps = [e for e in exps.values() if e['role'] == "Aviation"]
licence_exps = sorted(licence_exps, key=lambda e: e['startDate'])

section9 = "## 9. Licences, Certifications & Full Technical Skills Taxonomy\n\n**Licences (from dev.db):**\n"
for e in licence_exps:
    for a in acts_by_exp[e['id']]:
        if a['result']:
            section9 += f"- {a['result']}\n"
section9 += "\n**Full Technical Skills Taxonomy:** see Section 2 (Core Competencies) for the complete tag list.\n\n"

# Section 4 — cross-reference note
section4 = """## 4. Complete Engineering & R&D Projects (All 40 Projects)

*All 40 projects are compiled in full in Section 3 above, nested under their parent Experience. No project is extracted separately here to avoid duplication. Cross-reference Section 3 by organization for the complete project inventory.*

**R&D-flagged projects (isRnD = true):** flagged individually per project block as `R&D Project: Yes`.

"""

footer = f"\n---\n\n*End of Master Content Pool — Phase 6C. Total: 20 Experiences | 40 Projects | 163 Activities | 100% database coverage, zero pruning.*\n"

# Write final file
output = (
    STATIC_HEADER +
    section2 +
    section3 +
    "---\n\n" +
    section4 +
    "---\n\n" +
    section5 +
    "---\n\n" +
    section6 +
    "---\n\n" +
    section7 +
    "---\n\n" +
    section8 +
    "---\n\n" +
    section9 +
    footer
)

with open('/home/claude/work/MASTER-CONTENT-POOL-GENERATED.md', 'w') as f:
    f.write(output)

print(f"Done. Total activities written: {total_acts}")
print(f"File size: {len(output):,} chars")
