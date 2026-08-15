# Phase 6A — Evidence Map Addendum (widened scope)

## Why this is an addendum, not a V3 rewrite

6A's job is narrower than 6B's: it maps *what evidence exists and where it comes from*, not what deserves space or for which track — that judgement belongs in 6B (now V3). The evidence map itself doesn't need a track-column restructure the way 6B did. It has one real problem worth fixing, and it's narrow enough not to justify regenerating the full 600K document.

## The problem

Several genuinely different categories of evidence were tagged with the same generic label — **"Supporting leadership/venture evidence"** — in the activity-level rows of `MASTER-CV-EVIDENCE-MAP-V2.md`. For example, this exact tag is applied to:

- MUN activities (reviving a dormant student society, leading a 17-person delegation) — this is **leadership** evidence.
- Jasiri4Africa activities (business model canvas, Demo Day pitch) — this is **entrepreneurial/venture** evidence.
- SI-PASS certification — this is **teaching** evidence, mistagged into the same bucket.

Bundling three distinct categories under one label is why they were invisible when 6B was written under the industry-only lens: nothing distinguished "this is leadership" from "this is venture-building" from "this is teaching," so all three got swept into the same low-priority pile.

## The fix

Wherever the evidence map's activity-level "category" column currently reads **"Supporting leadership/venture evidence,"** it should be split into the actual category:

- **Leadership evidence** — university society roles (VP Aerospace Society, Secretary General ISA, MUN President) and any team-building/advisory-board activity within Kipepeo Venture Building.
- **Entrepreneurial/venture evidence** — Jasiri4Africa activities, Kipepeo Venture Building activities (SAFE agreement, Founders' Agreement, MoUs, accelerator/grant acceptances), Kilimo Anga business-model/field-validation activities.
- **Teaching/academic-service evidence** — SI-PASS, ASE301 TA, TUM IFR Simulator Instructor, and the training-session activities within VP Aerospace Society.

This is a find-and-recategorize pass on the existing document, not new analysis — Phase 6B V3 (§1, §3A–3D) already did the categorization work; 6A just needs its tags to match.

## Recommendation

Given the file's size, do this as a targeted search-and-replace pass against the specific activity IDs listed in Phase 6B V3 §3A–3D, rather than a full manual regeneration. I can run that pass directly against `MASTER-CV-EVIDENCE-MAP-V2.md` if you'd like — it's a mechanical fix now that the categories are defined, not a re-review.

No other structural change to 6A is needed. It remains correctly scoped as an inventory/traceability layer.
