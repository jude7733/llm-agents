def find_factorial(a: int) -> int:
    """
    Find the factorial of a number
    Args:
        a (int): The number
    Returns:
        int: The factorial of the number
    """

    if a == 0:
        return 1
    else:
        return int(a) * find_factorial(int(a) - 1)


def find_permutation(n: int, r: int) -> int:
    """
    Find the permutation of n and r
    Args:
        n (int): The total number of items
        r (int): The number of items to choose
    Returns
        int: The permutation of n and r
    """

    return find_factorial(int(n)) // find_factorial(int(n) - int(r))


def find_combination(n: int, r: int) -> int:
    """
    Find the combination of n and r
    Args:
        n (int): The total number of items
        r (int): The number of items to choose
    Returns:
        int: The combination of n and r
    """

    return find_permutation(int(n), int(r)) // find_factorial(int(r))


combinator_tools = [
    find_factorial,
    find_permutation,
    find_combination,
]
