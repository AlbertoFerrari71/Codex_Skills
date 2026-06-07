#!/usr/bin/env python3
"""Unit tests for check_agent_skills.py."""

from __future__ import annotations

import tempfile
import unittest
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_agent_skills as validator


VALID_SKILL = """---
name: as-common-valid-skill
description: Usa questa skill quando serve validare una skill completa di esempio.
---

# Scopo

Validare una skill di test.

# Procedura

1. Leggere il contesto.
2. Eseguire i controlli.
"""


def write_skill(root: Path, name: str, content: str | None = VALID_SKILL) -> Path:
    skill_dir = root / name
    skill_dir.mkdir(parents=True)
    if content is not None:
        (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
    return skill_dir


def issue_codes(report: validator.SkillReport) -> set[str]:
    return {issue.code for issue in report.errors + report.warnings}


class CheckAgentSkillsTests(unittest.TestCase):
    def test_valid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "as-common-valid-skill")
            (skill_dir / "references").mkdir()
            (skill_dir / "examples").mkdir()

            reports = validator.scan_skills(root)

            self.assertEqual(len(reports), 1)
            self.assertEqual(reports[0].errors, [])
            self.assertTrue(reports[0].has_operational_body)

    def test_skill_without_skill_md(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "as-common-missing-skill", None)

            report = validator.scan_skills(root)[0]

            self.assertIn("missing_skill_md", issue_codes(report))

    def test_missing_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "as-common-no-frontmatter", "# Scopo\n\nTest senza frontmatter.\n")

            report = validator.scan_skills(root)[0]

            self.assertIn("missing_frontmatter", issue_codes(report))

    def test_name_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-real-name",
                """---
name: as-common-other-name
description: Description valida per una skill con nome errato.
---

# Procedura

Eseguire il controllo.
""",
            )

            report = validator.scan_skills(root)[0]

            self.assertIn("name_mismatch", issue_codes(report))

    def test_underscore_in_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-bad_name",
                """---
name: as-common-bad_name
description: Description valida per una skill con underscore.
---

# Procedura

Eseguire il controllo.
""",
            )

            report = validator.scan_skills(root)[0]

            self.assertIn("naming_underscore", issue_codes(report))

    def test_empty_description(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-empty-description",
                """---
name: as-common-empty-description
description: ""
---

# Procedura

Eseguire il controllo.
""",
            )

            report = validator.scan_skills(root)[0]

            self.assertIn("missing_description", issue_codes(report))

    def test_backup_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "as-common-valid-skill")
            (skill_dir / "SKILL.20260604.bak.md").write_text("backup", encoding="utf-8")

            report = validator.scan_skills(root)[0]

            self.assertIn("backup_file", issue_codes(report))
            self.assertEqual(report.backup_files, ["as-common-valid-skill/SKILL.20260604.bak.md"])

    def test_timestamped_backup_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "as-common-valid-skill")
            (skill_dir / "SKILL.md.bak.20260606T175318Z").write_text("backup", encoding="utf-8")

            report = validator.scan_skills(root)[0]

            self.assertIn("backup_file", issue_codes(report))
            self.assertEqual(
                report.backup_files,
                ["as-common-valid-skill/SKILL.md.bak.20260606T175318Z"],
            )

    def test_archive_directory_is_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "as-common-valid-skill")
            archive_skill = root / "_archive" / "as-common-archived-skill"
            archive_skill.mkdir(parents=True)
            (archive_skill / "SKILL.md").write_text("archived", encoding="utf-8")

            reports = validator.scan_skills(root)

            self.assertEqual([report.name for report in reports], ["as-common-valid-skill"])

    def test_index_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "as-common-valid-skill")
            (skill_dir / "references").mkdir()

            reports = validator.scan_skills(root)
            output = validator.write_index(root, reports, now=datetime(2026, 6, 5, 12, 0, 0))

            text = output.read_text(encoding="utf-8")
            self.assertIn("# SKILLS_INDEX", text)
            self.assertIn("| Skill totali | 1 |", text)
            self.assertIn("as-common-valid-skill", text)

    def test_score_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "as-common-valid-skill")
            (skill_dir / "references").mkdir()
            (skill_dir / "examples").mkdir()

            reports = validator.scan_skills(root)
            output = validator.write_score(root, reports, now=datetime(2026, 6, 5, 12, 0, 0))

            text = output.read_text(encoding="utf-8")
            self.assertIn("# SKILL_SCORE", text)
            self.assertIn("as-common-valid-skill", text)
            self.assertIn("| as-common-valid-skill | 100 | A |", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
