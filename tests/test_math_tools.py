import pytest

from ci_lab.math_tools import average, is_even, median


def test_average_returns_arithmetic_mean() -> None:
    assert average([2, 4, 6, 8]) == 5

def test_average_raises_error_for_empty_list() -> None:
    with pytest.raises(ValueError, match="numbers must not be empty"):
        average([])

def test_median_for_odd_count() -> None:
    assert median([5, 1, 9]) == 5

def test_median_for_even_count() -> None:
    assert median([10, 2, 8, 4]) == 6

def test_is_even() -> None:
    assert is_even(10) is True
    assert is_even(7) is False
