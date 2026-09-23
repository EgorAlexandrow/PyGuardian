from pathlib import Path

from pyguardian.application import check_project


def test_check_project_counts_python_files(tmp_path: Path) -> None:
    """Count Python files in a project."""

    first_file = tmp_path / "first.py"
    second_file = tmp_path / "second.py"

    first_file.write_text("print('First file!')")
    second_file.write_text("print('Second file!')")

    result = check_project(tmp_path)

    assert result.files_checked == 2
    assert result.issues_found == 0
    assert result.success