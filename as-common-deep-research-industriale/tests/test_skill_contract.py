from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class DeepResearchIndustrialeSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-deep-research-industriale", text)

    def test_trigger_boundary_terms_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        required_terms = [
            "materiali",
            "prodotti chimici",
            "norme tecniche",
            "scouting fornitori",
            "brevetti usati come fonte tecnica",
            "stime tecnico-economiche",
            "quando non usarla",
        ]
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_source_and_uncertainty_contract_is_explicit(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["fatti verificati", "fonti e citazioni", "stime", "ipotesi", "raccomandazioni operative"]:
            with self.subTest(term=term):
                self.assertIn(term, text)
        self.assertIn("tema e' aggiornabile", text)

    def test_required_references_exist(self) -> None:
        expected = [
            "research-output-rubric.md",
            "source-quality-and-uncertainty.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())


if __name__ == "__main__":
    unittest.main()
