"""DataCanary package."""

from datacanary.validation import ValidationError, ValidationResult, validate_csv

__version__ = "0.0.1"

__all__ = ["ValidationError", "ValidationResult", "__version__", "validate_csv"]
