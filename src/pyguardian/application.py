from pathlib import Path

from pyguardian.models import CheckResult
from pyguardian.scanner import find_python_files


def check_project(path: Path) -> CheckResult:
    """Check a Python project and return the result."""

    python_files = find_python_files(path)
    return CheckResult(
        files_checked=len(python_files),
        issues_found=0
    )