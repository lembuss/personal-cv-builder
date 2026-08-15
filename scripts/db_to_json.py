"""
db_to_json.py — Career Database -> Structured multitrack CV JSON

Generates data/json/mastercv_multitrack.json DIRECTLY from career-db/server/prisma/dev.db.

This intentionally does NOT read data/markdown/master-content-pool.md. That file remains
useful as a human-readable, reviewable snapshot of the database (produced separately by
db_to_markdown.py), but parsing it back apart to rebuild structured JSON would mean
re-deriving information (tags, isRnD flags, project/activity boundaries) that is already
sitting as clean columns in dev.db. Both scripts are siblings that each read the database
directly.

REQUIRED INPUT FILES
---------------------
1. dev.db
   The career database (SQLite). Path resolved via CV_DB_PATH env var, defaulting to
   ../dev.db relative to this script (career-db/server/prisma/dev.db in the real repo).

2. scripts/config/tag_track_map.json
   Maps every Tag.name in the database to one or more of the 4 CV tracks
   (aircraft_systems_aerospace_engineering, venture_building_entrepreneurial_leadership,
   deep_tech_research_computational_capability, teaching_mentorship_academic_service).
   This is the ONLY source of track information — dev.db has no track concept at all.
   Path via CV_TAG_TRACK_MAP_PATH.

3. scripts/config/static_config.json
   Everything that has no source-of-truth column in dev.db at all: document title,
   contact info, profile summary, track labels, core_competencies, publications,
   certifications (manual pending a future Certification table — see note below),
   languages, the build block, and small per-degree "education_overrides"
   (status/focus text for education entries, keyed by Experience.title).
   Path via CV_STATIC_CONFIG_PATH.

OUTPUT
------
data/json/mastercv_generated_multitrack.json (path via CV_JSON_OUTPUT_PATH)

KEY DESIGN DECISIONS (agreed in discussion before this script was written)
----------------------------------------------------------------------
- Tracks: computed per Project as the union of tags on the Project (ProjectTag) and all
  its child Activities (ActivityTag), each resolved through tag_track_map.json. An
  Experience's tracks = union of all tags reachable under it (its Projects' tags +
  ActivityTag on every Activity belonging to it, project-linked or not). This is a
  spreading/union operation, not an average — one tagged activity buried in a project
  is enough to add a track to the whole project.

- Section routing by Experience.type:
    Academic         -> education[]
    Teaching         -> teaching[]
    Other            -> not routed here at all (certifications[] is manual, static_config)
    Leadership        -> experiences[] if it has >=1 Project row, else leadership[]
    Professional /
    StudentProject   -> experiences[]

- experiences[].summary / education[].summary / teaching[].details / leadership[].details
  are ALL simply Experience.description, verbatim. No condensing, no rewriting.

- experiences[].type = Experience.role, verbatim (matches the one precedent in the old
  reference file: Kipepeo Aerospace's "type": "Startup" is exactly its `role` column).

- Projects become experiences[].projects[] entries in the normal case. If an Experience
  that routes to experiences[] has ZERO real Project rows (e.g. Jasiri Fellow), its
  orphan Activities are wrapped into ONE synthesized pseudo-project named after the
  Experience's own title, so the output shape stays valid. If an Experience DOES have
  real Projects, any activities left over with no projectId are DROPPED from bullets
  (a warning is printed listing what was dropped) rather than silently guessed at —
  this matches the reference file's behaviour (e.g. Kendrone's stray "KCAA Instructor
  Rating" activity isn't a project bullet anywhere; it's a certifications-list item,
  handled manually in static_config.json).

- Project/experience "(R&D)" suffix: appended to the name whenever Project.isRnD is true.

- additional_research_projects[]: Projects belonging to Academic/Other-type Experiences.
  ids are auto-slugified from institution + project name — these will NOT match the old
  hand-picked slugs (e.g. "metu-piezo-sensor") exactly in every case, but will be stable
  and unique across repeated runs.

- additional_research_projects[].dates: Project has NO date columns in the schema at all.
  ASSUMPTION: falls back to the parent Experience's year span (single year if the
  Experience itself started and ended in the same year, else "YYYY - YYYY" / "YYYY -
  Present"). Flag this to Brian if a project needs its own distinct date.

KNOWN GAP — Certifications
---------------------------
There is no Certification/Licence table in dev.db. The old reference JSON's
certifications[] entries were hand-extracted from free-text Activity/Experience
description fields (e.g. one Skylink PPL paragraph -> 3 separate licence lines). This
is not reconstructable as a mechanical field mapping. Per agreement: certifications[] is
pulled verbatim from data/config/static_config.json (manual, hand-maintained) until a
proper Certification table is added to the career DB in a future revision.
"""

