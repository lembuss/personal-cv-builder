# PHASE 6B — MASTER CV CONTENT SELECTION (V3 — multi-track)

## What changed from V2

V2 made one CORE/SUPPORTING/RESERVE call per item, reasoned entirely through the aircraft-systems industry lens. That call is preserved below as the **Industry** column. V3 adds four more columns — **Entrepreneurial**, **TA/Academic**, **Scholarship**, **Further Education** — so a track-appropriate decision is visible without re-deriving it from scratch each time.

Two corrections this made necessary, not just additions:

1. The three METU leadership experiences (VP Aerospace Society, Secretary General ISA, MUN President) were labelled RESERVE in V2 as "duplicate/secondary METU student record" — the same reasoning used for genuinely duplicate academic records. That conflated *administrative duplication* with *distinct leadership evidence*. They're re-labelled below as their own Leadership category, RESERVE for Industry but CORE/SUPPORTING for TA/Academic and Further Education.
2. **Kipepeo Venture Building, Governance & Capital Strategy** and **Jasiri4Africa** were both flat RESERVE. Read against the Entrepreneurial track, this is some of the strongest evidence in the entire database — a SAFE agreement at a $1M valuation cap, a Pre-Incorporation Founders' Agreement with cap table/reverse vesting, three signed MoUs, two startup cloud-grant acceptances, and an active accelerator cohort. It had no activity-level representation anywhere in V2 because RESERVE items never reached §3. That's fixed in §3A below.

**Source of truth unchanged:** the career database (`dev.db`). No new career facts introduced — this is re-reading existing database content through four additional lenses.

### Decision labels (per track)
- **CORE** — should be represented in that track's variant.
- **SUPPORTING** — useful, secondary or partly redundant for that track.
- **RESERVE** — not needed for that track by default; stays in the database.
- **—** — not applicable / no meaningful connection to that track.

---

## 1. Experience-level CV treatment

| Experience | Industry | Entrepreneurial | TA/Academic | Scholarship | Further Ed | Notes |
|---|---|---|---|---|---|---|
| Skylink — PPL Training | CREDENTIAL | — | — | — | — | Licences section only, all tracks. |
| METU — B.Sc. (academic record) | EDUCATION | SUPPORTING | EDUCATION | EDUCATION | EDUCATION | Primary engineering education record everywhere. |
| METU — Secretary General, ISA | RESERVE | SUPPORTING | **CORE** | SUPPORTING | **CORE** | Distinct leadership evidence, not a duplicate academic record. 8-directorate org, 70+ members. |
| ALS Ltd — Internship | SUPPORTING | — | — | SUPPORTING | SUPPORTING | Early aircraft lifecycle grounding. |
| METU — VP, Aerospace Society | RESERVE | SUPPORTING | **CORE** | SUPPORTING | **CORE** | Launched student project team, ran technical training sessions — directly relevant to teaching/mentoring narrative. |
| METU — President, MUN Society | RESERVE | SUPPORTING | SUPPORTING | RESERVE | SUPPORTING | Organisational leadership/training design; weaker technical connection than the other two. |
| METU — SI-PASS Instructor | SUPPORTING | — | **CORE** | SUPPORTING | **CORE** | Certified peer instructor role — direct teaching credential. |
| METU — ASE301 TA | SUPPORTING | — | **CORE** | SUPPORTING | **CORE** | Formal TA role in the same discipline being applied to — strongest single teaching data point. |
| YSK — STEM Mentorship | RESERVE | RESERVE | **CORE** | SUPPORTING | SUPPORTING | Technical mentoring with quantified outcomes (43.6% fuel-efficiency gain). |
| eMobilis — Full Stack Dev | RESERVE | RESERVE | — | RESERVE | RESERVE | Peripheral to all five tracks; kept for completeness only. |
| Kendrone — UAS Engineer/Pilot/Instructor | **CORE** | SUPPORTING | SUPPORTING | SUPPORTING | SUPPORTING | Substantive UAS engineering; instructor component adds TA-track value. |
| Kendrone — RPL Training | CREDENTIAL | — | — | — | — | Licences section only. |
| TUM — M.Sc Aerospace | EDUCATION | — | EDUCATION | EDUCATION | EDUCATION | Degree status always factual: incomplete, 73 ECTS, thesis pending. |
| Univ. of Cologne — DAAD Scholar (LEAD!) | **CORE** | SUPPORTING | **CORE** | **CORE** | **CORE** | Scholar-funded research programme; strong across every non-industry track. |
| Amazilia Aerospace — Working Student | **CORE** | RESERVE | SUPPORTING | SUPPORTING | SUPPORTING | Strongest conventional industry evidence; limited direct scholarship/academic relevance beyond technical rigor. |
| HORYZN — Aerodynamics Project Engineer | **CORE** | SUPPORTING | SUPPORTING | **CORE** | **CORE** | R&D-heavy, publishable-quality technical work. |
| TUM IFR — Simulator Instructor | SUPPORTING | — | **CORE** | SUPPORTING | **CORE** | Graduate-level formal instruction and examiner role — the single best TA-track credential (grad-level, examiner authority). |
| HORYZN — Systems & Integration PM | **CORE** | SUPPORTING | SUPPORTING | **CORE** | **CORE** | End-to-end programme delivery; strong R&D/leadership signal for scholarship and further-ed narratives. |
| Kipepeo Aerospace — Founding CEO & Lead SE | **CORE** | **CORE** | SUPPORTING | SUPPORTING | SUPPORTING | Technical strand CORE everywhere; venture strand is what makes it CORE for Entrepreneurial specifically (see Venture Building row below). |
| Jasiri4Africa — Entrepreneur | RESERVE | **CORE** | — | RESERVE | RESERVE | Formal accelerator fellowship — direct, purpose-built evidence for accelerator/incubator applications. |

