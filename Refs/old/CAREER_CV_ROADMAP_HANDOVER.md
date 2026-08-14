# CAREER CV ROADMAP — CHAT HANDOVER

## 1. Purpose of this handover

This document is the working handover for continuing the career/CV development project in a new chat.

The overall goal is to build a **comprehensive, evidence-backed Master CV system** from Brian's career database, then use that Master CV/evidence base to produce targeted CVs for:

- aircraft systems engineering
- aerospace industry
- UAS/eVTOL/advanced air mobility
- R&D / deep-tech engineering
- research roles
- academia / teaching
- scholarships and completion of the MSc at TUM

The immediate objective is **not** to write another generic CV. The work is being done as a structured pipeline so that the career evidence is captured once and can subsequently be tailored without repeatedly reconstructing Brian's career.

---

# 2. Source of truth

The principal source of truth is the structured career database:

**`dev.db`**

The database contains structured:

- Experiences
- Projects
- Activities
- associated contextual fields/tags/evidence

The database was deliberately built as a career evidence repository rather than as a CV.

Important operating principle:

> **Do not invent, embellish, reinterpret, or add career facts merely because they would make a CV sound better.**

The database is Brian's career. The task is to represent it accurately and strategically.

Brian has explicitly stated that the career database already contains the substantive experience information he wants captured. Do not repeatedly ask him to reconstruct experiences that are already documented.

---

# 3. Professional positioning established during the roadmap

The intended professional identity is broadly:

**Aircraft Systems Engineer / Aerospace Engineer with end-to-end aircraft and UAS systems lifecycle experience, spanning requirements, architecture, allocation, hardware/software integration, testing, verification, validation and deployment, with substantial R&D/deep-tech exposure.**

Important context:

- Brian works across the hardware/software boundary.
- His aircraft-systems experience includes manned aircraft systems.
- His UAS experience can encompass complete unmanned aircraft systems.
- A significant portion of the career has been R&D-oriented.
- Amazilia, HORYZN and Kipepeo involved exploration/development of new concepts.
- His BSc and MSc education provide substantial deep-tech engineering/research background.
- Brian has an incomplete MSc at TUM. He completed 73 ECTS and still intends to complete the degree.
- The TUM degree must **never be represented as completed**.
- Brian is currently in Kenya but is willing to apply across Europe.
- A job is considered the faster practical route to funding while scholarship applications for MSc completion progress.

The Master CV therefore needs to be credible for both industry and technically sophisticated R&D environments without becoming an academic CV.

---

# 4. Master CV philosophy

The Master CV is **not** intended to contain every career activity with equal prominence.

Its purpose is to be the comprehensive professional source from which targeted CVs can be generated.

The important distinction established during the work is:

> **Important career evidence ≠ Master CV evidence ≠ individual CV bullet.**

An activity may be important and remain in the database without deserving a bullet in the Master CV.

Likewise, a project may be CORE while only a handful of its activities should survive into actual CV writing.

The Master CV should therefore:

- prioritise strong aircraft/UAS systems evidence
- preserve R&D/deep-tech evidence
- demonstrate end-to-end systems lifecycle capability
- show genuine hardware/software integration
- retain verification/testing evidence
- preserve applied research evidence
- avoid drowning the technical narrative in generic business/administrative activity
- retain reserve evidence for later targeted variants

---

# 5. Roadmap completed so far

The project followed a phased roadmap.

## Phase 1–4

These phases established and organised the career evidence/database and the overall CV strategy.

The career database was developed so that experiences contain projects and projects contain activities, with sufficient contextual/evidence fields to allow later traceability.

## Phase 5 — Competency / positioning work

Phase 5 produced the competency mapping and positioning layer.

Important correction made during Phase 5:

There is **one competency table** in the competency map. Earlier discussion mistakenly referred to multiple sections/tables; that was corrected.

The competency map is intended to show what the career evidence actually demonstrates, rather than inventing a skills inventory.

A narrative prose document was also considered, but it was not regarded as particularly strong compared with the structured competency/evidence approach.

Phase 5 is considered sufficiently complete for the current workflow.

---

# 6. Phase 6 architecture

Phase 6 is the transition from career evidence to the actual Master CV.

The agreed conceptual flow is:

**Career Database**
→ **6A Evidence Map**
→ **6B Content Selection / Professional Judgement**
→ **6C Master CV**

Later 6D–6F phases can then support refinement/tailoring and downstream CV variants.

The critical distinction:

### 6A asks:
**What evidence exists and where does it come from?**

### 6B asks:
**What deserves space in the Master CV and how should it be represented?**

### 6C asks:
**How do we actually write the Master CV?**

Do not collapse these phases.

---

# 7. Phase 6A — Evidence Map

An initial evidence map was generated from the database.

The first version was criticised because it was essentially too close to an extraction of the database rather than a genuinely useful evidence-selection layer.

