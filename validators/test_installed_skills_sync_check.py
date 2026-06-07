#!/usr/bin/env python3
"""Unit tests for installed_skills_sync_check.py."""

from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_agent_skills
import installed_skills_sync_check as sync_check


VALID_SKILL = """---
name: {name}
description: Usa questa skill quando serve testare lo stato installato delle skill Codex.
---

# Scopo

Validare lo stato installato.

# Procedura

1. Leggere i file locali.
2. Produrre un report.
"""


def run_git(root: Path, *args: str) -> None:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stdout)


def init_git(root: Path) -> None:
    try:
        run_git(root, "init", "-q")
    except (FileNotFoundError, RuntimeError) as exc:
        raise unittest.SkipTest(f"git unavailable for sync-check tests: {exc}") from exc


def git_add_all(root: Path) -> None:
    run_git(root, "add", ".")


def write_skill(root: Path, folder: str = "as-common-valid-skill", declared: str | None = None) -> Path:
    skill_dir = root / folder
    skill_dir.mkdir(parents=True)
    skill_name = declared or folder
    (skill_dir / "SKILL.md").write_text(VALID_SKILL.format(name=skill_name), encoding="utf-8")
    return skill_dir


def write_catalogs(root: Path) -> None:
    reports = check_agent_skills.scan_skills(root)
    now = datetime(2026, 6, 7, 12, 0, 0)
    check_agent_skills.write_index(root, reports, now=now)
    check_agent_skills.write_score(root, reports, now=now)


def issue_codes(result: sync_check.SyncResult) -> set[str]:
    return {issue.code for issue in result.issues}


class InstalledSkillsSyncCheckTests(unittest.TestCase):
    def test_tracked_active_skill_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            write_catalogs(root)
            git_add_all(root)

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "PASS")
            self.assertEqual(len(result.skills), 1)
            self.assertTrue(result.skills[0].skill_md_tracked)

    def test_name_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root, "as-common-real-name", declared="as-common-other-name")
            write_catalogs(root)
            git_add_all(root)

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "FAIL")
            self.assertIn("name_mismatch", issue_codes(result))

    def test_untracked_skill_md_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            write_catalogs(root)
            run_git(root, "add", "SKILLS_INDEX.md", "SKILL_SCORE.md")

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "FAIL")
            self.assertIn("skill_md_untracked", issue_codes(result))

    def test_backup_inside_active_skill_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            skill_dir = write_skill(root)
            (skill_dir / "SKILL.md.bak.20260607").write_text("backup", encoding="utf-8")
            write_catalogs(root)
            git_add_all(root)

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "FAIL")
            self.assertIn("backup_temp_in_active_skill", issue_codes(result))

    def test_archive_backup_does_not_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            archive_dir = root / "_archive" / "backup-skills"
            archive_dir.mkdir(parents=True)
            (archive_dir / "SKILL.md.bak.20260607").write_text("backup", encoding="utf-8")
            write_catalogs(root)
            git_add_all(root)

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "PASS")
            self.assertNotIn("backup_temp_in_active_skill", issue_codes(result))
            self.assertIn("archive_backup_policy", issue_codes(result))

    def test_skill_missing_from_catalog_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            write_catalogs(root)
            (root / "SKILLS_INDEX.md").write_text("# SKILLS_INDEX\n\n", encoding="utf-8")
            git_add_all(root)

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "FAIL")
            self.assertIn("missing_from_index", issue_codes(result))

    def test_catalog_contains_missing_skill_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            write_catalogs(root)
            with (root / "SKILLS_INDEX.md").open("a", encoding="utf-8") as handle:
                handle.write("| as-common-missing-skill | as-common-missing-skill | stale | no | no | 0 | 0 |\n")
            git_add_all(root)

            result = sync_check.run_sync_check(root)

            self.assertEqual(result.status, "FAIL")
            self.assertIn("index_skill_missing_on_disk", issue_codes(result))

    def test_result_and_output_distinguish_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            write_catalogs(root)
            git_add_all(root)
            (root / "local-note.txt").write_text("local", encoding="utf-8")

            result = sync_check.run_sync_check(root)
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                sync_check.print_result(result)

            self.assertEqual(result.status, "PASS WITH NON-BLOCKING WARNINGS")
            self.assertIn("Warnings: 1", buffer.getvalue())
            self.assertIn("RESULT: PASS WITH NON-BLOCKING WARNINGS", buffer.getvalue())

    def test_script_works_from_root_argument(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_git(root)
            write_skill(root)
            write_catalogs(root)
            git_add_all(root)

            script = Path(__file__).resolve().parent / "installed_skills_sync_check.py"
            result = subprocess.run(
                [sys.executable, str(script), "--root", "."],
                cwd=root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("INSTALLED SKILLS SYNC CHECK", result.stdout)
            self.assertIn("RESULT: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
