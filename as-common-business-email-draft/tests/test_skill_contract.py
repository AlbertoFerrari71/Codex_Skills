from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class BusinessEmailDraftSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-business-email-draft", text)

    def test_alberto_tone_and_email_outputs_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["logiche", "empatiche", "ferme", "oggetto", "versione pronta", "rischi relazionali"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_anti_triggers_and_boundaries_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["quando non usarla", "prompt codex", "runbook tecnico", "ui review", "non inventare promesse"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_required_references_exist(self) -> None:
        expected = [
            "alberto-email-tone-rubric.md",
            "delicate-email-risk-checklist.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())


if __name__ == "__main__":
    unittest.main()
