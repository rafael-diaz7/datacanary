# DataCanary

Local-first freshness and drift monitoring for public datasets.

**Status:** early development. DataCanary is not published yet and does not
perform dataset checks yet.

## North Star

Did the dataset I depend on stop updating or change in a way that could break
me?

## Planned Quickstart

Once published, DataCanary is intended to install cleanly with `pipx`:

```console
pipx install datacanary
datacanary --help
```

For now, install from a local checkout:

```console
python -m pip install -e ".[dev]"
datacanary --help
```

## Planned v0.1 Scope

- Define dataset sources in a small local config file.
- Run checks manually from the CLI.
- Store check history locally.
- Report freshness issues and basic drift signals such as schema and row count
  changes.
- Keep connectors and storage simple enough to evolve without locking in the
  wrong abstractions.

Future work may include remote CSV sources, JSON APIs, Socrata and ArcGIS
connectors, scheduling metadata, SQLite-backed history, and optional DuckDB
profiling.

## Development

```console
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
mypy src
pytest
```

## CLI

```console
datacanary --help
datacanary version
```

