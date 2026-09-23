from pathlib import Path
from dataclasses import dataclass


@dataclass
class Issue:
    """A problem found during project analysis."""

    path: Path
    line: int
    column: int
    message: str


@dataclass
class CheckResult:
    """Result of checking a Python project."""

    files_checked: int
    issues: list[Issue]

    @property
    def issues_found(self) -> int:
        """Return the number of issues found."""

        return len(self.issues)


    @property
    def success(self) -> bool:
        """Return True when no issues were found."""

        return not self.issues