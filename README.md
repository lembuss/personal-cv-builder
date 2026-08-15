# Personal CV Builder

A data-driven CV generation system that builds tailored CV variants from a structured master career content pool.

## Architecture

The CV builder uses the personal career experience database as its source of career information.

```text
Career Database
      │
      │ Git submodule
      ▼
career-db/server/prisma/dev.db
      │
      ▼
db_to_markdown.py
      │
      ▼
data/master-content-pool.md
      │
      ▼
markdown_to_json.py
      │
      ▼
data/mastercv_multitrack.json
      │
      ▼
Existing CV build system
      │
      ▼
output/
```

## Repository Structure

```text
cv-builder/
│
├── career-db/                       # Career database Git submodule
│   └── server/prisma/dev.db
│
├── data/
│   ├── json
│   |   ├── mastercv.json               # json test file
|   |   └── mastercv_multitrack.json    # Structured CV data
│   └── markdown 
│       ├── master-content-pool.md      # Master CV content pool
│       ├── master-cv-content.md        # md test file                 
|       └── master-cv-multitrack.md     # Master CV in markdown - need a generation script for this
│
├── docs/
│   ├── blueprints/                     # blueprints
│   ├── conceptual-outline/             # conceptual outline
│   ├── content-selection/              # content-selection
│   ├── evidence-maps/                  # Evidence and experience
│   └── roadmaps/                       # Project handover and roadmap documents
│
├── scripts/
│   ├── db_to_markdown.py            # Database → Markdown
│   ├── markdown_to_json.py          # Markdown → JSON
│   └── build_cvs.py                 # CV generation
│
├── templates/                       # CV templates
├── output/                          # Generated CV files
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

The Career DB repository is the source of truth for career experiences, skills, projects, education, and other structured career information.

### 2. Master Content Pool

`db_to_markdown.py` reads the career database and generates:

```text
data/master-cv-content-pool.md
```

The Master Content Pool is intended to be human-readable and editable. It provides the complete pool of career information from which tailored CVs can be produced.

### 3. Structured CV Data

`markdown_to_json.py` converts the Master Content Pool into:

```text
data/mastercv_multitrack.json
```

This provides the structured representation consumed by the CV generation system.

### 4. CV Generation

The existing build system uses the structured CV data and templates to generate individual CV variants.

Generated files are placed in:

```text
output/
```

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

The repository is currently being developed as a staged pipeline. The database-to-Markdown generator, Markdown-to-JSON conversion, and final CV build process are maintained as separate stages so each transformation can be tested independently.

## Generated Files

The following are generated artifacts:

* `data/master-cv-content-pool.md`
* `data/mastercv_multitrack.json`
* Files under `output/`

The Master Content Pool and JSON representation are version-controlled because they form part of the project's content pipeline and provide reproducible inputs to CV generation.

## Status

The repository is under active development.
