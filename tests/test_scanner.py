from pathlib import Path

from pyguardian.scanner import (
    DEFAULT_EXCLUDED_DIRS, is_excluded, find_python_files
)


def test_is_excluded():
    """Detect paths inside ecluded directories."""

    excluded_path = Path(".venv") / "Lib" / "package.py"
    normal_path = Path("src") / "pyguardian" / "cli.py"

    assert is_excluded(excluded_path, DEFAULT_EXCLUDED_DIRS)
    assert not is_excluded(normal_path, DEFAULT_EXCLUDED_DIRS)


def test_find_python_files(tmp_path: Path) -> None:
    """Find Python files in a directory."""

    python_file = tmp_path / "example.py"
    python_file.write_text("print('Hello, World!')")
    result = find_python_files(tmp_path)

    assert python_file in result


def test_find_python_files_ignores_venv(tmp_path: Path) -> None:
    """."""

    venv_file = tmp_path / ".venv" / "Lib" / "site-packages" / "package.py"
    venv_file.parent.mkdir(parents=True)
    venv_file.write_text("print('This is .venv!')")
    result = find_python_files(tmp_path)

    assert venv_file not in result