### Important consolidation decisions (unchanged from V2, still correct)
- **HORYZN:** one coherent written-CV experience, not two, regardless of track.
- **METU academic record:** the B.Sc. record appears once as Education in every track. The three leadership experiences are *separate* evidence, not restatements of it — they should never be silently folded into "METU" as if redundant.
- **Kendrone:** substantive UAS role stays distinct from the RPL credential.
- **TUM:** degree record stays distinct from technical/research projects in every track.

---

## 2. Project-level selection

Only projects whose track columns diverge meaningfully from V2's industry-only call are shown with full multi-track detail. Projects that are CORE for Industry and stay CORE/SUPPORTING everywhere else (the aircraft/UAS systems core — HIL rig, ABCU, WfA GCS, Kolibri integration, TAI UAS, AngaStack V2, Linda Nchi, ACMU, Sub-Terrain UAV, MBSE Galana Kulalu) are **unchanged from V2** — see that document for the per-item industry rationale; their SUPPORTING/CORE status for Scholarship, Further Ed and TA/Academic is generally SUPPORTING (they demonstrate rigor and lifecycle ownership, but aren't the primary evidence for those tracks the way research and teaching items are).

**Reclassified or newly surfaced projects:**

| Project | Parent | Industry | Entrepreneurial | TA/Academic | Scholarship | Further Ed |
|---|---|---|---|---|---|---|
| **Kipepeo Venture Building, Governance & Capital Strategy** | Kipepeo Aerospace | RESERVE | **CORE** | — | RESERVE | RESERVE |
| **Kilimo Anga — Field Ops, Pre-Pilot Readiness & Business Model** | Kipepeo Aerospace | RESERVE | **CORE** | — | RESERVE | RESERVE |
| Jasiri4Africa fellowship activities (no separate Project record — see Experience row) | Jasiri4Africa | RESERVE | **CORE** | — | RESERVE | RESERVE |
| Calculus SI (Peer-Assisted Study Sessions) | METU SI-PASS | RESERVE | — | **CORE** | SUPPORTING | SUPPORTING |
| ASE301 Course Instruction & Assessment | METU ASE301 TA | RESERVE | — | **CORE** | SUPPORTING | SUPPORTING |
| IFR Flight Simulator Instruction & Assessment | TUM IFR | SUPPORTING | — | **CORE** | SUPPORTING | SUPPORTING |
| Project Mentor — Hydrogen-Hybrid Engine | YSK | RESERVE | RESERVE | **CORE** | SUPPORTING | SUPPORTING |
| Project Mentor — Refuelling Rig | YSK | RESERVE | RESERVE | **CORE** | SUPPORTING | SUPPORTING |
| Geospatial Analysis — Nakuru Geotourism Research | TUM | RESERVE | — | SUPPORTING | SUPPORTING | SUPPORTING |

