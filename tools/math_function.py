def find_gcd(a: int, b: int) -> int:
    """
    Find the GCD of two numbers
    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The GCD of the two numbers
    """

    if b == 0:
        return int(a)
    else:
        return find_gcd(int(b), int(a) % int(b))


def find_lcm(a: int, b: int) -> int:
    """
    Find the LCM of two numbers
    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The LCM of the two numbers
    """

    return int(a) * int(b) // find_gcd(int(a), int(b))


def pythagorean_theorem(a: float, b: float) -> float:
    """
    Find the hypotenuse of a right triangle
    Args:
        a (float): The length of one side
        b (float): The length of the other side
    Returns:
        float: The length of the hypotenuse
    """

    return (float(a) ** 2 + float(b) ** 2) ** 0.5


math_function_tools = [
    find_gcd,
    find_lcm,
    pythagorean_theorem,
]
