"""Validation result models."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValidationError:
    """A single validation failure."""

    message: str
    row: int | None = None
    column: str | None = None


@dataclass(frozen=True)
class ValidationResult:
    """Structured result returned by validation."""

    errors: list[ValidationError] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0