import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.environ.get('CV_DB_PATH') or os.path.join(SCRIPT_DIR, '../career-db/server/prisma/dev.db')
TAG_TRACK_MAP_PATH = os.environ.get('CV_TAG_TRACK_MAP_PATH') or os.path.join(SCRIPT_DIR, 'config/tag_track_map.json')
STATIC_CONFIG_PATH = os.environ.get('CV_STATIC_CONFIG_PATH') or os.path.join(SCRIPT_DIR, 'config/static_config.json')
OUTPUT_PATH = os.environ.get('CV_JSON_OUTPUT_PATH') or os.path.join(SCRIPT_DIR, '../data/json/mastercv_generated_multitrack.json')

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)


# ---------------------------------------------------------------------------
# Load database
# ---------------------------------------------------------------------------
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

exps = {r['id']: dict(r) for r in cur.execute('SELECT * FROM Experience')}
projs = {r['id']: dict(r) for r in cur.execute('SELECT * FROM Project')}
acts = [dict(r) for r in cur.execute('SELECT * FROM Activity')]
tags = {r['id']: dict(r) for r in cur.execute('SELECT * FROM Tag')}

act_tags = defaultdict(list)     # activityId -> [tagName, ...]
for r in cur.execute('SELECT * FROM ActivityTag'):
    act_tags[r['activityId']].append(tags[r['tagId']]['name'])

proj_tags = defaultdict(list)    # projectId -> [tagName, ...]
for r in cur.execute('SELECT * FROM ProjectTag'):
    proj_tags[r['projectId']].append(tags[r['tagId']]['name'])

acts_by_exp = defaultdict(list)  # experienceId -> [activity, ...] (ALL activities, incl. project-linked)
for a in acts:
    acts_by_exp[a['experienceId']].append(a)

projs_by_exp = defaultdict(list)  # experienceId -> [project, ...]
for p in projs.values():
    projs_by_exp[p['experienceId']].append(p)

acts_by_proj = defaultdict(list)  # projectId -> [activity, ...]
for a in acts:
    if a['projectId']:
        acts_by_proj[a['projectId']].append(a)

# ---------------------------------------------------------------------------
# Load config
# ---------------------------------------------------------------------------
with open(TAG_TRACK_MAP_PATH) as f:
    tag_track_map = json.load(f)

TRACK_CODES = tag_track_map['_tracks']          # short code -> full track key
TAG_MAP = tag_track_map['map']                  # tag name -> [short codes]

with open(STATIC_CONFIG_PATH) as f:
    static_config = json.load(f)

ALL_TRACK_KEYS = list(TRACK_CODES.values())
UNMAPPED_TAGS_SEEN = set()


def resolve_tags_to_tracks(tag_names):
    """Resolve a collection of tag names to a sorted list of full track keys."""
    result = set()
    for name in tag_names:
        codes = TAG_MAP.get(name)
        if codes is None:
            UNMAPPED_TAGS_SEEN.add(name)
            continue
        for code in codes:
            result.add(TRACK_CODES[code])
    # Keep output in the canonical track_order for readability
    order = static_config.get('build', {}).get('track_order', ALL_TRACK_KEYS)
    return [t for t in order if t in result] or sorted(result)


def project_tags(project_id):
    """All tag names reachable from a Project: its own tags + all its Activities' tags."""
    names = set(proj_tags.get(project_id, []))
    for a in acts_by_proj.get(project_id, []):
        names.update(act_tags.get(a['id'], []))
    return names


