from pathlib import Path

from pyguardian.analyzers.syntax import check_syntax
from pyguardian.models import CheckResult, Issue
from pyguardian.scanner import find_python_files


def check_project(path: Path) -> CheckResult:
    """Check a Python project and return the result."""

    python_files = find_python_files(path)
    issues: list[Issue] = []

    for python_file in python_files:
        issue = check_syntax(python_file)
        if issue is not None:
            issues.append(issue)

    return CheckResult(
        files_checked=len(python_files),
        issues=issues,
    )