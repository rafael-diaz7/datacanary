# Contributing

Thanks for your interest in DataCanary. The project is early, so small,
focused contributions are especially helpful.

## Development Setup

```console
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Before Opening a Pull Request

Run the local checks:

```console
ruff check .
ruff format --check .
mypy src
pytest
```

## Contribution Guidelines

- Keep changes narrow and reviewable.
- Match the existing style and project structure.
- Add tests for behavior changes when practical.
- Avoid new runtime dependencies unless the benefit is clear.
- Separate unrelated cleanup from feature or bug fix changes.

