# Sources — CD3 pilot: BGS (Breast Cancer Now Generations Study) derived variables

## Dictionary files

- `DerivedVariables_Schema.json` (at `/Users/mclosas/Claude sessions/Schema_and_Derivation_Utils/Questionnaire/R0/schemas/derived/DerivedVariables_Schema.json`) · JSON Schema, draft 2020-12 · 60 properties describing one participant's R0 analysis-ready derived variables; each property carries `x-description` (derivation logic in prose), `x-derivedFrom` (source field pointers or, for the 10 R0_FamHist* properties, legacy SAS script paths), `x-calculation` (formula, where applicable), `x-formerName` (legacy variable name). Registered 2026-08-21.

## External sources

- None consulted for this pilot.

## The steward

- The steward is maintaining the BGS (Breast Cancer Now Generations Study) schema pipeline (Schema_and_Derivation_Utils repo) and directing this CD3 multi-cohort pilot (BGS, OFH, MWS as sibling packages).
- First-hand: overall derivation logic and pipeline history; directed the full-conversion scope (all 60 properties, not a subset) and the 12-category breakdown (confirmed as proposed).
- Ask here: whether D007's open cross-field routing question should be resolved by adding NA branches to fields like R0_AgeMenopause, category prioritisation for OFH/MWS, real-data access rulings.
- Not here / stays open: D007 (cross-field routing) is the one open decision as of this pilot.
