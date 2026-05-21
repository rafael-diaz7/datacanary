"""CSV schema validation helpers."""

from __future__ import annotations

import csv
from collections.abc import Iterable
from datetime import date
from pathlib import Path
from typing import Any, Literal

from datacanary.results import ValidationError, ValidationResult

ColumnType = Literal["string", "number", "date", "boolean"]
Schema = dict[str, dict[str, Any]]


def validate_required_columns(
    columns: Iterable[str],
    schema: Schema,
) -> ValidationResult:
    """Validate that all required schema columns are present."""
    column_names = set(columns)
    errors = [
        ValidationError(
            row=None,
            column=column,
            message=f"Missing required column: {column}",
        )
        for column, rules in schema.items()
        if rules.get("required") is True and column not in column_names
    ]

    return ValidationResult(errors=errors)


def validate_csv_headers(path: str | Path, schema: Schema) -> ValidationResult:
    """Validate required columns using only the CSV header row."""
    with Path(path).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader, None)

    if not headers:
        return ValidationResult(
            errors=[
                ValidationError(
                    row=None,
                    column=None,
                    message="CSV file is empty or missing a header row",
                )
            ]
        )

    return validate_required_columns(headers, schema)


def validate_csv(path: str | Path, schema: Schema) -> ValidationResult:
    """Validate a CSV file against a simple column schema."""
    errors: list[ValidationError] = []

    with Path(path).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames or []

        column_result = validate_required_columns(fieldnames, schema)
        errors.extend(column_result.errors)

        if errors:
            return ValidationResult(errors=errors)

        for row_number, row in enumerate(reader, start=2):
            for column, rules in schema.items():
                value = row.get(column) or ""
                if rules.get("required") is True and value == "":
                    errors.append(
                        ValidationError(
                            row=row_number,
                            column=column,
                            message="Required value is empty.",
                        )
                    )
                    continue

                if value == "":
                    continue

                expected_type = rules.get("type")
                if not _is_valid_type(value, expected_type):
                    errors.append(
                        ValidationError(
                            row=row_number,
                            column=column,
                            message=f"Expected {expected_type} value.",
                        )
                    )

    return ValidationResult(errors=errors)


def _is_valid_type(value: str, expected_type: Any) -> bool:
    if expected_type == "string" or expected_type is None:
        return True
    if expected_type == "number":
        return _is_number(value)
    if expected_type == "date":
        return _is_date(value)
    if expected_type == "boolean":
        return value.lower() in {"true", "false"}
    return False


def _is_number(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True


def _is_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True
