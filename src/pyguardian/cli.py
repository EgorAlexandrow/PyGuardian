import typer

from pathlib import Path

from pyguardian import __version__
from pyguardian.application import check_project
from pyguardian.scanner import find_python_files


app = typer.Typer(
    name="pyguardian",
    help="A unified quality gate for Python Projects.",
)

@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(
        False,
        "--version",
        help="Show the PyGuardian version and exit.",
    ),
) -> None:
    """PyGuardian command-line interface."""

    if version:
        typer.echo(f"PyGuardian version: {__version__}")
        raise typer.Exit()


@app.command()
def check(path: Path) -> None:
    """Check a Python project."""

    if not path.exists():
        typer.echo(f"Path does not exist: {path}")
        raise typer.Exit(code=1)

    if not path.is_dir():
        typer.echo(f"Path is not a directpry: {path}")
        raise typer.Exit(code=1)

    result = check_project(path)
    typer.echo(f"Files checked: {result.files_checked}")
    typer.echo(f"Issues found: {result.issues_found}")

    for issue in result.issues:
        typer.echo(f'{issue.path}:{issue.line}:{issue.column} - {issue.message}')

    if not result.success:
        raise typer.Exit(code=1)