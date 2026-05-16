from typer.testing import CliRunner

from datacanary import __version__
from datacanary.cli import app

runner = CliRunner()


def test_version_prints_package_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert __version__ in result.output


def test_help_includes_project_description() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert (
        "Local-first freshness and drift monitoring for public datasets."
        in result.output
    )
