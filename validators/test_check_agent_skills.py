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


def valid_skill_content(name: str) -> str:
    return VALID_SKILL.replace("as-common-valid-skill", name)


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

    def test_secret_generic_term_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-secret-word",
                """---
name: as-common-secret-word
description: Usa questa skill quando serve verificare parole generiche di sicurezza.
---

# Scopo

Documentare una policy: do not expose secrets in logs.

# Procedura

Eseguire il controllo.
""",
            )

            report = validator.scan_skills(root)[0]

            self.assertNotIn("sensitive_value", issue_codes(report))

    def test_likely_api_key_is_blocking_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(
                "OPENAI_API_KEY=sk-abcdefghijklmnopqrstuvwxyz123456\n",
                encoding="utf-8",
            )

            issues = validator.scan_repository_files(root)

            self.assertIn("sensitive_value", {issue.code for issue in issues})
            self.assertIn("ERROR", {issue.level for issue in issues})

    def test_uid_pwd_placeholders_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(
                "Connection string: UID=<UID_PLACEHOLDER>;PWD=<PWD_PLACEHOLDER>\n",
                encoding="utf-8",
            )

            issues = validator.scan_repository_files(root)

            self.assertEqual(issues, [])

    def test_catalog_freshness_detects_stale_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "as-common-valid-skill")
            reports = validator.scan_skills(root)
            validator.write_index(root, reports, now=datetime(2026, 6, 5, 12, 0, 0))
            validator.write_score(root, reports, now=datetime(2026, 6, 5, 12, 0, 0))
            self.assertEqual(validator.check_catalog_freshness(root, reports), [])

            (root / "SKILL_SCORE.md").write_text("# stale\n", encoding="utf-8")

            issues = validator.check_catalog_freshness(root, reports)

            self.assertIn("catalog_stale", {issue.code for issue in issues})

    def test_missing_reference_link_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-broken-reference",
                """---
name: as-common-broken-reference
description: Usa questa skill quando serve verificare link references mancanti.
---

# Scopo

Validare link dichiarati.

## References

- [Missing](references/missing.md)

# Procedura

Eseguire il controllo.
""",
            )

            report = validator.scan_skills(root)[0]

            self.assertIn("missing_declared_link", issue_codes(report))

    def test_existing_reference_link_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(
                root,
                "as-common-good-reference",
                """---
name: as-common-good-reference
description: Usa questa skill quando serve verificare link references validi.
---

# Scopo

Validare link dichiarati.

## References

- [Standard](references/standard.md)

# Procedura

Eseguire il controllo.
""",
            )
            (skill_dir / "references").mkdir()
            (skill_dir / "references" / "standard.md").write_text("# Standard\n", encoding="utf-8")

            report = validator.scan_skills(root)[0]

            self.assertNotIn("missing_declared_link", issue_codes(report))

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
            (skill_dir / "references" / "standard.md").write_text("# Standard\n", encoding="utf-8")
            (skill_dir / "examples").mkdir()
            (skill_dir / "examples" / "demo.md").write_text("# Demo\n", encoding="utf-8")

            reports = validator.scan_skills(root)
            output = validator.write_score(root, reports, now=datetime(2026, 6, 5, 12, 0, 0))

            text = output.read_text(encoding="utf-8")
            self.assertIn("# SKILL_SCORE", text)
            self.assertIn("as-common-valid-skill", text)
            self.assertIn("| Skill | StructureScore | OperationalQualityScore | Grade | Errors | Warnings | Recommendation |", text)
            self.assertIn("| as-common-valid-skill |", text)

    def test_empty_reference_example_dirs_do_not_add_cosmetic_points(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "as-common-plain-skill", valid_skill_content("as-common-plain-skill"))
            empty_skill = write_skill(
                root,
                "as-common-empty-dirs-skill",
                valid_skill_content("as-common-empty-dirs-skill"),
            )
            (empty_skill / "references").mkdir()
            (empty_skill / "examples").mkdir()

            reports = {report.name: report for report in validator.scan_skills(root)}

            self.assertFalse(reports["as-common-empty-dirs-skill"].has_real_references)
            self.assertFalse(reports["as-common-empty-dirs-skill"].has_real_examples)
            self.assertLessEqual(
                reports["as-common-empty-dirs-skill"].structure_score,
                reports["as-common-plain-skill"].structure_score,
            )

    def test_real_reference_example_files_add_structure_credit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            empty_skill = write_skill(
                root,
                "as-common-empty-dirs-skill",
                valid_skill_content("as-common-empty-dirs-skill"),
            )
            (empty_skill / "references").mkdir()
            (empty_skill / "examples").mkdir()
            real_skill = write_skill(
                root,
                "as-common-real-dirs-skill",
                valid_skill_content("as-common-real-dirs-skill"),
            )
            (real_skill / "references").mkdir()
            (real_skill / "references" / "standard.md").write_text("# Standard\n", encoding="utf-8")
            (real_skill / "examples").mkdir()
            (real_skill / "examples" / "demo.md").write_text("# Demo\n", encoding="utf-8")

            reports = {report.name: report for report in validator.scan_skills(root)}

            self.assertTrue(reports["as-common-real-dirs-skill"].has_real_references)
            self.assertTrue(reports["as-common-real-dirs-skill"].has_real_examples)
            self.assertGreater(
                reports["as-common-real-dirs-skill"].structure_score,
                reports["as-common-empty-dirs-skill"].structure_score,
            )

    def test_operational_quality_rewards_anti_trigger(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-without-anti-trigger",
                """---
name: as-common-without-anti-trigger
description: Usa questa skill quando serve preparare verifiche operative per Alberto in Codex.
---

# Scopo

Preparare verifiche operative.

# Output

Restituire un report sintetico.
""",
            )
            write_skill(
                root,
                "as-common-with-anti-trigger",
                """---
name: as-common-with-anti-trigger
description: Usa questa skill quando serve preparare verifiche operative per Alberto in Codex.
---

# Scopo

Preparare verifiche operative.

# Quando non usarla

Non usarla per generare codice o modificare repository.

# Output

Restituire un report sintetico.
""",
            )

            reports = {report.name: report for report in validator.scan_skills(root)}

            self.assertGreater(
                reports["as-common-with-anti-trigger"].operational_quality_score,
                reports["as-common-without-anti-trigger"].operational_quality_score,
            )

    def test_operational_quality_penalizes_generic_description(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "as-common-generic-description",
                """---
name: as-common-generic-description
description: Validare skill.
---

# Scopo

Validare.
""",
            )
            write_skill(
                root,
                "as-common-specific-description",
                """---
name: as-common-specific-description
description: Usa questa skill quando Alberto deve preparare un gate locale Codex con report e verifiche Git.
---

# Scopo

Preparare gate riproducibili per repository Codex.

# Quando non usarla

Non usarla per implementare feature applicative.

# Output

Restituire report, evidenze e prossimo step.
""",
            )

            reports = {report.name: report for report in validator.scan_skills(root)}

            self.assertLess(
                reports["as-common-generic-description"].operational_quality_score,
                reports["as-common-specific-description"].operational_quality_score,
            )

    def test_catalog_write_preserves_timestamp_when_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "as-common-valid-skill")
            reports = validator.scan_skills(root)

            output = validator.write_index(root, reports, now=datetime(2026, 6, 5, 12, 0, 0))
            first_text = output.read_text(encoding="utf-8")
            validator.write_index(root, reports, now=None)

            self.assertEqual(output.read_text(encoding="utf-8"), first_text)

    def test_step_0905_hardening_rules_are_present(self) -> None:
        root = Path(__file__).resolve().parent.parent

        pwsh_skill = (root / "as-common-pwsh-command-pack" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        safe_flow = (
            root / "as-common-powershell-git-safe-flow" / "SKILL.md"
        ).read_text(encoding="utf-8")
        pwsh_standard = (
            root
            / "as-common-pwsh-command-pack"
            / "references"
            / "pwsh-command-pack-standard.md"
        ).read_text(encoding="utf-8")
        known_bugs = (
            root
            / "as-common-pwsh-command-pack"
            / "references"
            / "pwsh-known-bugs-regression-tests.md"
        ).read_text(encoding="utf-8")

        bridge_text = (pwsh_skill + "\n" + pwsh_standard).lower()
        bridge_order = bridge_text[bridge_text.index("operational order:") :]
        self.assertLess(bridge_order.index("progressive"), bridge_order.index("last-*"))
        self.assertIn("server_modified", bridge_text)
        self.assertIn("## cached diff check", bridge_text)

        diagnostics_text = safe_flow + "\n" + pwsh_standard
        for token in (
            "git status --short",
            "git status -sb",
            "git diff --cached --name-status",
            "git diff --cached --check",
            "$LASTEXITCODE",
        ):
            self.assertIn(token, diagnostics_text)

        markdown_text = (pwsh_skill + "\n" + safe_flow + "\n" + pwsh_standard).lower()
        self.assertIn("here-string", markdown_text)
        self.assertIn("$lines = @()", markdown_text)
        self.assertIn("triple backticks", markdown_text)

        recovery_text = (pwsh_skill + "\n" + pwsh_standard + "\n" + known_bugs).lower()
        for token in (
            "git diff --cached --check",
            "new blank line at eof",
            "back up",
            "restage",
            "only those files",
        ):
            self.assertIn(token, recovery_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
