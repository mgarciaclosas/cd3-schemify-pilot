# Sources — CD3 pilot: Our Future Health (participant + questionnaire)

## Dictionary files

- `our_future_health_data_dictionary_v14.xlsx` (at `/Users/mclosas/Claude sessions/CD3 metadata harmonisation/CD3_OFH_Schema/raw_data/`) · Excel, 8 sheets (`README`, `participant`, `questionnaire`, `clinic_measurements`, `poct_lipid_profile`, `participant_geographies`, `linked_nhse_health_records`, `genetic_data`); `participant` (14 rows) and `questionnaire` (359 rows) read for this pilot. Columns: `entity`, `name`, `type`, `primary_key_type`, `coding_name`, `is_sparse_coding`, `is_multi_select`, `referenced_entity_field`, `relationship`, `folder_path`, `title`, `units`, `description`. Relational: `referenced_entity_field`/`relationship` link entities to `participant:PID` (many_to_one) -- confirmed `questionnaire` has its own local primary key (`ID`) and is many_to_one to participant, a genuinely different grain. `questionnaire`'s `folder_path` values map directly to its 6 source sections (`Questionnaire Information`, `1 About you and your household`, `2 Work and education`, `3 Your lifestyle`, `4 Family health history`, `5 Your health history`) -- used as this pilot's category breakdown verbatim, not inferred. Registered 2026-08-21.
- `our_future_health_codings_v14.xlsx` (same folder) · Excel, 10 sheets; `participant` (46 rows, filtered to 8 coding_names) and `questionnaire` (filtered to 353 coding_names used by questionnaire fields) sheets read. Columns: `coding_name`, `code`, `meaning`, `display_order`, `parent_code`. Full-table scan (not sampling) found 4 invariant codes reused across many fields with a single consistent meaning: -1 "Do not know", -3 "Prefer not to answer", -7 "None of the above", -999 "Suppressed"; also found several numerals reused with *context-dependent*, non-invariant meanings (e.g. -10, -2, 0), correctly not centralised. Registered 2026-08-21.

## External sources

- None consulted for this pilot.

## The steward

- Directing this CD3 multi-cohort pilot (BGS, OFH, MWS as sibling packages); confirmed OFH's scope should expand beyond `participant` to include `questionnaire` in full ("too little information" from `participant` alone).
- Ask here: whether D002's open non-nullability calls should stand, D008's multi-select shape ambiguity (highest priority — affects 134 of 373 total properties), D009's height/weight unit ambiguity, scope for the remaining 5 OFH domains, whether D005's DEMOG_SEX_1_1/DEMOG_SEX_2_1 relationship should be formalised.
- Not here / stays open: D002, D005, D008, D009, D011 (sparse-coding categorical-vs-continuous call) as of this pilot.
