from datacanary import ValidationError, ValidationResult


def test_empty_validation_result_passes() -> None:
    result = ValidationResult()

    assert result.passed is True
    assert result.errors == []


def test_validation_result_with_one_error_fails() -> None:
    result = ValidationResult(errors=[ValidationError(message="Invalid value.")])

    assert result.passed is False


def test_validation_error_stores_message_row_and_column() -> None:
    error = ValidationError(
        message="Invalid value.",
        row=2,
        column="amount",
    )

    assert error.message == "Invalid value."
    assert error.row == 2
    assert error.column == "amount"
