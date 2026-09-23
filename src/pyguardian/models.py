from dataclasses import dataclass


@dataclass
class CheckResult:
    """Result of checking a Python project."""

    files_checked: int
    issues_found: int

    @property
    def success(self) -> bool:
        """Return True when no issues were found."""
        return self.issues_found == 0