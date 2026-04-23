"""Tests for mathlib.arithmetic."""

import pytest

from mathlib import add, multiply

# ---------------------------------------------------------------------------
# add
# ---------------------------------------------------------------------------


def test_add_positive_ints() -> None:
    assert add(2, 3) == 5


def test_add_negative_int() -> None:
    assert add(-4, 10) == 6


def test_add_floats() -> None:
    assert add(1.5, 2.5) == pytest.approx(4.0)


def test_add_mixed_int_float() -> None:
    assert add(3, 0.5) == pytest.approx(3.5)


def test_add_zeros() -> None:
    assert add(0, 0) == 0


# ---------------------------------------------------------------------------
# multiply
# ---------------------------------------------------------------------------


def test_multiply_positive_ints() -> None:
    assert multiply(3, 4) == 12


def test_multiply_by_zero() -> None:
    assert multiply(99, 0) == 0


def test_multiply_floats() -> None:
    assert multiply(2.5, 4.0) == pytest.approx(10.0)


def test_multiply_negative_values() -> None:
    assert multiply(-3, 5) == -15


def test_multiply_mixed_int_float() -> None:
    assert multiply(2, 1.5) == pytest.approx(3.0)
