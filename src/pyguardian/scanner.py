from pathlib import Path


DEFAULT_EXCLUDED_DIRS = {
    ".venv",
    ".git",
    "__pycache__",
    ".pytest_cache",
}

def is_excluded(path: Path, excluded_dirs: set[str]) -> bool:
    """Return True if the path belongs to an ecluded directory."""

    return any(part in excluded_dirs for part in path.parts)


def find_python_files(path: Path) -> list[Path]:
    """."""

    python_files = [file for file in path.rglob("*.py") if not is_excluded(file, DEFAULT_EXCLUDED_DIRS)]
    return python_files