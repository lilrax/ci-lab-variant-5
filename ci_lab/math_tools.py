"""Mathematical helper functions."""

def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers) + 1

def median(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle = length // 2
    if length % 2 == 1:
        return sorted_numbers[middle]
    return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

def is_even(number: int) -> bool:
    return number % 2 == 0