Every other project keeps its V2 Industry label unchanged.

---

## 3. Activity-level selection

Section 3 of V2 only covered CORE/SUPPORTING industry projects, so RESERVE-for-industry items never got activity-level treatment even where they're CORE for another track. §3A below fills that gap for the newly-elevated Entrepreneurial and TA/Academic evidence. (Original V2 §3 industry-track activity selections are unchanged — see that document.)

### 3A. Entrepreneurial track — Kipepeo Venture Building, Governance & Capital Strategy

| Activity | Why this belongs in the entrepreneurial-track pool |
|---|---|
| Authored and executed the Kipepeo Aerospace Pre-Incorporation Founders' Agreement — cap table, reverse vesting, governance and IP transfer under Kenyan law | Direct founder-governance evidence; the kind of document accelerators specifically screen for. |
| Negotiated and executed a SAFE agreement with Zimbu Investments Limited, securing first external capital at a $1,000,000 valuation cap | Demonstrates the ability to close an actual investment instrument, not just pitch one. |
| Completed the Viktoria Ventures Startup360 Access to Finance programme; authored a $30,000 pre-seed investor-readiness dossier and financial model | Formal investor-readiness credential with a quantified financial model. |
| Onboarded into the 12-month #MyLittleBigThing Investor Readiness Program (MK-Africa / Strathmore @iBizAfrica), one of 16 semi-finalist ventures | Active incubation-pipeline standing — directly answers "are you accelerator-ready." |
| Secured Microsoft for Startups Founders Hub and Google Cloud for Startups grant acceptances | Track record of winning non-dilutive startup programme support. |
| Negotiated and executed three binding MoUs with an external investment firm for market access, testing and drone-corridor access | Partnership/negotiation evidence beyond internal engineering decisions. |
| Restructured the executive team and built a 7-member advisory board, converting a co-founder from BD Lead to Co-Founder & COO | Team-building and governance-structuring evidence. |

### 3B. Entrepreneurial track — Kilimo Anga: Field Operations, Pre-Pilot Readiness & Business Model

