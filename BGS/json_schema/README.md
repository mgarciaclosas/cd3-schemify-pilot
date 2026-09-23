# BGS — Generations Study baseline derived variables (JSON Schema package)

A machine-checkable version of the Generations Study (Breast Cancer Now Generations Study) R0 derived-variables dictionary, built for the CD3 harmonisation pilot. The schemas validate delivered data; two web pages let people browse them.

Decision numbers such as D016 point to `DECISIONS.md` if that file is kept beside this package. Each one is also stated in words where it matters.

## 1. What this package describes

The Generations Study is a prospective UK cohort of more than 100,000 women, followed for the causes of breast cancer. This package covers the analysis-ready variables the study derives from its baseline (R0) questionnaire.

| Table | Mother file | One row is | Categories |
|---|---|---|---|
| `derived_variables` | `derived_variables/derived_variables.schema.json` | one participant's baseline (R0) analysis-ready derived variables, keyed by `TCode` | identification (1), demographics (2), anthropometric (11), reproductive_hormonal (20), medical_history (4), behavioral (12), family_history (10) — 60 variables |

## 2. Layout and composition

```
json_schema/
├── common/defs.json                       shared sentinel codes and the TCode pattern
├── derived_variables/
│   ├── derived_variables.schema.json      the table: an array of row objects
│   └── categories/*.json                  one file per category
├── examples/                              toy rows: valid, invalid, and the ledger of seeded violations
├── tools/validate.py                      the validator (Python)
├── dictionary.html, playground.html       the two web pages
├── VARIABLES.csv, ROUTING.csv             the variable inventory and the routing register
└── assets/                                what the pages need
```

A row is the `allOf` union of its seven category files, followed by the conditional rules (section 5). The mother file's single `unevaluatedProperties: false` rejects any column not declared in a category, so an unknown column is an error. Every column is required in every row: a value is never left out and never `null`.

## 3. Value-encoding conventions

- **Codes get `oneOf`.** A coded variable is a `oneOf` of single-value branches, each with its label (for example 0 "No", 1 "Yes").
- **Measures get `anyOf`.** A measured variable is one numeric branch plus one branch per special code.
- **Titles** are the source dictionary's own description text, word for word. The source has no questionnaire wording, so no separate description is added.
- **Ranges** are the source's own, including its exclusive ends (height above 0 and below 320). Where the source states no upper limit (parity, ages, servings, alcohol units, cigarettes, physical activity), none is added.
- **`x-derivation`** carries the source's derivation prose. Each property's `$comment` carries its former name, a formula where there is one, and any rule or defect note.
- **`$id` namespace:** `https://schemas.example.org/cd3-bgs-pilot/` is a placeholder. Replace it before publishing the schemas anywhere public.

## 4. Sentinel semantics

| Code | Meaning | Where it applies |
|---|---|---|
| `-999` | Missing: no valid value was derived. It replaces the source's bare `null`, which the source glosses as "Missing or invalid", "Unknown" or "Left blank". | every property except `TCode` |
| `9999` | Not applicable: the derivation is structurally inapplicable. Adopted from the source's own code. | `R0_PregAt20`, `R0_Height20`, `R0_Weight20`, `R0_BMI20`, `R0_BMI`, `R0_WaistHipRatio`, `R0_AgeStartedOC`, `R0_AgeLastUsedOC`, `R0_OCLength`, `R0_AgeFFTP`, `R0_AgeLFTP`, `R0_BreastfeedingDuration`, `R0_Breastfed` |

