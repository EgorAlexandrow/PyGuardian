from pathlib import Path

from pyguardian.analyzers.syntax import check_syntax


def test_check_syntax_valid_file(tmp_path: Path) -> None:
    """Valid Python code should pass syntax checking."""

    python_file = tmp_path / "valid.py"
    python_file.write_text(
        "def hello():\n"
        "   return 'Hello, World!'\n"
    )

    issue = check_syntax(python_file)

    assert issue is None


def test_check_syntax_invalid_file(tmp_path: Path) -> None:
    """Invalid Python code should fail syntax checking."""

    python_file = tmp_path / "invalid.py"
    python_file.write_text(
        "def hello()\n"
        "   return 'Hello, World!'\n"
    )

    issue = check_syntax(python_file)

    assert issue is not None
    assert issue.path == python_file
    assert issue.line == 1
    assert issue.column > 0
    assert issue.message