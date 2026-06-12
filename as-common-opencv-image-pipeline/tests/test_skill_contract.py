from __future__ import annotations

import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"


class OpencvImagePipelineSkillContractTests(unittest.TestCase):
    def test_skill_md_exists_and_declares_expected_name(self) -> None:
        self.assertTrue(SKILL_MD.is_file())
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("name: as-common-opencv-image-pipeline", text)

    def test_image_pipeline_terms_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["qr code", "omografia", "binarizzazione", "istogrammi", "segmentazione", "debug immagini intermedie"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_cpp_style_and_anti_triggers_are_present(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8").lower()
        for term in ["namespace globali", "senza prefissi `cv::`", "quando non usarla", "fastapi", "analisi brevettuale"]:
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_required_references_exist(self) -> None:
        expected = [
            "image-pipeline-debug-checklist.md",
            "opencv-cpp-style-alberto.md",
        ]
        for filename in expected:
            with self.subTest(filename=filename):
                self.assertTrue((SKILL_DIR / "references" / filename).is_file())


if __name__ == "__main__":
    unittest.main()
