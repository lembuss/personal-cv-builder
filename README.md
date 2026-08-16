# Personal CV Builder

A data-driven CV generation system that builds tailored CV variants from a structured master career content pool.

## Architecture

The CV builder uses the personal career experience database as its source of career information. `db_to_markdown.py` and `db_to_json.py` are independent siblings that both read `dev.db` directly — the Markdown file is a human-readable snapshot for review, not an intermediate the JSON is built from.

```text
Career Database
      │
      │ Git submodule
      ▼
career-db/server/prisma/dev.db
      │
      ├─────────────────────────────┐
      ▼                              ▼
db_to_markdown.py               db_to_json.py  ◄── scripts/config/tag_track_map.json
      │                              │           ◄── scripts/config/static_config.json
      ▼                              ▼
data/markdown/                  data/json/
master-content-pool.md          mastercv_generated_multitrack.json
(human-readable review copy)          │
                                       ▼
                                  build_cv.py
                                       │
                                       ▼
                                    output/
                            Brian_Lembuss_CV_*.pdf
```

## Repository Structure

```text
cv-builder/
│
├── career-db/                       # Career database Git submodule
│   └── server/prisma/dev.db
│
├── scripts/
│   ├── config/
│   │   ├── tag_track_map.json       # Tag.name -> CV track lookup (only source of track info; not in the DB)
│   │   └── static_config.json       # Content with no source-of-truth column in dev.db:
│   │                                 #   title, contact, profile, core_competencies, publications,
│   │                                 #   certifications (manual pending a future Certification table),
│   │                                 #   languages, build block, education_overrides
│   ├── db_to_markdown.py            # Database -> Markdown (human-readable review copy)
│   ├── db_to_json.py                # Database -> Structured JSON (build_cv.py's input)
│   └── build_cv.py                  # JSON -> tailored/master CV PDFs
│
├── data/
│   ├── json/
│   │   └── mastercv_generated_multitrack.json  # Structured CV data (generated)
│   └── markdown/
│       └── master-content-pool.md              # Master CV content pool (generated)
│
├── docs/
│   ├── blueprints/                     # blueprints
│   ├── conceptual-outline/             # conceptual outline
│   ├── content-selection/              # content-selection
│   ├── evidence-maps/                  # Evidence and experience
│   └── roadmaps/                       # Project handover and roadmap documents
│
├── templates/                       # CV templates
├── output/                          # Generated CV PDFs (Brian_Lembuss_CV_*.pdf)
├── .gitignore
├── .gitmodules
└── README.md
```

## Data Pipeline

### 1. Career Database

The `career-db` directory is a Git submodule pointing to the personal career experience database.

The database is currently:

```text
career-db/server/prisma/dev.db
```

The Career DB repository is the source of truth for career experiences, skills, projects, education, and other structured career information. It has no concept of "tracks" (the 4 CV pillars) or of certifications/licences — both are supplied separately (see below).

### 2. Master Content Pool (Markdown)

`db_to_markdown.py` reads the career database and generates:

```text
data/markdown/master-content-pool.md
```

This is a human-readable, reviewable snapshot of everything in the database — useful for spotting data-entry issues at a glance. It is not read by any downstream script.

### 3. Structured CV Data (JSON)

`db_to_json.py` reads the career database directly and generates:

```text
data/json/mastercv_generated_multitrack.json
```

This is the structured representation `build_cv.py` consumes. Besides the database, it needs two hand-maintained config files:

- `scripts/config/tag_track_map.json` — maps every `Tag.name` to one or more of the 4 CV tracks. This is the *only* place track information lives; edit it whenever a new tag is added to the database.
- `scripts/config/static_config.json` — everything with no source-of-truth column in `dev.db` at all (contact info, profile text, publications, certifications, languages, per-degree education status/focus overrides).

Paths for the database, both config files, and the output JSON can all be overridden with environment variables (`CV_DB_PATH`, `CV_TAG_TRACK_MAP_PATH`, `CV_STATIC_CONFIG_PATH`, `CV_JSON_OUTPUT_PATH`) — see the script's docstring for details and for the routing/track-assignment rules it follows.

### 4. CV Generation

`build_cv.py` reads the structured JSON and a chosen track, and writes a clean, single-column ATS-safe PDF to `output/`:

```bash
python3 scripts/build_cv.py          # Master CV — all content, no filtering
python3 scripts/build_cv.py A        # Track A: Aircraft Systems & Aerospace Engineering
python3 scripts/build_cv.py B        # Track B: Venture Building & Entrepreneurial Leadership
python3 scripts/build_cv.py C        # Track C: Deep-Tech Research & Computational Capability
python3 scripts/build_cv.py D        # Track D: Teaching, Mentorship & Academic Service
```

Input/output paths can be overridden with `CV_JSON_PATH` and `CV_OUTPUT_DIR`; by default they resolve relative to the script's own location, so the commands above work from any working directory.

## Career Database Submodule

The Career DB is included as a Git submodule rather than duplicated inside this repository.

The CV builder uses the `main` branch of the Career DB as its source.

When setting up the repository on a new machine, clone the repository with its submodules:

```bash
git clone --recurse-submodules <cv-builder-repository-url>
```

If the CV builder repository has already been cloned without submodules:

```bash
git submodule update --init --recursive
```

The generation workflow will update the Career DB submodule to the latest `main` revision before generating the content pool.

## Python Environment

The project uses Python for its data transformation and CV generation scripts.

Create a local virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

The virtual environment itself is intentionally excluded from Git.

## Development

The repository is currently being developed as a staged pipeline. The database-to-Markdown generator, database-to-JSON converter, and final CV build process are maintained as separate stages so each transformation can be tested independently.

## Generated Files

The following are generated artifacts:

* `data/markdown/master-content-pool.md`
* `data/json/mastercv_generated_multitrack.json`
* `output/Brian_Lembuss_CV_*.pdf`

The Master Content Pool and JSON representation are version-controlled because they form part of the project's content pipeline and provide reproducible inputs to CV generation.

## Status

The repository is under active development.