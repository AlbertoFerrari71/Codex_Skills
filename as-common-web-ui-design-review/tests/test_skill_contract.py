from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class WebUiDesignReviewSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-web-ui-design-review", text)

    def test_skill_md_avoids_forbidden_operational_strings(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        forbidden = [
            "npx impeccable skills install",
            "npm install",
            "Set-Clipboard",
            "LAST-",
            "latest-",
        ]
        for value in forbidden:
            with self.subTest(value=value):
                self.assertNotIn(value, text)

    def test_skill_md_contains_required_terms(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        lower_text = text.lower()

        for term in ["screenshot", "dashboard", "responsive", "microcopy", "p0"]:
            with self.subTest(term=term):
                self.assertIn(term, lower_text)

        self.assertTrue("accessibility" in lower_text or "accessibilita" in lower_text)
        self.assertTrue("anti-ai-slop" in lower_text or "anti ai slop" in lower_text)

    def test_required_references_exist(self) -> None:
        expected = [
            "review-checklist.md",
            "priority-rubric.md",
            "input-modes.md",
            "anti-ai-slop-patterns.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())

    def test_impeccable_is_not_a_required_dependency(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        dependency_phrases = [
            "richiede impeccable",
            "dipende da impeccable",
            "dipendenza obbligatoria da impeccable",
            "impeccable e' obbligatorio",
            "impeccable è obbligatorio",
        ]
        for phrase in dependency_phrases:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, text)
        self.assertIn("non trattare impeccable come dipendenza obbligatoria", text)

    def test_non_goals_block_automatic_install_and_live_write(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        self.assertIn("non installare impeccable", text)
        self.assertIn("non avviare browser, live mode o scrittura live automatica", text)
        self.assertIn("non scrivere codice senza autorizzazione esplicita", text)


if __name__ == "__main__":
    unittest.main()
