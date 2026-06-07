#!/usr/bin/env python3
"""Check installed Codex skills against Git tracking and generated catalogs."""

from __future__ import annotations

import argparse
import fnmatch
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import check_agent_skills


ACTIVE_SKILL_PREFIX = "as-common-"
BACKUP_TEMP_PATTERNS = (
    "*.bak",
    "*.bak.*",
    "*.backup",
    "*.backup.*",
    "*.tmp",
    "*.temp",
    "*.orig",
    "*.rej",
    "*~",
)
RISKY_SCRIPT_SUFFIXES = {".ps1", ".bat", ".cmd"}
RISKY_NAME_TERMS = ("secret", "token", "credential", "password")
IGNORED_CACHE_PARTS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


@dataclass
class SyncIssue:
    level: str
    code: str
    message: str
    path: str = ""


@dataclass
class SkillSyncRecord:
    name: str
    rel_dir: str
    declared_name: str = ""
    in_index: bool = False
    in_score: bool = False
    skill_md_tracked: bool = False
    skill_has_tracked_files: bool = False
    untracked_files: list[str] = field(default_factory=list)
    ignored_files: list[str] = field(default_factory=list)


@dataclass
class SyncResult:
    root: Path
    inside_agents_skills: bool
    git_branch: str = "unavailable"
    git_head: str = "unavailable"
    skills: list[SkillSyncRecord] = field(default_factory=list)
    index_skills: set[str] = field(default_factory=set)
    score_skills: set[str] = field(default_factory=set)
    issues: list[SyncIssue] = field(default_factory=list)

    @property
    def blocking_issues(self) -> list[SyncIssue]:
        return [issue for issue in self.issues if issue.level == "BLOCKING"]

    @property
    def warnings(self) -> list[SyncIssue]:
        return [issue for issue in self.issues if issue.level == "WARNING"]

    @property
    def info(self) -> list[SyncIssue]:
        return [issue for issue in self.issues if issue.level == "INFO"]

    @property
    def status(self) -> str:
        if self.blocking_issues:
            return "FAIL"
        if self.warnings:
            return "PASS WITH NON-BLOCKING WARNINGS"
        return "PASS"


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


