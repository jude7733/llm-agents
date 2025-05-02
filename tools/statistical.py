def find_average(a: int, b: int) -> float:
    """
    Find the average of two numbers

    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        float: The average of the two numbers
    """

    return (int(a) + int(b)) / 2.0


def find_variance(numbers: list) -> float:
    """
    Find the variance of a list of numbers

    Args:
        numbers (list): The list of numbers
    Returns:
        float: The variance of the numbers
    """

    n = len(numbers)
    mean = sum(numbers) / n
    return sum((x - mean) ** 2 for x in numbers) / n


def find_standard_deviation(numbers: list) -> float:
    """
    Find the standard deviation of a list of numbers

    Args:
        numbers (list): The list of numbers
    Returns:
        float: The standard deviation of the numbers
    """

    return find_variance(numbers) ** 0.5


def find_median(numbers: list) -> float:
    """
    Find the median of a list of numbers

    Args:
        numbers (list): The list of numbers
    Returns:
        float: The median of the numbers
    """

    n = len(numbers)
    sorted_numbers = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]


def find_mode(numbers: list) -> list:
    """
    Find the mode of a list of numbers

    Args:
        numbers (list): The list of numbers
    Returns:
        list: The mode of the numbers
    """

    from collections import Counter

    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, cnt in count.items() if cnt == max_count]


statistical_tools = [
    find_average,
    find_variance,
    find_standard_deviation,
    find_median,
    find_mode,
]
