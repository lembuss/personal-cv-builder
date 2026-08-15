# CAREER CV ROADMAP — CHAT HANDOVER (v3 — Unbiased Multi-Track Master System)

## 0. What Changed in Revision 3 (Critical Realignment)

Previous revisions (v1 and v2) and early Phase 6 drafts suffered from an **industry-focused bias**. They imposed an artificial 3–4 page budget that trimmed out non-industry activities (such as venture governance, university leadership, and academic instruction) and relegated them to a secondary "reserve pool."

**This revision corrects that flaw completely:**

- **Discarded Page Limits & Editorial Pruning:** The Master Content Pool is explicitly **not** a 2-page or 3-page industry CV. It is an **exhaustive, un-pruned Master Content Pool** capturing 100% of Brian's career database (`dev.db`).
- **Four Equal-Priority Professional Pillars:** Technical Systems Engineering, Venture Building & Entrepreneurship, Deep-Tech Research, and Teaching/Academic Leadership carry equal weight. No pillar is treated as background filler or secondary noise.
- **Eight Target Application Tracks:** The pipeline directly feeds 8 downstream application tracks without ever re-clearing or reconstructing Brian's career.
- **Phase 6B Skipped for Master Pool Construction:** Because the Master Content Pool takes 100% of all 163 activities across all 40 projects and 20 experiences, the selection/pruning filter of Phase 6B is naturally absorbed.

---

## 1. Purpose & Overall Architecture

The goal is to maintain a **single, comprehensive, evidence-backed Master Content Pool** built directly from Brian's career database (`dev.db`). From this un-pruned Master Pool, targeted materials will be derived downstream for 8 equal-priority tracks:

1. **Aircraft systems engineering / aerospace industry roles**
2. **UAS / eVTOL / advanced air mobility roles**
3. **R&D / deep-tech engineering roles**
4. **Research roles / PhD admissions**
5. **Scholarships and completion of the MSc at TUM**
6. **Further education / university admissions (postgraduate study beyond TUM)**
7. **Entrepreneurial ventures — accelerators, incubators, founder-track applications**
8. **Teaching assistant and academic roles**

### Pipeline Flow

            CAREER DATABASE (dev.db)
                      │
                      ▼
        UNBIASED NARRATIVE (Phase 5)
                      │
                      ▼
         EVIDENCE MAP (Phase 6A + Addendum)
                      │
                      ▼
      MASTER CONTENT POOL (Phase 6C - 100% Data)
                      |
   ┌──────────────────┼──────────────────┐
   ▼                  ▼                  ▼
Industry CV        Founder Bio        Academic CV /
(2-Page Target)    / Venture Pitch     Teaching Statement

---

## 2. Active Source of Truth & Unbiased Reference Documents

The new chat must strictly restrict its context to the following **unbiased reference set**:

1. **`dev.db` (Primary Factual Source of Truth):** SQLite database containing all 20 experiences, 40 projects, and 163 activities.
2. **`CAREER_CV_ROADMAP_HANDOVER-V3.md`:** The strategic roadmap mandating a single master system across equal-priority multi-track applications.
3. **`MASTER-CV-EVIDENCE-MAP-V2.md` (Raw Activity Text):** The un-pruned, complete text inventory containing the exact `What`, `How`, and `Result` statements for all 163 database activities.
4. **`MASTER-CV-EVIDENCE-MAP-ADDENDUM.md`:** The patch document separating leadership, venture-building, and teaching evidence into their true categories.
5. **`Phase 5 — Professional Narrative (Unbiased Multi-Track Baseline)`:** The locked 4-pillar narrative balancing Technical Systems, Venture Building, Deep-Tech Research, and Teaching/Academic Leadership.

---

## 3. Disregarded & Deprecated Documents (DO NOT USE)

To avoid looping or re-introducing industry bias, the following documents are **explicitly disregarded or paused**:

*   **`master-cv-content.md`:** **DISREGARD.** This was an industry-biased, 3-page draft that pruned non-industry evidence.
*   **`MASTER_CV_BLUEPRINT_CONSOLIDATED.md` & `MASTER-CV-BLUEPRINT-V2.md`:** **DISREGARD PAGE BUDGETS.** While the logical section order is kept (Profile → Competencies → Experience → Projects → Education → Teaching → Leadership → Credentials → Skills), the 3–4 page limit is completely thrown out.
*   **`MASTER-CV-CONTENT-SELECTION-V2.md` & `V4.md` (`DOC.md`):** **DISREGARD SELECTION FILTERS.** These documents labeled non-industry items as "RESERVE for Industry." In the Master Content Pool, no activity is relegated to reserve.
*   **`mastercv.json` & `buildcv.py`:** **PAUSED.** Useful build scripts for later rendering, but paused until the Master Content Pool text is compiled in Markdown.

---

## 4. Phase 5 Locked Baseline: The Four Professional Pillars

The professional identity is governed by four equally weighted pillars:

