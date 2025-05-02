def add_two_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
      a (int): The first number
      b (int): The second number

    Returns:
      int: The sum of the two numbers
    """

    return int(a) + int(b)


def subtract_two_numbers(a: int, b: int) -> int:
    """
    Subtract two numbers

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The difference of the two numbers
    """

    return int(a) - int(b)


def divide_two_numbers(a: int, b: int) -> float:
    """
    Divide two numbers

    Args:
        a (int): The first number
        b (int): The second number

    returns:
        float: The quotient of the two numbers
    """

    return float(a) / float(b)


def multiply_two_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers

    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The product of the two numbers
    """

    return int(a) * int(b)


def find_square(a: int) -> int:
    """
    Find the square of a number

    Args:
        a (int): The number
    Returns:
        int: The square of the number
    """

    return int(a) * int(a)


def find_square_root(a: int) -> float:
    """
    Find the square root of a number
    Args:
        a (int): The number
    Returns:
        float: The square root of the number
    """

    return float(a) ** 0.5


def find_power(a: int, b: int) -> float:
    """
    Find the power of a number
    Args:
        a (int): The base number
        b (int): The exponent
    Returns:
        float: The result of a raised to the power of b
    """

    return float(a) ** float(b)


def find_modulus(a: int, b: int) -> int:
    """
    Find the modulus of two numbers
    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The modulus of the two numbers
    """

    return int(a) % int(b)


def find_logarithm(base: float, x: float) -> float:
    """
    Find the logarithm of a number
    Args:
        base (float): The base of the logarithm
        x (float): The number
    Returns:
        float: The logarithm of the number
    """

    return float(x) / float(base)


def find_exponential(base: float, exponent: float) -> float:
    """
    Find the exponential of a number
    Args:
        base (float): The base of the exponential
        exponent (float): The exponent
    Returns:
        float: The exponential of the number
    """

    return float(base) ** float(exponent)


arithmetic_tools = [
    add_two_numbers,
    subtract_two_numbers,
    divide_two_numbers,
    multiply_two_numbers,
    find_square,
    find_square_root,
    find_power,
    find_modulus,
    find_exponential,
    find_logarithm,
]
