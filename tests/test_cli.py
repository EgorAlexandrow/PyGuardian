from pathlib import Path

from typer.testing import CliRunner

from pyguardian.cli import app


runner = CliRunner()


def test_check_succes(tmp_path: Path) -> None:
    """Retrn exit code 0 for a project without issues."""

    python_file = tmp_path / "example.py"
    python_file.write_text("print('hello, World!')")

    result = runner.invoke(app, ["check", str(tmp_path)])

    assert result.exit_code == 0
    assert "Files checked: 1" in result.stdout
    assert "Issues found: 0" in result.stdout


def test_check_failure(tmp_path: Path) -> None:
    """Return exit code 1 for a project with isuues."""

    python_file = tmp_path / "bad_example.py"
    python_file.write_text(
        "def hello()\n"
        "   return 'Hello, World!'\n"
    )

    result = runner.invoke(app, ["check", str(tmp_path)])

    assert result.exit_code == 1
    assert "Files checked: 1" in result.stdout
    assert "Issues found: 1" in result.stdout
    assert "bad_example.py" in result.stdout