The lesson from that exercise:

> An evidence map should not simply reproduce the database in another format.

The database remains the detailed source of truth.

The 6A output is useful for traceability and mapping evidence to competencies/CV destinations, but should not become a second career database.

---

# 8. Phase 6B — Professional judgement

The first 6B document was:

**`MASTER-CV-CONTENT-SELECTION.md`**

It was critically reviewed and rejected.

Problems identified:

1. The experience-level section repeated generic descriptions instead of making real CV architecture decisions.
2. A numerical scoring system was used to classify evidence.
3. The scoring system over-promoted activities based on tags.
4. Too many activities were classified CORE.
5. The scoring could promote technically irrelevant activities simply because they contained broad tags.
6. The document confused:
   - importance of evidence
   - Master CV relevance
   - whether something deserved an actual CV bullet
7. It was too close to a database dump with labels attached.
8. It did not exercise sufficiently careful professional judgement against the actual evidence.

This document should **not** be treated as the final 6B output.

---

# 9. Phase 6B V2

A substantially revised document was then generated:

**`MASTER-CV-CONTENT-SELECTION-V2.md`**

This is currently the working 6B document.

It was rebuilt around qualitative professional judgement rather than an automated numerical score.

The decision labels are:

- **CORE** — should be represented in the Master CV.
- **SUPPORTING** — useful evidence, but secondary or partly redundant.
- **RESERVE** — retain for targeted CVs, but do not spend Master CV space on it by default.

A RESERVE item is **not unimportant**. It simply does not earn scarce space in this particular Master CV.

---

# 10. What V2 actually does

The revised 6B document contains:

### A. Experience-level CV treatment

Instead of simply saying an experience is "important", it determines how that database experience should appear in the written CV.

Examples of decisions:

- METU student records should not become multiple employment-style entries.
- HORYZN's separate database Experience records should be represented coherently in the written CV rather than duplicated simply because the database has multiple records.
- TUM's degree record should be distinct from the technical/research project evidence.
- Kendrone's substantive UAS employment should be distinguished from the separate licensing/training record.
- Kipepeo should foreground technical engineering/R&D rather than venture administration.

### B. Project-level selection

Each project receives a deliberate:

**CORE / SUPPORTING / RESERVE**

decision plus a specific rationale.

### C. Activity-level selection

Only selected activities are carried forward as evidence for the writing stage.

This is deliberately much smaller than the database.

A CORE project does **not** mean every activity in that project becomes a CV bullet.

### D. Master CV evidence interpretation

The document identifies the strongest evidence themes:

- aircraft/UAS systems engineering
- end-to-end systems lifecycle
- hardware/software integration
- systems architecture
- interfaces
- HIL
- verification/testing
- R&D
- UAM/eVTOL
- autonomous UAS
- applied research

### E. Evidence deliberately not promoted

Examples include:

- broad Kipepeo governance/incorporation/fundraising/investor-readiness work
- general venture/business activities where engineering evidence is already stronger elsewhere
- general IT/marketing/company operations
- peripheral student/software work
- most specialist undergraduate projects where stronger aircraft evidence exists
- university society leadership for the aircraft-systems Master CV
- general teaching/examining evidence unless strategically useful
- peripheral research unrelated to the core positioning

These remain in the database.

They are not deleted or considered worthless.

---

# 11. Current 6B writing pool

The V2 document identifies these as particularly important evidence sources for 6C.

## Highest-priority professional experiences

1. Kipepeo Aerospace
2. Amazilia Aerospace
3. HORYZN
4. TUM
5. Kendrone
6. University of Cologne

## Highest-priority project evidence

- Aircraft Systems HIL Test Rig
- Aircraft Battery Charging Unit (ABCU)
- WfA MiniFreighter GCS
- Kolibri eVTOL Systems Integration / Flight Testing
- Kolibri Aerodynamics Module
- TAI UAS
- Kilimo Anga Quadrotor / AngaCam
- AngaStack V2
- Linda Nchi / K-DEMO-2.5
- Generic Modeling of Slotneutral UAM Throughput
- ACMU Embedded Software
- Autonomous Sub-Terrain UAV
- Kendrone Seedball Dispersal UAS
- Kendrone UAS Avionics / Payload Integration
- University of Cologne MBSE Agricultural UAS

Secondary evidence includes:

- Amazilia Ground Control Station
- AngaStack V1
- Kendrone Aerial Mapping
- Kendrone UAS Pilot Training
- METU Numerical Methods
- selected METU fixed-wing/VTOL design projects

These selections remain open to interrogation before 6C.

---

# 12. Specific evidence themes to preserve

The following are especially important because they differentiate Brian's profile.

## End-to-end systems lifecycle

The career evidence supports work across:

