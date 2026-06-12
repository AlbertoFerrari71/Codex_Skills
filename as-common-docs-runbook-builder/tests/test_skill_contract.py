from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class DocsRunbookBuilderSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-docs-runbook-builder", text)

    def test_runbook_structure_terms_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["runbook operativo", "procedura ripetibile", "prerequisiti", "verifiche", "rollback / stop", "troubleshooting", "ownership"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_overlaps_are_routed_to_neighbor_skills(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["as-common-project-instructions-builder", "as-common-project-riepilogo-operativo", "as-common-codex-step-manager"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_required_references_exist(self) -> None:
        expected = [
            "runbook-structure-checklist.md",
            "runbook-vs-project-instructions.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())


if __name__ == "__main__":
    unittest.main()
