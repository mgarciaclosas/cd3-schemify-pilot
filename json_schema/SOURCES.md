# Sources — UK Generations Study R0 Questionnaire (schemify pilot)

## Dictionary files

- `BaselineMetadata.xlsx` (at `/Users/mclosas/Claude sessions/GS_Schema_Generator/BaselineMetadata.xlsx`) · Excel, 8 sheets · `Questions` (1868 rows: QuestionID, RoundID, Section, QuestionTypeID, QuestionText, VariableName, NewVariableName, PII, ArrayName, description, checkbox, minimum, maximum, SchemaFile, SchemaPropertyName) and `Answers` (1301 rows: QuestionID, RoundID, AnswerID, AnswerText, AnswerDataType, AnswerCode, ShortDescription, OriginalAnswerID) are the two sheets actually used so far; `AnswerID` is a harmonised code reused across questions with the same meaning (distinct from the per-question `AnswerCode`, and from `OriginalAnswerID`, its pre-harmonisation predecessor). `Rounds`, `QuestionTypes`, `SchemaMetadata`, `QuestionHierarchy`, `DataDictionary`, `ArrayDef` not yet read for this pilot. Registered 2026-08-21.
- Existing generated schemas, read for cross-reference only (not as source-of-truth — BaselineMetadata.xlsx is): `GS_Schema_Generator/schemas_generated/GeneralInformation_Schema.json` and the canonical copy at `Schema_and_Derivation_Utils/Questionnaire/R0/schemas/raw/GeneralInformation_Schema.json` (identical content) · registered 2026-08-21.

## External sources

- None consulted for this pilot.

## The steward

- The steward is maintaining the UK Generations Study schema pipeline (Schema_and_Derivation_Utils repo) and the GS_Schema_Generator tooling that currently produces these schemas.
- First-hand: overall pipeline architecture and history; pointed out the AnswerID harmonisation directly, which corrected an initial gap in the agent's sentinel-source check (D002).
- Ask here: which categories to prioritise beyond this pilot, whether the -999/MISSING sentinel choice (D001) should change, real-data access rulings, whether to proceed past this one pilot category.
- Not here / stays open: whatever BaselineMetadata.xlsx itself doesn't state — logged as `open` decisions in DECISIONS.md as they arise (none open as of this pilot).
