import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import read_json, summarize, validate_bundle, validate_rubric


def fixture():
    dims = list("STAMPED")
    rubric = {
        "version": "0.1.0", "title": "Synthetic", "description": "Test only",
        "source": {"repository": "https://example.org", "revision": "a" * 40,
                   "path": "main.tex", "status": "provisional"},
        "dimensions": [{"id": d, "label": d, "description": d} for d in dims],
        "principles": [{"code": f"{d}.1", "dimension": d, "level": "must", "statement": d} for d in dims],
        "criteria": [{"id": f"{d}-01", "dimension": d, "principles": [f"{d}.1"],
                      "title": d, "question": d, "rationale": d, "evidence_guidance": d,
                      "anchors": [{"value": n, "label": str(n), "description": str(n)}
                                  for n in ([0, 1] if d == "S" else [0, 1, 2, 3])],
                      "source": {"section": d, "locator": "https://example.org"}} for d in dims]}
    assessment = {"id": "first", "reviewer": {"id": "r1", "name": "Reviewer"},
                  "created_at": "2026-10-27T00:00:00Z", "updated_at": "2026-10-27T00:00:00Z",
                  "review_of": None, "weights": {d: 1 for d in dims},
                  "responses": {"S-01": {"score": 1}}, "comment": ""}
    bundle = {"format_version": "1.0.0", "rubric_version": "0.1.0",
              "research_object": {"title": "Synthetic", "locator": "local:test", "revision": "", "scope": ""},
              "assessments": [assessment]}
    return rubric, bundle


class ValidationTests(unittest.TestCase):
    def test_minimal_optional_fields_and_binary_normalization(self):
        rubric, bundle = fixture()
        validate_bundle(bundle, rubric)
        scores = summarize(bundle["assessments"][0], rubric)
        self.assertEqual(scores["dimension_scores"]["S"], 100)
        self.assertAlmostEqual(scores["overall_score"], 100 / 7)
        self.assertFalse(scores["complete"])
        self.assertEqual(scores["answered"], 1)

    def test_unanswered_retains_denominator(self):
        rubric, bundle = fixture()
        criterion = copy.deepcopy(rubric["criteria"][0])
        criterion["id"] = "S-02"
        rubric["criteria"].append(criterion)
        self.assertEqual(summarize(bundle["assessments"][0], rubric)["dimension_scores"]["S"], 50)
        bundle["assessments"][0]["responses"]["S-02"] = {"score": None}
        self.assertEqual(summarize(bundle["assessments"][0], rubric)["dimension_scores"]["S"], 50)

    def test_adjustable_weights(self):
        rubric, bundle = fixture()
        assessment = bundle["assessments"][0]
        assessment["weights"] = {d: int(d == "S") for d in "STAMPED"}
        validate_bundle(bundle, rubric)
        self.assertEqual(summarize(assessment, rubric)["overall_score"], 100)
        self.assertFalse(summarize(assessment, rubric)["complete"])

    def test_evidence_and_confidence_do_not_change_score(self):
        rubric, bundle = fixture()
        assessment = bundle["assessments"][0]
        before = summarize(assessment, rubric)
        assessment["responses"]["S-01"].update({"confidence": "high", "evidence_rating": "sufficient"})
        self.assertEqual(before, summarize(assessment, rubric))

    def test_bad_anchor_and_unknown_criterion(self):
        rubric, bundle = fixture()
        for response in ({"S-01": {"score": 2}}, {"S-99": {"score": 0}}, {"S-01": {"score": True}}):
            bundle["assessments"][0]["responses"] = response
            with self.assertRaises(ValueError):
                validate_bundle(bundle, rubric)

    def test_invalid_weights(self):
        rubric, bundle = fixture()
        for weights in ({d: 0 for d in "STAMPED"}, {d: float("inf") for d in "STAMPED"}):
            bundle["assessments"][0]["weights"] = weights
            with self.assertRaises(ValueError):
                validate_bundle(bundle, rubric)

    def test_review_graph_and_duplicate_ids(self):
        rubric, bundle = fixture()
        first = bundle["assessments"][0]
        second = copy.deepcopy(first)
        second.update(id="second", review_of="first")
        bundle["assessments"].append(second)
        validate_bundle(bundle, rubric)
        first["review_of"] = "second"
        with self.assertRaises(ValueError):
            validate_bundle(bundle, rubric)
        first["review_of"] = "missing"
        with self.assertRaises(ValueError):
            validate_bundle(bundle, rubric)
        first["review_of"] = None
        second["id"] = "first"
        with self.assertRaises(ValueError):
            validate_bundle(bundle, rubric)

    def test_indirect_missing_review_target(self):
        rubric, bundle = fixture()
        first = bundle["assessments"][0]
        second = copy.deepcopy(first)
        first["review_of"] = "second"
        second.update(id="second", review_of="missing")
        bundle["assessments"].append(second)
        with self.assertRaises(ValueError):
            validate_bundle(bundle, rubric)

    def test_version_and_exact_hash(self):
        rubric, bundle = fixture()
        raw = json.dumps(rubric).encode()
        bundle["rubric_sha256"] = hashlib.sha256(raw).hexdigest()
        validate_bundle(bundle, rubric, raw)
        with self.assertRaises(ValueError):
            validate_bundle(bundle, rubric, raw + b"\n")
        bundle["rubric_version"] = "9.0.0"
        with self.assertRaises(ValueError):
            validate_bundle(bundle, rubric, raw)

    def test_rubric_cross_references(self):
        rubric, _ = fixture()
        rubric["criteria"][0]["principles"] = ["S.99"]
        with self.assertRaises(ValueError):
            validate_rubric(rubric)

    def test_strict_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            for text in ('{"a":1,"a":2}', '{"a":NaN}'):
                path.write_text(text)
                with self.assertRaises(ValueError):
                    read_json(path)


if __name__ == "__main__":
    unittest.main()
