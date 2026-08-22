# Sources — CD3 pilot: Million Women Study recruitment variables

## Dictionary files

- `millionwomenstudydatadictionary-v1-21.xlsx` (at `/Users/mclosas/Claude sessions/CD3 metadata harmonisation/CD3_MWS_Schema/raw_data/`) · Excel, 6 sheets (`Basic information`, `Recruitment variables`, `Self-reported health at recruit`, `3-year resurvey`, `Dietary data at 3-year resurvey`, `8-year resurvey`); only `Recruitment variables` read for this pilot. Parse notes: real header is row 4 (`Field Name` split into `Short`/`Long` sub-columns, `Description`, `Valid range` split into `From`/`To`, `Availability for questionnaire versions` split into `Aqua`/`Blue`/`Other`, `Code list`), with two further header/sub-header rows (row 5: version names again; row 6: availability percentages) before data starts at row 7 (first data row read at row 8 in 1-indexed terms via openpyxl's read_only iterator). Code lists are packed into a single cell as newline-separated `code=label` pairs, not one row per code (contrast with BGS/OFH, both of which use one row per code). Registered 2026-08-21.

## External sources

- None consulted for this pilot.

## The steward

- Directing this CD3 multi-cohort pilot (BGS, OFH, MWS as sibling packages); confirmed MWS's scope as the "Recruitment variables" sheet specifically.
- Ask here: whether the 7-category breakdown (D007) should stand, where the real participant ID field lives (D004), whether RCIGSPD/RSMOKE routing (D006) should be formalised.
- Not here / stays open: D004 (ID field location), D006 (RCIGSPD routing), D007 (category breakdown confirmation) as of this pilot.