def experience_tags(experience_id):
    """All tag names reachable from an Experience: its Projects' tags + all its Activities' tags."""
    names = set()
    for p in projs_by_exp.get(experience_id, []):
        names.update(project_tags(p['id']))
    for a in acts_by_exp.get(experience_id, []):
        names.update(act_tags.get(a['id'], []))
    return names


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------
def fmt_dates(e):
    """'Oct 2024 - Present' style, matching the reference file's experience/education/
    teaching/leadership date format."""
    start = datetime.strptime(e['startDate'][:10], '%Y-%m-%d').strftime('%b %Y') if e['startDate'] else '?'
    if e['current']:
        end = 'Present'
    elif e['endDate']:
        end = datetime.strptime(e['endDate'][:10], '%Y-%m-%d').strftime('%b %Y')
    else:
        end = '?'
    return f"{start} \u2013 {end}"


def fmt_year_span(e):
    """Year-only span for additional_research_projects, since Project has no date columns
    of its own. ASSUMPTION: falls back to the parent Experience's year range."""
    start_year = e['startDate'][:4] if e['startDate'] else '?'
    if e['current']:
        end_year = 'Present'
    elif e['endDate']:
        end_year = e['endDate'][:4]
    else:
        end_year = start_year
    return start_year if start_year == end_year else f"{start_year} \u2013 {end_year}"


def rnd_name(p):
    return f"{p['name'].strip()} (R&D)" if p['isRnD'] else p['name'].strip()


_slug_re = re.compile(r'[^a-z0-9]+')

# Small, hand-maintained abbreviation lookup so slugs read like "tum-..." / "metu-..."
# instead of "technical-..." / "middle-...". Add to this as new institutions appear.
INSTITUTION_ABBREV = {
    'technical university of munich': 'tum',
    'middle east technical university': 'metu',
    'university of cologne': 'cologne',
    'emobilis technology institute': 'emobilis',
}


def slugify(*parts, max_words=None):
    text = ' '.join(p for p in parts if p).lower().strip()
    text = INSTITUTION_ABBREV.get(text, text)
    if max_words:
        text = ' '.join(text.split()[:max_words])
    slug = _slug_re.sub('-', text).strip('-')
    return slug


def dedupe_id(base, used):
    slug = base
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


# Ordering matching db_to_markdown.py: current experiences first (by startDate DESC),
# then closed ones by endDate DESC. Python's sort is stable, so stack ascending sorts
# from least- to most-significant key.
ordered_exp_ids = list(exps.keys())
ordered_exp_ids.sort(key=lambda eid: exps[eid]['startDate'], reverse=True)
ordered_exp_ids.sort(key=lambda eid: (exps[eid]['endDate'] or '9999'), reverse=True)
ordered_exp_ids.sort(key=lambda eid: exps[eid]['current'], reverse=True)


# ---------------------------------------------------------------------------
# Build experiences[] / additional_research_projects[] / education[] /
# teaching[] / leadership[]
# ---------------------------------------------------------------------------
experiences_out = []
research_projects_out = []
education_out = []
teaching_out = []
leadership_out = []

used_exp_ids = set()
used_research_ids = set()

