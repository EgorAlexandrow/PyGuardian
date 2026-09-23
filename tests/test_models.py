from pathlib import Path

from pyguardian.models import Issue, CheckResult


def test_issue() -> None:
    issue = Issue(
        path=Path("example.py"),
        line=1,
        column=5,
        message="Syntax error",
    )


def test_check_result_success() -> None:
    """A result with no issues is successful."""

    result = CheckResult(
        files_checked=2,
        issues=[],
    )

    assert result.success


def test_check_result_failure() -> None:
    """A result with no issues is not successful."""

    result = CheckResult(
        files_checked=2,
        issues=[
            Issue(
                path=Path("example.py"),
                line=1,
                column=5,
                message="Syntax error",
            )
        ],
    )

    assert not result.success