1.  **Aircraft Systems & Aerospace Engineering:** End-to-end systems lifecycle ownership (requirements, functional decomposition, architecture, HW/SW integration, HIL testing, V&V, MRO, flight testing) across manned aircraft (ALS Ltd), UAV OEMs (Amazilia Aerospace, Kipepeo Aerospace), and eVTOL platforms (HORYZN).
2.  **Venture Building & Entrepreneurial Leadership:** Technical founder capability (company incorporation BN-BGCKDY99, Pre-Incorporation Founders' Agreement with 80/20 equity split & 4-year reverse vesting, $1,000 SAFE execution at $1M cap with Zimbu Investments, $150k Microsoft + $2k Google startup grants, 3 commercial MoUs, Jasiri Fellow, #MyLittleBigThing, Startup360 A2F, 2026–2027 IRP cohort, and 120 farmer validation studies).
3.  **Deep-Tech Research & Computational Capability:** Applied research and publication depth (AIAA 2024 co-authored UAM throughput paper, embedded C++ TDD logging with 5× compression, MBSE agricultural UAS architecture graded *Sehr gut* [A, 8 ECTS], ROS/OctoMap 3D subterranean perception, and OpenFOAM/ANSYS CFX CFD).
4.  **Teaching, Mentorship & Academic Service:** Academic instruction and administration (TUM EC135 IFR simulator instructor/examiner, METU ASE301 Numerical Methods TA, certified SI-PASS Calculus tutoring, Young Scientists Kenya STEM mentorship with 43.6% engine efficiency gain, and METU ISA Secretary General managing 8 directorates).

---

## 5. Non-Embellishment & Operating Rules

The following rules govern all content generation:

1.  **Strict Truthfulness:** Do not invent, embellish, reinterpret, or add career facts. The database (`dev.db`) is Brian's career.
2.  **TUM MSc Status:** Must **never** be represented as completed or awarded. Always state: *Degree completion pending (73 ECTS completed; 17 credits and thesis remaining)*.
3.  **Kipepeo Aerospace:** Represent technical OEM deliverables and formal venture governance metrics accurately without inflating early-stage revenues.
4.  **No Pruning in 6C:** The Master Content Pool must contain **all 163 activities** across **all 40 projects** and **20 experiences**. Do not condense or omit activities to save vertical space.
5.  **Preserve Technical Metrics:** Retain exact quantitative metrics (e.g., $FS=4.07$, $100\text{N}$ tip load, 80% log reduction / 5x throughput gain, $86.9\%$ CAT-D/E traffic, $66\text{km}$ to $15\text{km}$ detour reduction, $W_0=20,600\text{kg}$, 306kW hover power, $93.9\%$ farmer interest)[cite: 13, 14].

---

## 6. Current Status & Phase Progress

*   **Phases 1–4 (Database & Inventory):** **COMPLETE** (`dev.db` contains 20 experiences, 40 projects, 163 activities).
*   **Phase 5 (Multi-Track Positioning Baseline):** **COMPLETE & LOCKED** (governed by the 4-pillar narrative above).
*   **Phase 6A (Evidence Mapping):** **COMPLETE** (`MASTER-CV-EVIDENCE-MAP-V2.md` + Addendum).
*   **Phase 6B (Selection Filter):** **SKIPPED / ABSORBED** (because the Master Content Pool takes 100% of activities, no selection filter is applied).
*   **Phase 6C (Master Content Pool Construction):** **IMMEDIATE NEXT TASK FOR NEW CHAT**.

---

## 7. Immediate Task Instructions for the New Chat

The immediate objective in the new chat is to execute **Phase 6C: Compile the Complete Un-Pruned Master Content Pool** in structured Markdown text.

### Execution Blueprint for Phase 6C:
The new chat must generate the Master Content Pool following this section layout, outputting all 163 activities without cutting text:

1.  **Header & Master Professional Profile** (incorporating the 4-pillar narrative).
2.  **Core Competencies** (spanning all domain clusters: Systems Engineering, Avionics/Embedded, Software/Cloud, Aerodynamics/CFD, Venture/Governance, Teaching/Academic).
3.  **Complete Professional Experience (All 20 Experiences / 163 Activities):**
    *   Kipepeo Aerospace (39 activities)
    *   Middle East Technical University (24 activities)
    *   Kendrone Ltd — UAS Company (18 activities)
    *   Amazilia Aerospace GmbH (17 activities)
    *   Technical University of Munich — Graduate Student (12 activities)
    *   ALS Ltd (7 activities)
    *   HORYZN — Systems Integration PM (7 activities)
    *   HORYZN — Aerodynamics Engineer (6 activities)
    *   University of Cologne — DAAD Scholar (5 activities)
    *   METU — Vice President, Aerospace Society (4 activities)
    *   Skylink Flight Services — PPL (3 activities)
    *   eMobilis Technology Institute (3 activities)
    *   METU — President, MUN Society (3 activities)
    *   METU — Secretary General, ISA (3 activities)
    *   Jasiri4Africa — Jasiri Fellow (3 activities)
    *   TUM Rotorcraft Institute — Simulator Instructor (2 activities)
    *   METU — SI-PASS Calculus Leader (2 activities)
    *   METU — Student Assistant ASE301 TA (2 activities)
    *   Young Scientists Kenya — STEM Mentorship (2 activities)
    *   Kendrone Ltd — RPL Training (1 activity)
4.  **Complete Engineering & R&D Projects (All 40 Projects)**
5.  **Education** (TUM MSc pending 73 ECTS, METU BSc Honours 3.12 CGPA, Cologne DAAD)
6.  **Research & Publications** (AIAA 2024 paper, Geotourism journal article, TUM UAM Thesis)
7.  **Teaching & Academic Experience** (TUM, METU, YSK)
8.  **Leadership & Mentorship** (ISA SecGen, Aerospace Society VP, MUN President)
9.  **Licences, Certifications & Full Technical Skills Taxonomy**

When starting the new chat, instruct the AI to **begin Phase 6C immediately** using this