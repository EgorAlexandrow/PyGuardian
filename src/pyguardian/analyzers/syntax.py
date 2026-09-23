import ast
from pathlib import Path

from pyguardian.models import Issue


def check_syntax(path: Path) -> Issue | None:
    """Return True if a Python file has valid syntax."""

    source = path.read_text(encoding="utf-8")

    try:
        ast.parse(source)
    except SyntaxError as error:
        return Issue(
            path=path,
            line=error.lineno or 0,
            column=error.offset or 0,
            message=error.msg,
        )

    return None