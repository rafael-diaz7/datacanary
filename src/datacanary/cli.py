"""Command line interface for DataCanary."""

from __future__ import annotations

import typer
from rich.console import Console

from datacanary import __version__

app = typer.Typer(
    help="Local-first freshness and drift monitoring for public datasets.",
    no_args_is_help=True,
)
console = Console()


@app.callback()
def main() -> None:
    """Local-first freshness and drift monitoring for public datasets."""


@app.command()
def version() -> None:
    """Print the DataCanary package version."""
    console.print(__version__)
