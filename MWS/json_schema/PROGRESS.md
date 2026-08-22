# CD3 pilot — Million Women Study recruitment variables — conversion progress

package: CD3_Schemify_Pilot/MWS/json_schema · started: 2026-08-21
grain: One element is one participant's recruitment-questionnaire derived variables.
dictionary: millionwomenstudydatadictionary-v1-21.xlsx ("Recruitment variables" sheet) — full inventory in SOURCES.md

## How to continue

This conversion runs over several sittings. To continue: open a fresh agent
session in this package's directory and invoke the skill again.

This is the third of three sibling CD3 pilots (BGS, OFH, MWS — see
`../../` for the others). Scope for this pilot is the "Recruitment variables"
sheet only — MWS's dictionary has 5 other sheets (`Basic information`,
`Self-reported health at recruit`, `3-year resurvey`, `Dietary data at
3-year resurvey`, `8-year resurvey`), not converted here.

## Conventions

- sentinel not_on_questionnaire (-1) adopted verbatim from the source's own
  code lists, confirmed against the sheet's own Availability columns
  (Aqua/Blue/Other questionnaire versions) -- every field carrying this code
  has 'No' availability for exactly one version · D001
- sentinel missing_numeric (-999) agent-decided for everything else without a
  source-documented code, mirroring the sibling packages' policy · D002
- $id base: https://schemas.example.org/cd3-mws-pilot/ (replace before publishing)
- title separator: — (em dash) · formatting: 2-space, one key per line
- real data: none in this repo; toy fixtures authored from the source's stated
  code lists and valid ranges, or an agent-decided plausibility range where
  the source states neither · D003
- this table has no identifier field at all -- the "Recruitment variables"
  sheet defines none; a participant ID likely lives on a different sheet
  (e.g. "Basic information") not read for this pilot. uniqueItems is declared
  on the mother file but has no ID field to anchor it -- open item · D004
- RNUMFTP's code "10=10 or more" is a real top-coded value, not a missingness
  sentinel -- encoded as its own const branch alongside the 0-9 numeric range · D005
- RCIGSPD's source description states "in current smokers", implying routing
  from RSMOKE, but the source gives no explicit sentinel for the non-smoker
  case -- not enforced as a skip rule, left open · D006

## Categories

| # | category | file | vars | status | touched |
|---|---|---|---|---|---|
| 1 | Body/Lifestyle | recruitment/categories/body_lifestyle.json | 9 | rendered, pending steward review | 2026-08-21 |
| 2 | Reproductive/Pregnancy | recruitment/categories/reproductive_pregnancy.json | 7 | rendered, pending steward review | 2026-08-21 |
| 3 | Breast Health | recruitment/categories/breast_health.json | 2 | rendered, pending steward review | 2026-08-21 |
| 4 | Gynae Surgery | recruitment/categories/gynae_surgery.json | 6 | rendered, pending steward review | 2026-08-21 |
| 5 | Contraceptive | recruitment/categories/contraceptive.json | 4 | rendered, pending steward review | 2026-08-21 |
| 6 | HRT | recruitment/categories/hrt.json | 7 | rendered, pending steward review | 2026-08-21 |
| 7 | Menstrual | recruitment/categories/menstrual.json | 3 | rendered, pending steward review | 2026-08-21 |

38 of 38 "Recruitment variables" properties converted (full sheet, no subset).

## Package milestones

- [x] intake: source registered · grain confirmed · categories proposed (7, derived from content groupings within the sheet -- not re-confirmed individually with the steward before drafting, given established pattern from the sibling packages; flagged for review)
- [x] common/defs.json + mother scaffold validate green
- [ ] every category confirmed by steward
- [ ] cross-category skip audit (D006 open)
- [x] coverage audit 1:1 (38/38, scoped to this sheet)
- [x] pages current
- [ ] review walked · cleanup decided
- [ ] D004 (no ID field) needs resolving before this table could join others

## Session log

- 2026-08-21 · intake + convert all 7 categories · Registered the MWS dictionary's "Recruitment variables" sheet (real header at row 4, data from row 8 -- multi-row header, unlike BGS/OFH), parsed packed code-list cells, discovered and adopted the source's own not_on_questionnaire (-1) sentinel by cross-checking against the Availability columns, drafted all 38 properties across 7 categories, authored fixtures (15 valid rows, 6 invalid cases), rendered both pages, all validate.py checks green. · next: present to steward, including the 7-category breakdown (proposed but not separately re-confirmed this time) and D004 (missing ID field).
