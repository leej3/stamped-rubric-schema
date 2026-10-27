"""Validate structure and cross-record invariants; optionally summarize scores."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = tuple("STAMPED")


def read_json(path: Path) -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"Non-finite JSON number: {value}")

    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_constant=reject_constant)


def check_schema(value: Any, filename: str) -> None:
    schema = read_json(ROOT / "schemas" / filename)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(value), key=lambda e: str(list(e.path)))
    if errors:
        details = [f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}"
                   for e in errors]
        raise ValueError("\n".join(details))


def unique(records: list[dict], field: str, context: str) -> set[str]:
    values = [record[field] for record in records]
    if len(set(values)) != len(values):
        raise ValueError(f"Duplicate {context} {field}")
    return set(values)


def validate_rubric(rubric: dict) -> None:
    check_schema(rubric, "rubric.schema.json")
    dimensions = unique(rubric["dimensions"], "id", "dimension")
    if dimensions != set(DIMENSIONS):
        raise ValueError("Exactly the seven STAMPED dimensions are required")
    principles = unique(rubric["principles"], "code", "principle")
    unique(rubric["criteria"], "id", "criterion")
    mapped = set()
    for principle in rubric["principles"]:
        if not principle["code"].startswith(principle["dimension"] + "."):
            raise ValueError(f"Principle dimension mismatch: {principle['code']}")
    for criterion in rubric["criteria"]:
        cid = criterion["id"]
        if not cid.startswith(criterion["dimension"] + "-"):
            raise ValueError(f"Criterion dimension mismatch: {cid}")
        refs = criterion["principles"]
        if len(set(refs)) != len(refs) or not set(refs) <= principles:
            raise ValueError(f"Invalid principle references: {cid}")
        if not any(ref.startswith(criterion["dimension"] + ".") for ref in refs):
            raise ValueError(f"No same-dimension principle source: {cid}")
        values = [anchor["value"] for anchor in criterion["anchors"]]
        if values not in ([0, 1], [0, 1, 2, 3]):
            raise ValueError(f"Anchors must be ordered 0–1 or 0–3: {cid}")
        mapped.update(refs)
    if mapped != principles:
        raise ValueError(f"Unmapped principles: {sorted(principles - mapped)}")
    covered = {criterion["dimension"] for criterion in rubric["criteria"]}
    if covered != dimensions:
        raise ValueError("Every dimension needs at least one criterion")


def validate_bundle(bundle: dict, rubric: dict, rubric_bytes: bytes | None = None) -> None:
    validate_rubric(rubric)
    check_schema(bundle, "assessment-bundle.schema.json")
    if bundle["rubric_version"] != rubric["version"]:
        raise ValueError("Rubric version mismatch; migration must be explicit")
    if "rubric_sha256" in bundle:
        if rubric_bytes is None:
            raise ValueError("Exact rubric bytes required to verify rubric_sha256")
        actual = hashlib.sha256(rubric_bytes).hexdigest()
        if bundle["rubric_sha256"] != actual:
            raise ValueError("Rubric SHA-256 mismatch; use the exact referenced rubric")
    assessments = bundle["assessments"]
    ids = unique(assessments, "id", "assessment")
    by_id = {a["id"]: a for a in assessments}
    criteria = {c["id"]: c for c in rubric["criteria"]}
    for assessment in assessments:
        target = assessment["review_of"]
        if target is not None and target not in ids:
            raise ValueError(f"Unknown review target: {assessment['id']}")
    for assessment in assessments:
        aid = assessment["id"]
        seen = set()
        current = aid
        while current is not None:
            if current in seen:
                raise ValueError(f"Cycle in review references: {aid}")
            seen.add(current)
            current = by_id[current]["review_of"]
        weights = list(assessment["weights"].values())
        if not all(math.isfinite(value) for value in weights) or sum(weights) <= 0:
            raise ValueError(f"Weights must be finite and have positive sum: {aid}")
        for cid, response in assessment["responses"].items():
            if cid not in criteria:
                raise ValueError(f"Unknown criterion {cid} in {aid}")
            score = response["score"]
            allowed = {a["value"] for a in criteria[cid]["anchors"]}
            if score is not None and (isinstance(score, bool) or score not in allowed):
                raise ValueError(f"Invalid anchor score {score} for {cid} in {aid}")
            if score is not None and response.get("observation") == "not_assessed":
                raise ValueError(f"Rated response cannot be marked not_assessed: {cid}")


def summarize(assessment: dict, rubric: dict) -> dict:
    """Scores use all criterion denominators, even when responses are absent."""
    dimension_scores = {}
    answered = 0
    for dimension in DIMENSIONS:
        criteria = [c for c in rubric["criteria"] if c["dimension"] == dimension]
        total = 0.0
        for criterion in criteria:
            score = assessment["responses"].get(criterion["id"], {}).get("score")
            if score is not None:
                answered += 1
                total += score / max(a["value"] for a in criterion["anchors"])
        dimension_scores[dimension] = 100 * total / len(criteria)
    weights = assessment["weights"]
    overall = sum(dimension_scores[d] * weights[d] for d in DIMENSIONS) / sum(weights.values())
    return {"assessment_id": assessment["id"], "dimension_scores": dimension_scores,
            "overall_score": overall, "weights": weights, "answered": answered,
            "total": len(rubric["criteria"]), "complete": answered == len(rubric["criteria"])}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assessments", type=Path, nargs="*")
    parser.add_argument("--rubric", type=Path, default=ROOT / "rubric.json")
    parser.add_argument("--scores", action="store_true")
    args = parser.parse_args()
    try:
        rubric = read_json(args.rubric)
        validate_rubric(rubric)
        for path in args.assessments:
            bundle = read_json(path)
            validate_bundle(bundle, rubric, args.rubric.read_bytes())
            if args.scores:
                print(json.dumps([summarize(a, rubric) for a in bundle["assessments"]], indent=2))
            else:
                print(f"Valid: {path}")
        if not args.assessments:
            print(f"Valid rubric: {args.rubric}")
    except (ValueError, OSError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
