from datacanary import ValidationError, validate_csv


def test_valid_csv_passes(tmp_path) -> None:
    csv_path = tmp_path / "valid.csv"
    csv_path.write_text(
        "name,amount,created_at,active\n"
        "Ada,12.5,2026-05-17,true\n"
        "Grace,0,2026-05-18,false\n",
        encoding="utf-8",
    )

    result = validate_csv(
        csv_path,
        {
            "name": {"required": True, "type": "string"},
            "amount": {"required": True, "type": "number"},
            "created_at": {"required": True, "type": "date"},
            "active": {"required": True, "type": "boolean"},
        },
    )

    assert result.passed is True
    assert result.errors == []


def test_missing_required_column_fails_before_row_validation(tmp_path) -> None:
    csv_path = tmp_path / "missing_column.csv"
    csv_path.write_text("name\n\n", encoding="utf-8")

    result = validate_csv(
        csv_path,
        {
            "name": {"required": True, "type": "string"},
            "amount": {"required": True, "type": "number"},
        },
    )

    assert result.passed is False
    assert result.errors == [
        ValidationError(
            row=0,
            column="amount",
            message="Missing required column.",
        )
    ]


def test_empty_required_value_fails(tmp_path) -> None:
    csv_path = tmp_path / "empty_required.csv"
    csv_path.write_text("name,amount\nAda,\n", encoding="utf-8")

    result = validate_csv(
        csv_path,
        {
            "name": {"required": True, "type": "string"},
            "amount": {"required": True, "type": "number"},
        },
    )

    assert result.passed is False
    assert result.errors == [
        ValidationError(
            row=2,
            column="amount",
            message="Required value is empty.",
        )
    ]


def test_missing_cell_in_short_row_fails_as_empty_required_value(tmp_path) -> None:
    csv_path = tmp_path / "short_row.csv"
    csv_path.write_text("name,amount\nAda\n", encoding="utf-8")

    result = validate_csv(
        csv_path,
        {
            "amount": {"required": True, "type": "number"},
        },
    )

    assert result.passed is False
    assert result.errors == [
        ValidationError(
            row=2,
            column="amount",
            message="Required value is empty.",
        )
    ]


def test_invalid_number_date_and_boolean_values_fail(tmp_path) -> None:
    csv_path = tmp_path / "invalid_types.csv"
    csv_path.write_text(
        "amount,created_at,active\n"
        "twelve,2026-05-17,true\n"
        "12,not-a-date,false\n"
        "12,2026-05-17,yes\n",
        encoding="utf-8",
    )

    result = validate_csv(
        csv_path,
        {
            "amount": {"type": "number"},
            "created_at": {"type": "date"},
            "active": {"type": "boolean"},
        },
    )

    assert result.passed is False
    assert result.errors == [
        ValidationError(
            row=2,
            column="amount",
            message="Expected number value.",
        ),
        ValidationError(
            row=3,
            column="created_at",
            message="Expected date value.",
        ),
        ValidationError(
            row=4,
            column="active",
            message="Expected boolean value.",
        ),
    ]
