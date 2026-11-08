"""Unit tests for the offline ASO helper scripts."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ASOToolTests(unittest.TestCase):
    def test_keyword_relevance_is_bounded(self):
        result = load("keyword_analyzer").analyze_keyword("task manager", ["task management"], "Productivity")
        self.assertGreaterEqual(result["relevance_heuristic"], 0)
        self.assertLessEqual(result["relevance_heuristic"], 1)

    def test_metadata_limit_validation(self):
        result = load("metadata_optimizer").validate({"title": "x" * 31}, "apple")
        self.assertFalse(result["title"]["valid"])

    def test_competitor_shared_terms(self):
        result = load("competitor_analyzer").analyze([
            {"name": "A", "title": "Task Manager"},
            {"name": "B", "title": "Task Planner"},
        ])
        self.assertIn("task", result["shared_terms"])

    def test_aso_score_range(self):
        result = load("aso_scorer").score({})
        self.assertGreaterEqual(result["overall_score"], 0)
        self.assertLessEqual(result["overall_score"], 100)

    def test_ab_test_sample_size_positive(self):
        result = load("ab_test_planner").sample_size(0.05, 0.1)
        self.assertGreater(result, 0)

    def test_localization_limit_validation(self):
        result = load("localization_helper").validate({"en-US": {"title": "x" * 51}}, "google")
        self.assertFalse(result["en-US"]["title"]["valid"])

    def test_review_analyzer_counts_reviews(self):
        result = load("review_analyzer").analyze([{"text": "Great app, very useful"}])
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["sentiment_counts"]["positive"], 1)

    def test_launch_checklist_is_not_precompleted(self):
        result = load("launch_checklist").build_checklist("both")
        self.assertTrue(result["checklist"])
        self.assertTrue(all(item["complete"] is False for item in result["checklist"]))
        self.assertTrue(any(item["item"].startswith("[Apple]") for item in result["checklist"]))
        self.assertTrue(any(item["item"].startswith("[Google]") for item in result["checklist"]))


if __name__ == "__main__":
    unittest.main()
