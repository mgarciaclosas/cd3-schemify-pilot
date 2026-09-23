# CD3 pilot — BGS derived variables — conversion progress

package: CD3_Schemify_Pilot/BGS/json_schema · started: 2026-09-15
grain: One element is one participant's baseline (R0) analysis-ready derived variables, keyed by `TCode`
dictionary: DerivedVariables_Schema.json (Generations Study, JSON Schema, 60 properties) — full inventory in SOURCES.md

## How to continue

This conversion runs over several sittings — an agent session can hold only so
much at once, so the work is planned in units that each fit one session. Nothing
is lost between sittings: this file is the memory.

To continue at any time: open a fresh agent session in this package's directory
and invoke the skill again. The agent reads this file and proposes the next
unit. You can also ask for anything directly — a specific category, a change,
a question, the final review.

## Conventions

- sentinels: `9999` not applicable (adopted from source) · `-999` missing (approved, replaces source `null`) · D003, D004
- $id base: https://schemas.example.org/cd3-bgs-pilot/ (replace before publishing) · D002
- grain: see header · title separator: — (em dash) · formatting: 2-space, one key per line · D002
- titles: source `description` text verbatim; no separate description · D010
- real data: none in repo · D005
- routing: faithful · D009

## Categories

Approved by the steward 2026-09-21 (D015).

| # | category | file | vars | source slice | status | touched |
|---|---|---|---|---|---|---|
| 1 | Identification | derived_variables/categories/identification.json | 1 | TCode | confirmed | 2026-09-21 |
| 2 | Demographics | derived_variables/categories/demographics.json | 2 | R0_Ethnicity, R0_AshkenaziAncestry | confirmed | 2026-09-21 |
| 3 | Anthropometric | derived_variables/categories/anthropometric.json | 11 | Height/Weight/BMI (age 20 and baseline), HighestWeight(+Age), Waist, Hip, WaistHipRatio | confirmed | 2026-09-21 |
| 4 | Reproductive/Hormonal | derived_variables/categories/reproductive_hormonal.json | 20 | pregnancy, menarche, OC, parity/births, breastfeeding, menopause, HRT | confirmed | 2026-09-21 |
| 5 | Medical History | derived_variables/categories/medical_history.json | 4 | R0_BBD, diabetes (3) | confirmed | 2026-09-21 |
| 6 | Behavioral | derived_variables/categories/behavioral.json | 12 | alcohol (4), smoking (5), physical activity, fruit, green veg | confirmed | 2026-09-21 |
| 7 | Family History | derived_variables/categories/family_history.json | 10 | R0_FamHist* | confirmed | 2026-09-21 |

## Package milestones

- [x] intake: sources registered · grain confirmed · categories confirmed (D001, D015)
- [x] common/defs.json + mother scaffold validate green (2026-09-21, 3 files)
- [x] every category confirmed (7/7, 2026-09-21)
- [x] skip audit (ROUTING.md) — done 2026-09-21: R001-R004 encoded and fixtured, R005 not-enforceable (D013), R006/R007 declined (D036)
- [x] coverage audit 1:1 (60/60 converted, 0 pending, 0 mismatches)
- [x] pages current for the whole package (2026-09-21)
- [x] review walked (18 agent-decided lines ratified 2026-09-21, 0 open) · [x] cleanup decided (keep, 2026-09-21)

## Session log

