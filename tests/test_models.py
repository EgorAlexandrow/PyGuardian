from pyguardian.models import CheckResult


def test_check_result_success() -> None:
    """A result with no issues is successful."""

    result = CheckResult(
        files_checked=2,
        issues_found=0,
    )

    assert result.success


def test_check_result_failure() -> None:
    """A result with no issues is not successful."""

    result = CheckResult(
        files_checked=2,
        issues_found=1,
    )

    assert not result.success