| Activity | Why this belongs in the entrepreneurial-track pool |
|---|---|
| Selected into the Top 50 (MK-Africa #MyLittleBigThing Sustainable Venture Challenge); completed a Falsifiable Test Plan and virtual experiment setup | Competitive venture-challenge validation. |
| Executed a 30-Day Build & Test Challenge; validated 93.9% farmer interest (vs. 40% benchmark) and a 325.56 KES/acre willingness-to-pay baseline, driving four UI/UX iterations | Quantified market-validation methodology — exactly what an accelerator application wants to see evidenced, not asserted. |

### 3C. Entrepreneurial track — Jasiri4Africa (Talent Investor Fellowship)

| Activity | Why this belongs in the entrepreneurial-track pool |
|---|---|
| Completed the Jasiri Jumpstart and 3-month Residential Intensive; executed field-level market discovery on smallholder agri-data adoption barriers | Formal accelerator programme completion with fieldwork, not classroom-only. |
| Formulated the dual-sided business model canvas and revenue architecture for the iCARUS concept — pay-per-scan B2C and B2B subscriptions, $5.7M TAM | Structured business-model artifact — standard accelerator deliverable, already produced. |
| Authored and delivered the iCARUS pitch deck at Jasiri Demo Day 1, Bugesera, Rwanda | Direct pitch-delivery evidence to programme directors and venture coaches. |

### 3D. TA/Academic track — teaching evidence

| Activity | Why this belongs in the TA/academic-track pool |
|---|---|
| SI-PASS: certified as SI-PASS Leader/Instructor after formal 2-day training; delivered peer-led Calculus I & II sessions across two full semesters | Sustained, certified peer-instruction role. |
| ASE301: conducted 5 dedicated consultation sessions for 30+ students; graded 3 major assignment cycles with detailed feedback | Formal TA duties (instruction + assessment) in aerospace engineering itself — the most directly relevant teaching evidence for an aerospace-adjacent academic post. |
| TUM IFR Simulator: delivered practical IFR flight instruction; served as official course examiner in 5-hour final practical/oral exams, evaluated against departmental scorecards | Graduate-level instruction with formal examiner authority — the strongest single teaching credential in the database. |
| VP, Aerospace Society: organised MATLAB/Autodesk Inventor technical training sessions for society members; hosted faculty guest lectures and technical seminars | Shows teaching initiative extending beyond formal TA duties into peer technical education. |
| STEM Mentorship (YSK): guided embedded-systems architecture and control-logic design for a student refuelling-rig project; advised on a hydrogen-hybrid engine project that achieved a validated 43.6% fuel-efficiency gain | Technical mentorship with a genuinely quantified outcome — rare and worth keeping visible. |

---

## 4. What the multi-track evidence says about the Master CV

### A. The industry-facing core narrative is unchanged
Sections 4A–4E of V2 (primary identity, lifecycle, hardware/software boundary, R&D, academic/research positioning) remain correct and are not repeated here.

### B. Entrepreneurial positioning is a genuine, separate strength — not a footnote to Kipepeo's engineering story
The venture-building evidence stands on its own: signed investment instruments, formal accelerator completions, and quantified market validation. For accelerator/incubator applications this evidence should lead, with the technical platform (TAI UAS, AngaStack, Kilimo Anga engineering) as supporting proof that the founder can actually build what's being pitched.

### C. Teaching evidence is thin in volume but high in quality
Five distinct teaching/instruction experiences exist, spanning peer instruction, formal TA duties, and graduate-level exam authority. This is enough for a credible academic-service section — it should not be compressed into a single throwaway line as V2's blueprint envisioned.

### D. Leadership evidence needed rescuing from "duplicate record" framing
Once separated from the B.Sc. academic record, the three METU leadership experiences are legitimate organisational-leadership evidence (launching a project team, reviving a dormant society, running an 8-directorate association) — relevant wherever leadership or initiative is being assessed, which is most further-education and some academic applications.

---

## 5. Track-specific writing pools (in addition to the unchanged Industry pool from V2 §6)

### Entrepreneurial
Kipepeo Aerospace (Founding CEO framing, venture strand) → Kipepeo Venture Building activities (§3A) → Kilimo Anga business-model activities (§3B) → Jasiri4Africa (§3C) → TAI UAS / Kilimo Anga / AngaStack as proof-of-build evidence beneath the venture narrative.

### TA/Academic
TUM IFR Simulator Instructor → ASE301 TA → SI-PASS Instructor → VP Aerospace Society (teaching-adjacent activities only) → STEM Mentorship → underpinned by the research-heavy technical projects (UAM throughput, ACMU, MBSE, Sub-Terrain UAV) as the research-capability evidence.

### Scholarship / MSc completion
TUM technical/research projects (unchanged CORE from V2) → University of Cologne DAAD/LEAD! programme → HORYZN R&D strand → BSc honours record → teaching evidence as secondary signal of academic engagement.

### Further education / university admission
Same research core as Scholarship, plus the METU leadership experiences (initiative/trajectory signal) and Secretary General/VP roles where a programme values demonstrated leadership alongside academics.

---

## 6. Quality-control rules for 6C (extends V2 §7)

1. All eight original V2 rules still apply.
2. **Track discipline:** when writing a track-specific variant, only pull from that track's CORE/SUPPORTING pool. Don't let strong industry evidence crowd out weaker-but-relevant track evidence just because it reads more impressively.
3. **Don't inflate the entrepreneurial narrative past what's documented.** The SAFE agreement, MoUs and grants are real and specific — state them exactly as documented; don't imply revenue, product-market fit, or a completed funding round beyond the pre-seed/pilot stage actually evidenced.
4. **Kipepeo gets framed differently per track, not filtered differently.** For Industry, Kipepeo is "founding engineer, technical platform." For Entrepreneurial, it's "founder who closed a SAFE, structured governance, and won three startup programmes" — same underlying role, different foregrounded evidence.

---

**Workflow (unchanged):** Career Database → 6A Evidence Map → **6B Content Selection (V3, multi-track)** → 6C Master CV → per-track tailored variants.
