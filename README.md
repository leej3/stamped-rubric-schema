# STAMPED rubric schema

A manuscript-derived rubric for assessing how a **research object** supports the seven STAMPED dimensions.
A DOI, publication, directory, or repository can be the entry point.
Follow the evidence it makes discoverable, and retain the path by which evidence was found.

This is a developmental pilot, not a validated general measure of scientific quality or a certification scheme.
Scores describe this rubric and its chosen weights.
They do not establish a universal ordering of research objects.

## Contents

- `rubric.json`: the versioned principles, criterion-specific anchors, evidence guidance, and manuscript source mappings.
- `stamped-rubric-schema.yaml`: LinkML semantic model, analogous to the existing STAMPED principles and checklist models.
- `schemas/rubric.schema.json`: exact rubric JSON contract (Draft 2020-12).
- `schemas/assessment-bundle.schema.json`: exact multi-reviewer JSON contract.
- `scripts/validate.py`: structural validation, cross-record checks, and reference scoring implementation.
- `docs/assessment-protocol.md`: workflow shared by people and agents.
- `docs/rubric-method.md`: criterion construction and source coverage.
- `examples/paper-remodnav.json`: worked source-based assessment.
- `docs/paper-remodnav-assessment.md`: scope and limitations of that example.

The LinkML model expresses the entities and relationships.
JSON Schema defines wire details such as explicit null scores and criterion-keyed response objects; the Python validator adds rules that JSON Schema cannot express conveniently.
Both contracts are maintained together.
JSON Schemas are checked-in authored artifacts, not represented as generated LinkML output.

## Validate and inspect scores

With Python 3.11+ and [uv](https://docs.astral.sh/uv/):

```sh
uv sync --locked --no-dev
uv run --no-dev python scripts/validate.py
uv run --no-dev python scripts/validate.py examples/paper-remodnav.json --scores
uv run --no-dev python -m unittest discover -s tests -v
```

Development tools, including LinkML and the Snapper documentation hook, are in the locked `dev` dependency group:

```sh
uv sync --locked
uv run pre-commit install
uv run pre-commit run snapper --all-files
```

The sibling website repository, `stamped-rubric`, imports snapshots of the JSON contracts and content.
Its import/export format is the assessment bundle.

## Scoring contract

Each criterion contributes its selected anchor value divided by its maximum.
Binary anchors are 0–1; graded anchors are 0–3.
Within a dimension, criterion contributions have equal weight:

```text
dimension = 100 × sum(score / maximum) / number_of_criteria
overall = sum(dimension × dimension_weight) / sum(dimension_weights)
```

All criteria remain in the denominator.
Missing responses and explicit null scores contribute zero to the provisional total but remain distinguishable from an assigned zero.
Every report includes completion counts.
A zero-weight dimension still displays its own score and incomplete status; its contribution to the overall score is zero.
At least one dimension weight must be positive.

Dimension weights default to one and are adjustable.
Store all seven weights in every assessment.
Do not compare totals without considering both the profile and the weights.
Evidence ratings, confidence, rationale, feedback, and improvement flags never alter scores.

There is no discretionary exclusion or N/A denominator adjustment in this pilot.
Record applicability objections as criterion feedback.
Future explicit applicability rules require a new rubric version; never silently rewrite old assessments.

## Multiple reviewers and provenance

An assessment identifies its reviewer without treating human and agent contributors differently.
Each has its own responses, weights, and comments.
An assessment may reference an earlier one through `review_of`; originals remain available and scores are not automatically averaged.
Review references must be acyclic and point within the bundle.

A report records the rubric version and, preferably, `rubric_sha256`: SHA-256 of **the exact bytes of `rubric.json`**, including formatting and its final newline.
If a digest is supplied, mismatches fail validation.
Version-only imports are accepted for authoring convenience but provide weaker provenance; full exports should include the digest.
Do not silently migrate a version mismatch.

The rubric records the exact manuscript commit inspected, with source status `provisional` until the manuscript reconciliation is finalized.
This identifies the working source; it does not claim the final upstream pin is already settled.

## Attribution and license

Distributed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt), matching the source STAMPED repositories.
Principles and manuscript-derived content are adapted from the [STAMPED manuscript](https://github.com/stamped-principles/stamped-paper), with revision-specific links in `rubric.json`.
The rubric's operational anchors are new interpretations and should not be mistaken for verbatim manuscript claims.
The manuscript authors and STAMPED Principles contributors retain attribution.

The development approach uses observable anchors, traceable evidence, and explicit missingness; see `docs/assessment-protocol.md` for its scope and the review questions used in the pilot.
