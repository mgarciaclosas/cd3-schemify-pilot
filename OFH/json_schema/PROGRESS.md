# CD3 pilot — Our Future Health (participant + questionnaire) — conversion progress

package: CD3_Schemify_Pilot/OFH/json_schema · started: 2026-08-21
grain: Two tables, two grains. participant: one element is one participant's core registration/consent/birth/blood-sample/demographic record. questionnaire: one element is one submitted questionnaire response (a participant may have more than one).
dictionary: our_future_health_data_dictionary_v14.xlsx + our_future_health_codings_v14.xlsx (participant and questionnaire sheets) — full inventory in SOURCES.md

## How to continue

This conversion runs over several sittings. To continue: open a fresh agent
session in this package's directory and invoke the skill again.

This is one of three sibling CD3 pilots (BGS, OFH, MWS — see `../../`
for the others). Scope for this pilot is `participant` (14 properties) +
`questionnaire` (359 properties, all 6 of its source sections) — OFH's data
dictionary has 5 more domains (`clinic_measurements`, `poct_lipid_profile`,
`participant_geographies`, `linked_nhse_health_records`, `genetic_data`), not
converted here; two of those (`linked_nhse_health_records` at 569 vars /
328,833 coding rows, and `genetic_data`) are likely impractical for the same
treatment without a different strategy for their coding tables.

## Conventions

- sentinels are source-adopted, not agent-invented, for the fields that have
  one: prefer_not_to_answer (-3), dont_know (-1, questionnaire only),
  none_of_the_above (-7, questionnaire only, substantive not missingness),
  suppressed (-999, disclosure control) · D001, D007
- 352 of 353 coded questionnaire fields carry at least one of the four known
  sentinels; only SKIP_PHQ9_GAD7_1_1 has none (left required) · D007
- Important: -999 means something different here than in the sibling BGS
  package (there, it's agent-decided generic missingness) — packages are
  independent, this is expected, not a bug · D001
- questionnaire is a second table, not folded into participant — genuinely
  different grain, confirmed via the source's own relational metadata · D006
- 134 of 353 questionnaire fields (is_multi_select=yes) have an unresolved
  shape ambiguity — flagged per-field and as a package-level open item, not
  guessed at · D008. Real, significant: affects over a third of the table.
- height/weight fields have an unresolved unit ambiguity (paired unit-selector
  fields) · D009. SUBMISSION_DATE format assumed ISO 8601 · D010.
- $id base: https://schemas.example.org/cd3-ofh-pilot/ (replace before publishing)
- title separator: — (em dash) · formatting: 2-space, one key per line
- real data: none in this repo; toy fixtures authored from the source's stated
  codes and an agent-decided plausibility range for uncoded numeric fields · D003

## Categories

| # | table | category | file | vars | status | touched |
|---|---|---|---|---|---|---|
| 1 | participant | Participant | participant/categories/participant.json | 14 | rendered, pending steward review | 2026-08-21 |
| 2 | questionnaire | Questionnaire Information | questionnaire/categories/questionnaire_info.json | 4 | rendered, pending steward review | 2026-08-21 |
| 3 | questionnaire | About You Household | questionnaire/categories/about_you_household.json | 21 | rendered, pending steward review | 2026-08-21 |
| 4 | questionnaire | Work Education | questionnaire/categories/work_education.json | 15 | rendered, pending steward review | 2026-08-21 |
| 5 | questionnaire | Lifestyle | questionnaire/categories/lifestyle.json | 117 | rendered, pending steward review | 2026-08-21 |
| 6 | questionnaire | Family Health History | questionnaire/categories/family_health_history.json | 74 | rendered, pending steward review | 2026-08-21 |
| 7 | questionnaire | Health History | questionnaire/categories/health_history.json | 128 | rendered, pending steward review | 2026-08-21 |

373 properties converted total (14 participant + 359 questionnaire, both full
scope, no subset). Remaining 5 OFH domains not started.

## Package milestones

- [x] intake: sources registered · grain confirmed for both tables · categories confirmed (1 for participant; 6 for questionnaire, taken from source's own folder_path)
- [x] common/defs.json + both mother scaffolds validate green
- [ ] every category confirmed by steward
- [ ] D008 (multi-select shape) resolved — significant open item, affects >1/3 of questionnaire
- [x] coverage audit 1:1 (373/373, scoped to participant + questionnaire)
- [x] pages current for both tables
- [ ] review walked · cleanup decided
- [ ] decide whether/how to scope the remaining 5 OFH domains

## Session log

- 2026-08-21 · intake + convert participant domain · Registered both OFH source files, confirmed single-category scope (14 vars), scaffolded package, drafted all 14 properties, discovered and adopted the source's own sentinel conventions (-3 prefer-not-to-answer, -999 suppressed) rather than inventing one, authored fixtures (20 valid rows, 6 invalid cases), rendered both pages, all validate.py checks green. · next: present to steward; decide scope for the remaining 7 OFH domains if this pilot is judged successful.
- 2026-08-21 · add questionnaire table (all 6 sections, 359 properties) · Confirmed questionnaire is a genuinely different grain from participant (own local ID, many_to_one PID) and added as a second table per LAYOUT.md. Derived the 6-category breakdown directly from the source's own folder_path column. Scanned all 353 coded fields' coding tables at scale, found two more invariant source sentinels (dont_know -1, none_of_the_above -7) confirmed by full-table scan not sampling; 352/353 fields covered. Flagged two significant open items rather than guessing: is_multi_select's type/shape mismatch (134 fields) and height/weight unit ambiguity. Reorganised fixtures into examples/<table>/ per LAYOUT.md's multi-table convention (moved participant's fixtures, not just added questionnaire's). Caught and fixed one real bug in my own fixture-generation script (two plain-string fields were silently dropped from every row). Authored fixtures (80 valid rows, 7 invalid cases). All validate.py checks green. · next: present to steward, with D008 (multi-select ambiguity) as the highest-priority open item.