def relative_display(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def run_git(root: Path, args: list[str]) -> tuple[int, str]:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    except FileNotFoundError:
        return 127, "git command not found"
    return result.returncode, result.stdout.strip()


def git_lines(root: Path, args: list[str]) -> list[str]:
    exit_code, output = run_git(root, args)
    if exit_code != 0 or not output:
        return []
    return [line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()]


def is_git_repository(root: Path) -> bool:
    exit_code, _ = run_git(root, ["rev-parse", "--is-inside-work-tree"])
    return exit_code == 0


def git_branch(root: Path) -> str:
    exit_code, output = run_git(root, ["--no-pager", "branch", "--show-current"])
    if exit_code != 0 or not output:
        return "unavailable"
    return output.splitlines()[0].strip()


def git_head(root: Path) -> str:
    exit_code, output = run_git(root, ["rev-parse", "--short", "HEAD"])
    if exit_code != 0 or not output:
        return "unavailable"
    return output.splitlines()[0].strip()


def is_inside_agents_skills(root: Path) -> bool:
    parts = [part.lower() for part in root.parts]
    for index, part in enumerate(parts[:-1]):
        if part == ".agents" and parts[index + 1] == "skills":
            return True
    return False


def find_active_skill_dirs(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and path.name.startswith(ACTIVE_SKILL_PREFIX) and (path / "SKILL.md").is_file()
    )


def find_skill_like_dirs_without_skill_md(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and path.name.startswith(ACTIVE_SKILL_PREFIX) and not (path / "SKILL.md").is_file()
    )


def is_empty_dir(path: Path) -> bool:
    return path.is_dir() and not any(path.iterdir())


def matches_any_pattern(name: str, patterns: Iterable[str]) -> bool:
    lowered = name.lower()
    return any(fnmatch.fnmatch(lowered, pattern.lower()) for pattern in patterns)


def is_backup_or_temp(path: Path) -> bool:
    return matches_any_pattern(path.name, BACKUP_TEMP_PATTERNS)


def is_ignored_cache_or_temp(path_text: str) -> bool:
    parts = set(Path(path_text).parts)
    name = Path(path_text).name
    return bool(parts & IGNORED_CACHE_PARTS) or is_backup_or_temp(Path(name)) or name.endswith(".pyc")


def is_env_file(path: Path) -> bool:
    name = path.name.lower()
    return name == ".env" or name.startswith(".env.")


def risky_filename_terms(path: Path) -> list[str]:
    lowered = path.name.lower()
    return [term for term in RISKY_NAME_TERMS if term in lowered]


def parse_catalog_skill_names(path: Path) -> set[str]:
    text = check_agent_skills.read_text_file(path)
    if text is None:
        return set()
    names: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^\|\s*(as-common-[a-z0-9-]+)\s*\|", line)
        if match:
            names.add(match.group(1))
    return names


def declared_skill_name(skill_md: Path) -> str:
    text = check_agent_skills.read_text_file(skill_md)
    if text is None:
        return ""
    frontmatter_valid, frontmatter, _ = check_agent_skills.parse_frontmatter(text)
    if not frontmatter_valid:
        return ""
    return frontmatter.get("name", "").strip()


def issue(level: str, code: str, message: str, path: str = "") -> SyncIssue:
    return SyncIssue(level=level, code=code, message=message, path=path)


def scan_active_skill(root: Path, skill_dir: Path, index_skills: set[str], score_skills: set[str]) -> tuple[SkillSyncRecord, list[SyncIssue]]:
    rel_dir = relative_display(root, skill_dir)
    skill_name = skill_dir.name
    skill_md_rel = f"{rel_dir}/SKILL.md"
    declared_name = declared_skill_name(skill_dir / "SKILL.md")
    tracked_files = git_lines(root, ["ls-files", "--", rel_dir])
    untracked_files = git_lines(root, ["ls-files", "--others", "--exclude-standard", "--", rel_dir])
    ignored_files = git_lines(root, ["ls-files", "--others", "--ignored", "--exclude-standard", "--", rel_dir])
    tracked_set = set(tracked_files)

    record = SkillSyncRecord(
        name=skill_name,
        rel_dir=rel_dir,
        declared_name=declared_name,
        in_index=skill_name in index_skills,
        in_score=skill_name in score_skills,
        skill_md_tracked=skill_md_rel in tracked_set,
        skill_has_tracked_files=bool(tracked_files),
        untracked_files=untracked_files,
        ignored_files=ignored_files,
    )

    issues: list[SyncIssue] = []
    if not record.skill_has_tracked_files:
        issues.append(issue("BLOCKING", "skill_untracked", "Active skill directory has no tracked files.", rel_dir))
    if not record.skill_md_tracked:
        issues.append(issue("BLOCKING", "skill_md_untracked", "SKILL.md is not tracked by Git.", skill_md_rel))
    if not declared_name:
        issues.append(issue("BLOCKING", "missing_frontmatter_name", "SKILL.md frontmatter name is missing or unreadable.", skill_md_rel))
    elif declared_name != skill_name:
        issues.append(
            issue(
                "BLOCKING",
                "name_mismatch",
                f"Frontmatter name '{declared_name}' differs from folder '{skill_name}'.",
                skill_md_rel,
            )
        )
    if not record.in_index:
        issues.append(issue("BLOCKING", "missing_from_index", "Active skill missing from SKILLS_INDEX.md.", skill_name))
    if not record.in_score:
        issues.append(issue("BLOCKING", "missing_from_score", "Active skill missing from SKILL_SCORE.md.", skill_name))

    for file_path in skill_dir.rglob("*"):
        if file_path.is_dir():
            continue
        rel_file = relative_display(root, file_path)
        if is_backup_or_temp(file_path):
            issues.append(issue("BLOCKING", "backup_temp_in_active_skill", "Backup/temp file inside active skill.", rel_file))

    for rel_file in untracked_files:
        suffix = Path(rel_file).suffix.lower()
        if suffix in RISKY_SCRIPT_SUFFIXES:
            issues.append(issue("BLOCKING", "untracked_script_in_active_skill", "Untracked script file inside active skill.", rel_file))
        elif not is_backup_or_temp(Path(rel_file)):
            issues.append(issue("WARNING", "untracked_file_in_active_skill", "Untracked file inside active skill.", rel_file))

    for rel_file in ignored_files:
        if is_ignored_cache_or_temp(rel_file):
            issues.append(issue("WARNING", "ignored_cache_in_active_skill", "Ignored cache/temp file inside active skill.", rel_file))
        else:
            issues.append(issue("WARNING", "ignored_file_in_active_skill", "Ignored file inside active skill.", rel_file))

    return record, issues


def path_is_under_active_skill(rel_path: str, active_skill_names: set[str]) -> bool:
    first_part = rel_path.replace("\\", "/").split("/", 1)[0]
    return first_part in active_skill_names


def path_is_under_archive(rel_path: str) -> bool:
    return rel_path.replace("\\", "/").startswith("_archive/")


def scan_global_risk_files(root: Path) -> list[SyncIssue]:
    issues: list[SyncIssue] = []
    for file_path in root.rglob("*"):
        if file_path.is_dir() or ".git" in file_path.parts:
            continue
        rel_file = relative_display(root, file_path)
        if is_env_file(file_path):
            issues.append(issue("BLOCKING", "env_file", ".env file found in repository.", rel_file))
            continue
        terms = risky_filename_terms(file_path)
        if terms:
            issues.append(
                issue(
                    "WARNING",
                    "risky_filename",
                    f"Filename contains sensitive term(s): {', '.join(terms)}.",
                    rel_file,
                )
            )
    return issues


def scan_untracked_outside_active(root: Path, active_skill_names: set[str]) -> list[SyncIssue]:
    issues: list[SyncIssue] = []
    for rel_file in git_lines(root, ["ls-files", "--others", "--exclude-standard"]):
        if path_is_under_active_skill(rel_file, active_skill_names):
            continue
        if path_is_under_archive(rel_file):
            issues.append(issue("INFO", "archive_untracked_file", "Untracked file under _archive is informational.", rel_file))
            continue
        suffix = Path(rel_file).suffix.lower()
        if suffix in RISKY_SCRIPT_SUFFIXES or is_env_file(Path(rel_file)):
            issues.append(issue("WARNING", "untracked_risky_file_outside_skill", "Untracked risky local file outside active skills.", rel_file))
        elif risky_filename_terms(Path(rel_file)):
            issues.append(issue("WARNING", "untracked_sensitive_name_outside_skill", "Untracked local file with sensitive filename outside active skills.", rel_file))
        else:
            issues.append(issue("WARNING", "untracked_file_outside_skill", "Untracked local file outside active skills.", rel_file))
    return issues


def scan_catalog_freshness(root: Path) -> list[SyncIssue]:
    reports = check_agent_skills.scan_skills(root)
    issues = check_agent_skills.check_catalog_freshness(root, reports)
    return [
        issue(
            "BLOCKING",
            catalog_issue.code,
            catalog_issue.message,
            catalog_issue.path,
        )
        for catalog_issue in issues
    ]


def run_sync_check(root: Path) -> SyncResult:
    result = SyncResult(root=root, inside_agents_skills=is_inside_agents_skills(root))
    result.git_branch = git_branch(root)
    result.git_head = git_head(root)

    if result.inside_agents_skills:
        result.issues.append(issue("INFO", "inside_agents_skills", "Root is inside .agents/skills.", str(root)))
    else:
        result.issues.append(issue("INFO", "outside_agents_skills", "Root is not inside .agents/skills; acceptable for CI or copied repositories.", str(root)))

    archive_backup = root / "_archive" / "backup-skills"
    if archive_backup.is_dir():
        backup_count = sum(1 for path in archive_backup.rglob("*") if path.is_file())
        result.issues.append(issue("INFO", "archive_backup_policy", f"_archive/backup-skills ignored as inactive backup area ({backup_count} files).", "_archive/backup-skills"))

    if not is_git_repository(root):
        result.issues.append(issue("BLOCKING", "git_unavailable", "Root is not a Git worktree or Git is unavailable.", str(root)))
        return result

    result.index_skills = parse_catalog_skill_names(root / "SKILLS_INDEX.md")
    result.score_skills = parse_catalog_skill_names(root / "SKILL_SCORE.md")

    active_skill_dirs = find_active_skill_dirs(root)
    active_skill_names = {path.name for path in active_skill_dirs}

    for skill_like_dir in find_skill_like_dirs_without_skill_md(root):
        rel_dir = relative_display(root, skill_like_dir)
        if is_empty_dir(skill_like_dir):
            result.issues.append(issue("WARNING", "empty_skill_like_dir", "Empty as-common-* directory without SKILL.md.", rel_dir))
        else:
            result.issues.append(issue("WARNING", "inactive_skill_like_dir", "as-common-* directory without SKILL.md is not treated as active.", rel_dir))

    for skill_dir in active_skill_dirs:
        record, issues = scan_active_skill(root, skill_dir, result.index_skills, result.score_skills)
        result.skills.append(record)
        result.issues.extend(issues)

    missing_index_dirs = result.index_skills - active_skill_names
    missing_score_dirs = result.score_skills - active_skill_names
    for skill_name in sorted(missing_index_dirs):
        result.issues.append(issue("BLOCKING", "index_skill_missing_on_disk", "SKILLS_INDEX.md contains skill not present on disk.", skill_name))
    for skill_name in sorted(missing_score_dirs):
        result.issues.append(issue("BLOCKING", "score_skill_missing_on_disk", "SKILL_SCORE.md contains skill not present on disk.", skill_name))

    result.issues.extend(scan_catalog_freshness(root))
    result.issues.extend(scan_global_risk_files(root))
    result.issues.extend(scan_untracked_outside_active(root, active_skill_names))

    return result


def print_issue_list(title: str, issues: list[SyncIssue]) -> None:
    print()
    print(title)
    if not issues:
        print("- None.")
        return
    for item in issues:
        path_part = f" [{item.path}]" if item.path else ""
        print(f"- {item.code}: {item.message}{path_part}")


def print_result(result: SyncResult) -> None:
    print("INSTALLED SKILLS SYNC CHECK")
    print()
    print(f"Root: {result.root}")
    print(f"Inside .agents\\skills: {yes_no(result.inside_agents_skills)}")
    print(f"Git branch: {result.git_branch}")
    print(f"Git HEAD: {result.git_head}")
    print()
    print(f"Skills found: {len(result.skills)}")
    print(f"Skills in SKILLS_INDEX.md: {len(result.index_skills)}")
    print(f"Skills in SKILL_SCORE.md: {len(result.score_skills)}")
    print()
    print(f"Blocking issues: {len(result.blocking_issues)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Info: {len(result.info)}")

    print_issue_list("Blocking issues", result.blocking_issues)
    print_issue_list("Warnings", result.warnings)
    print_issue_list("Info", result.info)

    print()
    print(f"RESULT: {result.status}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check installed skill sync state.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"Root not valid: {root}")
        return 2

    result = run_sync_check(root)
    print_result(result)
    return 1 if result.blocking_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
