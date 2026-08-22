# UK Generations Study — R0 Questionnaire (schemify pilot) — conversion progress

package: GS_Schemify_Pilot/json_schema · started: 2026-08-21
grain: One element is one participant's R0 (baseline) questionnaire response.
dictionary: BaselineMetadata.xlsx (Questions, Answers, ArrayDef, DataDictionary sheets) — full inventory in SOURCES.md

## How to continue

This conversion runs over several sittings — an agent session can hold only so
much at once, so the work is planned in units that each fit one session. Nothing
is lost between sittings: this file is the memory.

To continue at any time: open a fresh agent session in this package's directory
and invoke the skill again. The agent reads this file and proposes the next
unit. You can also ask for anything directly — a specific category, a change,
a question, the final review.

This package is a **pilot**: it exists to test whether the schemify approach
is worth adopting for the full R0 pipeline before committing to all 19
categories. Only `general_information` has been converted so far, deliberately.

## Conventions

- sentinels: -999 (missing_numeric) · "MISSING" (missing_string) — agent-decided,
  since BaselineMetadata.xlsx defines no dedicated missing-value code for most
  fields · D001. Plus three harmonised sentinels adopted from the source's own
  AnswerID system: AnswerID=3 "Don't know", AnswerID=5 "Don't remember",
  AnswerID=6 "Not applicable" · D002
- $id base: https://schemas.example.org/gs-r0-pilot/ (replace before publishing)
- grain: see header · title separator: — (em dash) · formatting: 2-space, one key per line
- real data: none in this repo; toy fixtures authored from the dictionary's value
  space only · D003
- companion flag-field pattern: some "don't know"/"not applicable" answers are
  captured as a separate paired boolean field (e.g. R0_GPdk alongside R0_GP)
  rather than an inline sentinel branch, when the primary field is a date, name,
  or other free-entry type that can't cleanly hold a sentinel value · D004

## Categories

| # | category | file | vars | source slice | status | touched |
|---|---|---|---|---|---|---|
| 1 | General Information | r0_questionnaire/categories/general_information.json | 41 | BaselineMetadata.xlsx Questions where SchemaFile=GeneralInformation_Schema.json | confirmed pending steward review | 2026-08-21 |
| 2 | Contraceptive HRT | r0_questionnaire/categories/contraceptive_hrt.json | 19 | BaselineMetadata.xlsx Questions where SchemaFile=ContraceptiveHRT_Schema.json | pending | — |
| 3 | Menstrual Menopause | r0_questionnaire/categories/menstrual_menopause.json | 29 | ...MenstrualMenopause_Schema.json | pending | — |
| 4 | Pregnancies | r0_questionnaire/categories/pregnancies.json | 23 | ...Pregnancies_Schema.json | pending | — |
| 5 | Birth Details | r0_questionnaire/categories/birth_details.json | 42 | ...BirthDetails_Schema.json | pending | — |
| 6 | Physical Development | r0_questionnaire/categories/physical_development.json | 35 | ...PhysicalDevelopment_Schema.json | pending | — |
| 7 | Physical Activity | r0_questionnaire/categories/physical_activity.json | 36 | ...PhysicalActivity_Schema.json | pending | — |
| 8 | Alcohol Smoking Diet | r0_questionnaire/categories/alcohol_smoking_diet.json | 47 | ...AlcoholSmokingDiet_Schema.json | pending | — |
| 9 | Other Lifestyle Factors | r0_questionnaire/categories/other_lifestyle_factors.json | 28 | ...OtherLifestyleFactors_Schema.json | pending | — |
| 10 | Jobs | r0_questionnaire/categories/jobs.json | 13 | ...Jobs_Schema.json | pending | — |
| 11 | Breast Disease | r0_questionnaire/categories/breast_disease.json | 12 | ...BreastDisease_Schema.json | pending | — |
| 12 | Breast Cancer | r0_questionnaire/categories/breast_cancer.json | 3 | ...BreastCancer_Schema.json | pending | — |
| 13 | Other Breast Surgery | r0_questionnaire/categories/other_breast_surgery.json | 7 | ...OtherBreastSurgery_Schema.json | pending | — |
| 14 | Mammograms | r0_questionnaire/categories/mammograms.json | 11 | ...Mammograms_Schema.json | pending | — |
| 15 | XRays | r0_questionnaire/categories/xrays.json | 19 | ...XRays_Schema.json | pending | — |
| 16 | Cancer Relatives | r0_questionnaire/categories/cancer_relatives.json | 63 | ...CancerRelatives_Schema.json | pending | — |
| 17 | MH Illnesses | r0_questionnaire/categories/mh_illnesses.json | 21 | ...MH_Illnesses_Schema.json | pending | — |
| 18 | MH Cancers Benign Tumors | r0_questionnaire/categories/mh_cancers_benign_tumors.json | 3 | ...MH_CancersBenignTumors_Schema.json | pending | — |
| 19 | MH Drugs Supplements | r0_questionnaire/categories/mh_drugs_supplements.json | 48 | ...MH_DrugsSupplements_Schema.json | pending | — |

Var counts for categories 2–19 are from the existing raw schema property counts
(GS_Schema_Generator output), carried over for planning only — not yet verified
against BaselineMetadata.xlsx directly.

## Package milestones

- [x] intake: sources registered · grain confirmed · categories confirmed (all 19, pilot scope: convert #1 only)
- [x] common/defs.json + mother scaffold validate green
- [ ] every category confirmed (1 of 19 drafted/validated/rendered; steward confirmation still open)
- [ ] cross-category skip audit
- [x] coverage audit 1:1 (for the converted category; full-package coverage pending remaining categories)
- [x] pages current for the converted category
- [ ] review walked · cleanup decided

## Session log

- 2026-08-21 · intake + convert general_information · Registered BaselineMetadata.xlsx, proposed and derived the 19-category table from existing GS_Schema_Generator output, scaffolded package, drafted general_information (41 properties), authored fixtures (23 valid rows, 8 invalid cases), added the R0_GPdk/R0_GP skip pattern, rendered dictionary.html + playground.html, all validate.py checks green (check/fixtures/coverage). Pilot scope only — 18 categories remain unconverted. · next: present general_information to the steward for confirmation; decide whether to continue to category 2 or stop here as a completed pilot.