Codes that look like sentinels but are real levels: `R0_Parous` -1 (never pregnant) and 9 (ever pregnant, parity unknown); `R0_Menopause` 9 (never had periods); `R0_Ethnicity` 9 ("Not known", the source's own code).

`-999` is agent-proposed and steward-approved, because the source has no numeric missing code. It collapses the source's three `null` glosses into one code.

## 5. Enforced routing rules

Policy: strict. Only rules the source states, or clearly implies, are enforced; none is added from study design. The list below is taken from the mother file.

- **R001 skip:** pregnant at age 20 (`R0_PregAt20` = 1) means `R0_BMI20` is 9999. Source: "If AgeEntry < 20 or R0_PregAt20 == 1, BMI is set to 9999."
- **R001 applicability:** `R0_PregAt20` = 0 means `R0_BMI20` must not be 9999. The source sets `R0_PregAt20` to 9999 for anyone under 20, so 0 implies the participant was 20 or over.
- **R002 skip:** pregnant at baseline (`R0_PregAtEntry` = 1) means `R0_BMI` and `R0_WaistHipRatio` are 9999. The source names `R0_CurrentPreg` (not delivered); `R0_PregAtEntry` is a straight copy of it.
- **R002 applicability:** `R0_PregAtEntry` = 0 means neither may be 9999.
- **R003 skip:** `R0_Parous` of -1 or 0 (no live birth) means `R0_AgeFFTP`, `R0_AgeLFTP`, `R0_BreastfeedingDuration` and `R0_Breastfed` are all 9999. Source: "9999 (NA) if no live-birth pregnancies".
- **R003 applicability:** `R0_Parous` = 1 means `R0_Breastfed` and `R0_BreastfeedingDuration` must not be 9999. There is no reverse half for the two age fields, because the source also gives them 9999 when dates are missing.
- **R004:** `R0_DiabetesStatus` of 0 or -999 means `R0_AgeDiabetes` is -999. Source: "only retained if R0_DiabetesStatus=1". With status 1 the age is a number or -999.

## 6. Documented but not enforced

Rules a consumer should check downstream, because JSON Schema cannot express them:

- **Age at menarche:** `R0_AgeMenarche` should be missing when the questionnaire says the participant never had periods. `R0_EverHadPeriods` is not delivered.
- **Under 20 at baseline:** `R0_BMI20` and `R0_PregAt20` should be 9999 when `AgeEntry` < 20. `AgeEntry` is not delivered.
- **Arithmetic:** `R0_BMI20` = `R0_Weight20` / (`R0_Height20` / 100)² and `R0_BMI` = `R0_Weight` / (`R0_Height` / 100)², each rounded to 1 decimal. `R0_WaistHipRatio` = `R0_WaistCircum` / `R0_HipCircum`, rounded to 2 decimals.
- **Reproductive consistency:** `R0_Parity` should be 0 when `R0_Parous` is -1 or 0; `R0_AgeFFTP` should not exceed `R0_AgeLFTP`; `R0_AgeStartedOC` should not exceed `R0_AgeLastUsedOC`; `R0_HRTStartAge` should not exceed `R0_HRTStopAge`; `R0_OCLength` and `R0_HRTDuration` should agree with their ages.
- **Family history:** for each of the five sites, the count (`R0_FamHist…Num`) should be at least 1 when its flag is 1, and 0 when its flag is 0.
- **Declined by the steward:** R006 and R007 (`R0_AlcoholUnitsPerWeek` among current drinkers; `R0_CigsPerDay` among current smokers). The source titles limit these fields to current drinkers and smokers, but neither field has a not-applicable code. The rows wait in `ROUTING.csv` and can be enforced later.
- **9999 with no stated trigger:** `R0_Height20`, `R0_Weight20`, `R0_AgeStartedOC`, `R0_AgeLastUsedOC` and `R0_OCLength` accept 9999, but the source never says when. No rule is attached.
- **Row uniqueness:** `TCode` uniqueness across rows cannot be checked by JSON Schema; `uniqueItems` only rejects identical rows.

## 7. Known source issues handled

- **`R0_PhysicalActivity` unit:** the source title says "hours/week", but its derivation text says MET-hours per week. The title is kept as it is, the defect is noted in the property, and the unit is undecided.
- **`R0_PregAtEntry` codes:** the derived-variables schema declares 0 = No, 1 = Yes. The derivation notebook copies `R0_CurrentPreg` unchanged, which the legacy Pregnancies schema codes as 0 = more than one option chosen, 1 = Yes, 2 = No, 3 = Not sure (default 2). Delivered data may therefore carry 2 or 3, which this package rejects. The declared 0/1 is kept and the defect noted.
- **`R0_Height20`:** the source lists `R0_RecWght_Num` where its own derivation text says `R0_RecHght_Num`. Noted in the property.
- **Oral contraceptive fields:** the source descriptions say "null if never used", yet the fields carry a 9999 branch. Kept as the source has it.
- **Family history text:** the source derivation text for four fields reads "equals contains" [sic]. Kept as the source has it.
- **Empty source entries:** a few properties have an empty `x-formerName` or `x-calculation`. They are left out.
- **Not carried over:** the source's `x-derivedFrom` lineage and its questionnaire answer IDs (`x-answerIDs`). The lineage remains in the source file.

## 8. Sources and provenance

- `DerivedVariables_Schema.json`, from the Generations Study repository (`Questionnaire/R0/…/DerivedVariables_Schema.json`). JSON Schema draft 2020-12, 60 properties. Registered 2026-09-15.
- Generations Study schema repository, https://github.com/UK-Generations-Study/Schema_and_Derivation_Utils. Consulted 2026-09-21:
  - `Documentation/JSON Schema Conventions.md`: `null` means "Missing or invalid", 9999 means not applicable, and it gives no skip-logic guidance.
  - `Questionnaire/R0/scripts/Derivation.ipynb`, read as a raw file: used to check how `R0_PregAtEntry` and the 9999 rules are computed.
  - The legacy Pregnancies schema, read from a local copy: used for `R0_CurrentPreg` coding.
- `Questionnaire/R0/README.pdf` and `R0_workflow.pdf` were not read.
- The steward answered all questions on the study and the choices made here.

## 9. Validating and browsing

```
pip install -r tools/requirements.txt      # or use: uv run tools/validate.py …
python3 tools/validate.py summary .        # schemas, fixtures, coverage — everything
python3 tools/validate.py data . --file your_export.csv
```

- Double-click `dictionary.html`. Keyword search is built in; the Semantic search switch fetches a small model once, then also finds related variables by meaning.
- Run `python3 -m http.server 8000` from this folder, then open `http://localhost:8000/playground.html`. Serve the whole folder so `assets/vendor/` travels with the page.
- Data files use the in-band codes above (`-999`, `9999`), never blanks.

Current state: 9 schema files valid, 60 of 60 variables converted, 7 conditionals, 9 valid toy rows and 51 seeded violations all caught.

## 10. Open items to confirm with the data provider

- Which unit `R0_PhysicalActivity` is in: hours per week, or MET-hours per week.
- Whether delivered `R0_PregAtEntry` uses 0/1, as declared, or the questionnaire's 0/1/2/3.
- Whether the five 9999 fields with no stated trigger should get a rule, and whether R006 and R007 (current drinkers, current smokers) should be enforced with a not-applicable code.
- No real data was available; only toy rows were used. A run of `validate.py data` against delivered data would test these points.