**requirements → architecture → allocation/interfaces → design/build → integration → testing → verification/validation → deployment/handover**

Do not turn this into an unsupported generic claim. Individual CV claims must be traceable to the actual database evidence.

## Hardware/software boundary

Important documented evidence includes:

- aircraft-system interfaces
- CAN/Ethernet integration
- HIL
- avionics integration
- embedded C++
- electrical/power/flight-control architecture
- software/cloud systems
- deployed aerial intelligence platforms

This should be a genuine differentiator in the Master CV.

## R&D

R&D is not a decorative section.

It is embedded throughout the career:

- eVTOL development
- UAM modelling
- embedded aircraft systems
- autonomous UAS perception
- MBSE
- hybrid-VTOL development
- aerial-intelligence systems

## Academic/research

Important research evidence includes:

- UAM throughput/approach modelling
- ACMU embedded aircraft systems work
- autonomous UAS work
- University of Cologne MBSE/UAS work
- selected METU engineering projects

Teaching/academic assistantship remains useful for academic/scholarship variants.

---

# 13. Important decisions already made

## Europass

The earlier discussion established that Europass should not be the default Master CV format.

The objective is a professionally controlled Master CV rather than forcing the entire career into the Europass structure.

## Career database

The database should **not be bloated** simply to make it conform to a CV.

Incompleteness itself is not an "activity".

The database's job is to capture real career evidence.

## Aerospace Society

A decision was made to add Aerospace Society as its own Experience with the relevant work represented as a Project and Activities, rather than forcing it into another experience.

This addition was based on older CV/material review.

## University leadership

Brian deliberately omitted university leadership roles from the main aircraft-systems competency story because they do not stand out strongly enough for that professional positioning.

They remain potentially useful for academic/leadership variants.

---

# 14. Working rules for the next chat

These are important.

### Do NOT:

- repeatedly re-read the entire database unnecessarily
- ask Brian to restate experiences already documented
- invent new career facts
- add fields that do not exist in the database
- create activities simply because a CV would benefit from them
- reinterpret the career to fit an imagined ideal candidate
- replace Brian's terminology with generic consultant language
- turn every database activity into a CV bullet
- use arbitrary scoring systems to determine professional importance
- repeat changes that have already been acknowledged as completed

### DO:

- use the database as the source of truth
- preserve its terminology and factual depth
- make concrete, actionable decisions
- distinguish database evidence from CV presentation
- explain why a particular item is selected or not selected
- maintain traceability back to database records
- challenge weak reasoning rather than automatically agreeing
- avoid unnecessary fluff
- group related decisions when they are genuinely part of one issue
- be detailed when doing substantive analysis, but concise when the task is simple

Brian has explicitly asked for **functional, actionable assistance rather than vague consultancy language**.

---

# 15. Current status

### Completed / sufficiently established

- Career database
- Career evidence structure
- CV roadmap
- Phase 5 competency map
- Phase 6 architecture
- Phase 6A evidence mapping
- Phase 6B V2 professional-judgement/content-selection document

### Current position

**We are at Phase 6B.**

The current document is:

**`MASTER-CV-CONTENT-SELECTION-V2.md`**

It should now be **critically interrogated**, not blindly accepted.

The next logical step is:

1. Review the V2 selections.
2. Identify any CORE/SUPPORTING/RESERVE decisions that are factually or strategically wrong.
3. Resolve those decisions.
4. Freeze 6B.
5. Move to **6C — actual Master CV construction**.

Do not start writing the CV until the selection layer is sufficiently trusted.

---

# 16. The ultimate objective

The final system should allow Brian to maintain:

### One comprehensive career evidence database

↓

### One evidence/competency map

↓

### One professionally judged Master CV/content pool

↓

### Multiple targeted CVs

For example:

- Aircraft Systems Engineer
- Aerospace Systems / R&D Engineer
- UAS/eVTOL Engineer
- Research Engineer
- Academic / Research
- Scholarship / MSc completion
- specific European job applications

The key advantage is that future applications should require **selection and tailoring**, not repeatedly reconstructing Brian's career from scratch.

---

# 17. Immediate next task

Before proceeding to 6C:

> **Critically review `MASTER-CV-CONTENT-SELECTION-V2.md` and interrogate its actual decisions.**

The review should focus on:

- wrong project priorities
- missing genuinely important projects
- over-promoted projects
- incorrect experience-level treatment
- evidence that has been unnecessarily relegated to RESERVE
- evidence that should be SUPPORTING rather than CORE
- potential duplication between projects
- whether the proposed writing pool genuinely represents the strongest career evidence

Once these decisions are settled, 6B can be considered complete.

Then proceed directly to **6C — Master CV construction**.

---

## Final operating principle

**The database describes Brian's career.**

**6A organises the evidence.**

**6B decides what matters for the Master CV.**

**6C writes it.**

Do not reverse that order.
