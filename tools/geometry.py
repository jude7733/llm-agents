def find_area_of_circle(radius: float) -> float:
    """
    Find the area of a circle
    Args:
        radius (float): The radius of the circle
    Returns:
        float: The area of the circle
    """

    return 3.14 * float(radius) * float(radius)


def find_area_of_rectangle(length: float, width: float) -> float:
    """
    Find the area of a rectangle
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    Returns:
        float: The area of the rectangle
    """

    return float(length) * float(width)


def find_area_of_triangle(base: float, height: float) -> float:
    """
    Find the area of a triangle
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle
    Returns:
        float: The area of the triangle
    """

    return 0.5 * float(base) * float(height)


def find_area_of_square(side: float) -> float:
    """
    Find the area of a square
    Args:
        side (float): The side length of the square
    Returns:
        float: The area of the square
    """

    return float(side) * float(side)


def find_volume_of_cube(side: float) -> float:
    """
    Find the volume of a cube
    Args:
        side (float): The side length of the cube
    Returns:
        float: The volume of the cube
    """

    return float(side) * float(side) * float(side)


def find_volume_of_sphere(radius: float) -> float:
    """
    Find the volume of a sphere
    Args:
        radius (float): The radius of the sphere
    Returns:
        float: The volume of the sphere
    """

    return (4 / 3) * 3.14 * float(radius) * float(radius) * float(radius)


def find_volume_of_cylinder(radius: float, height: float) -> float:
    """
    Find the volume of a cylinder
    Args:
        radius (float): The radius of the cylinder
        height (float): The height of the cylinder
    Returns:
        float: The volume of the cylinder
    """

    return 3.14 * float(radius) * float(radius) * float(height)


geometry_tools = [
    find_area_of_circle,
    find_area_of_rectangle,
    find_area_of_triangle,
    find_area_of_square,
    find_volume_of_cube,
    find_volume_of_sphere,
    find_volume_of_cylinder,
]
