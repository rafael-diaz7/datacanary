"""DataCanary package."""

from datacanary.results import ValidationError, ValidationResult
from datacanary.validation import validate_csv, validate_csv_headers

__version__ = "0.0.1"

__all__ = [
    "ValidationError",
    "ValidationResult",
    "__version__",
    "validate_csv",
    "validate_csv_headers",
]
