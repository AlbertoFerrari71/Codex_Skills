from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class PythonFastapiDebugSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-python-fastapi-debug", text)

    def test_fastapi_debug_terms_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["fastapi", "pytest", "sqlalchemy", "uvicorn", "jinja", "status code", "error trace", "fixture"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_minimal_fix_and_boundaries_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["fix piccolo", "gate prima di commit", "trace reale da ipotesi", "quando non usarla", "opencv", "git publish flow"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_required_references_exist(self) -> None:
        expected = [
            "fastapi-debug-flow.md",
            "pytest-minimal-repro-checklist.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())


if __name__ == "__main__":
    unittest.main()