for eid in ordered_exp_ids:
    e = exps[eid]
    etype = e['type']
    own_projects = sorted(projs_by_exp.get(eid, []), key=lambda p: p['createdAt'])
    orphan_acts = [a for a in acts_by_exp.get(eid, []) if not a['projectId']]

    if etype == 'Other':
        # Not routed anywhere structurally. Certifications derived from these rows are
        # handled manually in static_config.json (see module docstring).
        continue

    if etype == 'Academic':
        override = static_config.get('education_overrides', {}).get(e['title'], {})
        education_out.append({
            'institution': e['organization'].strip(),
            'location': e['location'],
            'degree': e['title'],
            'dates': fmt_dates(e),
            'summary': e['description'],
            **({'status': override['status']} if 'status' in override else {}),
            **({'focus': override['focus']} if override.get('focus') else {}),
            'tracks': resolve_tags_to_tracks(experience_tags(eid)),
        })
        for p in own_projects:
            rid = dedupe_id(slugify(e['organization'], max_words=1) + '-' + slugify(p['name'], max_words=3), used_research_ids)
            research_projects_out.append({
                'id': rid,
                'name': rnd_name(p),
                'institution': e['organization'].strip(),
                'dates': fmt_year_span(e),
                'tracks': resolve_tags_to_tracks(project_tags(p['id'])),
                'bullets': [a['what'] for a in sorted(acts_by_proj.get(p['id'], []), key=lambda a: a['createdAt'])],
            })
        if orphan_acts:
            warn(f"Academic experience '{e['title']}' has {len(orphan_acts)} activity(ies) not "
                 f"attached to any Project — dropped from additional_research_projects: "
                 + '; '.join(a['what'][:60] for a in orphan_acts))
        continue

    if etype == 'Teaching':
        teaching_out.append({
            'role': e['title'],
            'institution': e['organization'].strip(),
            'location': e['location'],
            'dates': fmt_dates(e),
            'details': e['description'],
            'tracks': resolve_tags_to_tracks(experience_tags(eid)),
        })
        continue

    if etype == 'Leadership' and not own_projects:
        leadership_out.append({
            'role': e['title'],
            'organisation': e['organization'].strip(),
            'dates': fmt_dates(e),
            'details': e['description'],
            'tracks': resolve_tags_to_tracks(experience_tags(eid)),
        })
        continue

    # Everything else (Professional, StudentProject, and Leadership-with-a-Project)
    # routes to experiences[]
    if own_projects:
        proj_blocks = [{
            'name': rnd_name(p),
            'tracks': resolve_tags_to_tracks(project_tags(p['id'])),
            'bullets': [a['what'] for a in sorted(acts_by_proj.get(p['id'], []), key=lambda a: a['createdAt'])],
        } for p in own_projects]
        if orphan_acts:
            warn(f"Experience '{e['organization'].strip()} \u2014 {e['title']}' has "
                 f"{len(orphan_acts)} activity(ies) not attached to any Project — dropped "
                 f"from experiences[] bullets (check if any belong in certifications): "
                 + '; '.join(a['what'][:60] for a in orphan_acts))
    else:
        # No real Project rows at all -> synthesize one pseudo-project so the shape stays
        # valid, wrapping every activity under this experience.
        all_acts_sorted = sorted(acts_by_exp.get(eid, []), key=lambda a: a['createdAt'])
        proj_blocks = [{
            'name': e['title'],
            'tracks': resolve_tags_to_tracks(experience_tags(eid)),
            'bullets': [a['what'] for a in all_acts_sorted],
        }]

    exp_id = dedupe_id(slugify(e['organization'], max_words=2), used_exp_ids)
    experiences_out.append({
        'id': exp_id,
        'company': e['organization'].strip(),
        'role': e['title'],
        'location': e['location'],
        'type': e['role'],
        'dates': fmt_dates(e),
        'summary': e['description'],
        'tracks': resolve_tags_to_tracks(experience_tags(eid)),
        'projects': proj_blocks,
    })

# ---------------------------------------------------------------------------
# Assemble final document
# ---------------------------------------------------------------------------
document = {
    'title': static_config['title'],
    'contact': static_config['contact'],
    'profile': static_config['profile'],
    'tracks': static_config['tracks'],
    'core_competencies': static_config['core_competencies'],
    'experiences': experiences_out,
    'additional_research_projects': research_projects_out,
    'education': education_out,
    'publications': static_config['publications'],
    'teaching': teaching_out,
    'leadership': leadership_out,
    'certifications': static_config['certifications'],
    'languages': static_config['languages'],
}

output = {
    'version': static_config.get('version', '2.0'),
    'document': document,
    'build': static_config['build'],
}

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
print(f"Done. Wrote {OUTPUT_PATH}")
print(f"  experiences: {len(experiences_out)}")
print(f"  additional_research_projects: {len(research_projects_out)}")
print(f"  education: {len(education_out)}")
print(f"  teaching: {len(teaching_out)}")
print(f"  leadership: {len(leadership_out)}")

if UNMAPPED_TAGS_SEEN:
    print(f"\nWARNING: {len(UNMAPPED_TAGS_SEEN)} tag(s) used in the DB have no entry in "
          f"tag_track_map.json (they contributed no track):")
    for t in sorted(UNMAPPED_TAGS_SEEN):
        print(f"  - {t!r}")

if WARNINGS:
    print(f"\n{len(WARNINGS)} data warning(s):")
    for w in WARNINGS:
        print(f"  - {w}")