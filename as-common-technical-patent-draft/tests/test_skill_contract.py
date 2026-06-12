from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class TechnicalPatentDraftSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-technical-patent-draft", text)

    def test_legal_boundaries_are_explicit(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        required_terms = [
            "non sostituisce il consulente brevettuale",
            "claim draft",
            "bozza tecnica non legale",
            "freedom-to-operate",
            "validita brevettuale garantita",
            "contraffazione",
        ]
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_output_sections_support_disclosure(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["problema tecnico", "soluzione proposta", "varianti", "disegni/figure", "domande per il consulente"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_required_references_exist(self) -> None:
        expected = [
            "invention-disclosure-checklist.md",
            "legal-boundary-notes.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())


if __name__ == "__main__":
    unittest.main()
