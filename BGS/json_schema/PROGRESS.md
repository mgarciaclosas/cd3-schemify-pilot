# CD3 pilot — BGS (Breast Cancer Now Generations Study) derived variables — conversion progress

package: CD3_Schemify_Pilot/BGS/json_schema · started: 2026-08-21
grain: One element is one participant's R0 (baseline) analysis-ready derived variables.
dictionary: DerivedVariables_Schema.json (Schema_and_Derivation_Utils/Questionnaire/R0/schemas/derived/) — full inventory in SOURCES.md

## How to continue

This conversion runs over several sittings — an agent session can hold only so
much at once, so the work is planned in units that each fit one session. Nothing
is lost between sittings: this file is the memory.

To continue at any time: open a fresh agent session in this package's directory
and invoke the skill again. The agent reads this file and proposes the next
unit. You can also ask for anything directly — a specific category, a change,
a question, the final review.

This package is one of three sibling CD3 pilots (BGS, OFH, MWS — see
`../../` for the others), independent of the earlier R0-questionnaire pilot at
`GS_Schemify_Pilot/`. Unlike that pilot, this one converts **all** source
properties in one pass, not a single category, per the steward's explicit
instruction.

## Conventions

- sentinels: -999 (missing_numeric) · "MISSING" (missing_string) — agent-decided,
  mirrors the R0-questionnaire pilot's policy · D001. Plus 9999 (not_applicable)
  — adopted verbatim from the source, which already used it consistently across
  ~12 properties, distinct from bare null · D002
- $id base: https://schemas.example.org/cd3-bgs-pilot/ (replace before publishing)
- grain: see header · title separator: — (em dash) · formatting: 2-space, one key per line
- real data: none in this repo; toy fixtures authored from the source schema's
  stated bounds and enums only · D003
- x-derivedFrom (source's lineage-pointer mechanism) has no equivalent in
  schemify's 5-key x-* vocabulary; folded into x-derivation as prose instead ·
  D004. x-formerName (legacy variable name) folded into $comment · D005
- 10 R0_FamHist* properties trace provenance to legacy SAS scripts on a network
  drive, not other schema fields — preserved verbatim in x-derivation rather
  than treated as unresolvable $defs pointers · D006
- no cross-field routing (if/then) rules added yet — the source schema does not
  establish clear skip logic between these derived fields (e.g. R0_AgeMenopause
  has no NA branch even though R0_Menopause=2 would logically make it
  inapplicable) — open item, D007

## Categories

| # | category | file | vars | status | touched |
|---|---|---|---|---|---|
| 1 | Identity | derived_variables/categories/identity.json | 1 | rendered, pending steward review | 2026-08-21 |
| 2 | Ethnicity | derived_variables/categories/ethnicity.json | 2 | rendered, pending steward review | 2026-08-21 |
| 3 | Body Size | derived_variables/categories/body_size.json | 11 | rendered, pending steward review | 2026-08-21 |
| 4 | Menarche | derived_variables/categories/menarche.json | 1 | rendered, pending steward review | 2026-08-21 |
| 5 | Contraceptive Use | derived_variables/categories/contraceptive_use.json | 4 | rendered, pending steward review | 2026-08-21 |
| 6 | Pregnancy Parity | derived_variables/categories/pregnancy_parity.json | 8 | rendered, pending steward review | 2026-08-21 |
| 7 | Breast Disease | derived_variables/categories/breast_disease.json | 1 | rendered, pending steward review | 2026-08-21 |
| 8 | Diabetes | derived_variables/categories/diabetes.json | 3 | rendered, pending steward review | 2026-08-21 |
| 9 | Menopause HRT | derived_variables/categories/menopause_hrt.json | 7 | rendered, pending steward review | 2026-08-21 |
| 10 | Alcohol | derived_variables/categories/alcohol.json | 4 | rendered, pending steward review | 2026-08-21 |
| 11 | Smoking Diet Activity | derived_variables/categories/smoking_diet_activity.json | 8 | rendered, pending steward review | 2026-08-21 |
| 12 | Family History | derived_variables/categories/family_history.json | 10 | rendered, pending steward review | 2026-08-21 |

60 of 60 source properties converted (full pilot, no subset).

## Package milestones

- [x] intake: source registered · grain confirmed · categories confirmed (12, all converted)
- [x] common/defs.json + mother scaffold validate green
- [ ] every category confirmed (all 12 rendered; steward confirmation still open)
- [ ] cross-category skip audit (D007 — no rules written yet, needs steward input)
- [x] coverage audit 1:1 (60/60)
- [x] pages current for all 12 categories
- [ ] review walked · cleanup decided

## Session log

- 2026-08-21 · intake + convert all 12 categories · Registered DerivedVariables_Schema.json, proposed and confirmed the 12-category breakdown, scaffolded package, drafted all 60 properties across 12 category files, authored fixtures (27 valid rows, 7 invalid cases), rendered dictionary.html + playground.html, all validate.py checks green (check/fixtures/coverage). Caught and fixed one gap during fixture-building: R0_Parity had no plausibility maximum (unlike the other count fields). · next: present to the steward for category-by-category confirmation, and settle D007 (cross-field routing) before review.
