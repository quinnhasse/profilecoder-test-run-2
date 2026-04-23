"""Core arithmetic helpers for mathlib."""

from __future__ import annotations


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b.

    Args:
        a: First operand. Accepts int or float.
        b: Second operand. Accepts int or float.

    Returns:
        a + b, preserving type rules of the underlying Python addition.
    """
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of a and b.

    Args:
        a: First operand. Accepts int or float.
        b: Second operand. Accepts int or float.

    Returns:
        a * b, preserving type rules of the underlying Python multiplication.
    """
    return a * b