- 2026-09-21 · intake · sources surveyed, routing scan run (5 stated rules in ROUTING.csv), interview answered (D001–D010), Generations conventions doc consulted, 7 categories proposed · next: intake (steward approves category table, then scaffold)
- 2026-09-21 · intake · category table approved (D015), `-999` approved (D004), D016 resolved; scaffolded package (assets, tools, common/defs.json, mother, identification category), validate.py check green, VARIABLES.csv categories assigned · next: convert anthropometric
- 2026-09-21 · convert anthropometric · 11 vars drafted, fixtures 8 valid / 14 seeded violations all caught, both pages rendered, D018-D020; routing R001/R002 stay waiting on reproductive_hormonal (PregAt20, PregAtEntry) · next: convert reproductive_hormonal (steward confirms anthropometric first)
- 2026-09-21 · convert reproductive_hormonal · anthropometric confirmed by steward; 20 vars drafted, R001-R003 encoded (D022-D024), x-universe added on BMI/WHR, fixtures 9 valid / 31 seeded violations all caught, D022-D027 · next: steward confirms reproductive_hormonal and answers D027, then convert medical_history (encodes R004)
- 2026-09-21 · convert medical_history · reproductive_hormonal confirmed by steward (D027 answered, D028 open); 4 vars drafted, R004 encoded (D029), fixtures 9 valid / 36 seeded violations all caught, D029-D030 · next: steward confirms medical_history and answers D030, then convert behavioral
- 2026-09-21 · convert behavioral · medical_history confirmed by steward; 12 vars drafted, no rule encoded (R006/R007 proposed, cell value asked, D032), PhysicalActivity unit defect D031, fixtures 9 valid / 44 seeded violations all caught · next: steward confirms behavioral and answers D030-D032, then convert family_history
- 2026-09-21 · elicit (0 open in this batch) · D030 -999 for now, D031 keep unit defect as is, D032 keep no rule for R006/R007 for now (rows stay proposed) · next: convert family_history (behavioral awaiting steward confirmation)
- 2026-09-21 · convert family_history + demographics · behavioral confirmed by steward; family_history (10) drafted with soft checks D033; demographics (2) had been skipped in planning order and was caught by the coverage check, converted (D035); all 60 converted, fixtures 9 valid / 51 seeded violations all caught · next: steward confirms demographics and family_history, then skips audit (R006/R007 proposed) and review
- 2026-09-21 · skips audit · demographics, family_history, identification confirmed by steward (7/7); routing check green: R001-R004 encoded and fixtured, R005 not-enforceable (D013), 5 NA-bearing fields with no stated trigger covered by D016; R006/R007 still proposed (steward: keep as is for now) so the milestone is not ticked · next: skips audit (steward decides R006/R007, or a second 'later' migrates them to the README at review)
- 2026-09-21 · skips audit · steward declined R006/R007 (D036); swept stale 'waits'/'awaits' comments in anthropometric.json and behavioral.json (5); routing check green (2 informational/warn notes explained: R0_EverHadPeriods not delivered, 5 NA-bearing fields with no stated trigger D016); milestone ticked · next: review
- 2026-09-21 · elicit (0 open) · D028 closed by reading the raw Generations notebook; D037 defect (R0_PregAtEntry codes 0/1 declared vs 0/1/2/3 produced) resolved: keep declared 0/1, note added to the field's comment · next: review
- 2026-09-21 · revise all categories (comments) · removed 'Derived from' lineage sentences from 59 property comments at steward request (D038); kept former names, formulas, rule and defect notes, one [sic] note on R0_Height20; re-rendered; no status changes · next: review
- 2026-09-21 · review (walk, part 1) · completion checks run (summary green, 0 open ledger lines, 18 agent-decided lines grouped into 5 themes); presented themes 1-3 (sentinels, bounds and types, naming and annotations) · next: review (walk themes 4-5: routing rules, not-enforceable; then README and cleanup)
- 2026-09-21 · review (walk, part 2) · steward accepted themes 1-3 (D003, D011, D012, D014, D017, D019, D020, D025, D034, D035 now user-confirmed); presenting themes 4-5 (routing D022-D024, D029; not-enforceable D013, D018, D026, D033) · next: review (steward answers themes 4-5; then README and cleanup)
- 2026-09-21 · review (README) · steward accepted themes 4-5 (all 18 agent-decided lines now user-confirmed); README.md written with 10 sections; real-data offer: none in repo (D005) · next: review (cleanup offer: keep or clean the working files)
- 2026-09-21 · review (cleanup) · steward chose keep: state trio stays beside the package · next: — (complete)
