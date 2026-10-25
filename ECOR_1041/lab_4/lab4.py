# ECOR 1041 Lab 4

__author__ = "Matthé Bekkers"
__student_number__ = "101297066"

import math

# =====================================================
# Exercise 1


def area_of_disk(radius: float) -> float:
    """Return the area of a disk with the specified radius.
    Precondidion: radius >= 0.
    >>> area_of_disk(5)
    78.54
    """

    return math.pi * radius ** 2

# =======================================================
# Exercise 2


LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934


def convert_to_litres_per_100_km(mpg: float) -> float:
    """ Return a conversion between miles per gallon and liters per kilometer with the specified mileage per gallon.
    Precondition: mpg > 0.
    >>> convert_to_litres_per_100_km(32)
    8.83
    >>> convert_to_litres_per_100_km(10)
    28.25
    >>> convert_to_litres_per_100_km(14.123)
    20.00
    """
    return 1 / ((mpg * KMS_PER_MILE) / LITRES_PER_GALLON) * 100

# =======================================================
# Exercise 3


def accumulated_amount(principal: float, rate: float, n: int, time: int) -> float:
    """ Return the accumulated amount with the specified prinicpal, rate of accumulation of interest, the "n" amount of times the interest is compounded each year, and amount of time the money is garnered.
    Precondition: n >= 0
    >>> accumulated_amount(1500, 0.043, 4, 6)
    1938.84
    >>> accumulated_amount(0, 0.42, 5, 15)
    0.0
    >>> accumulated_amount(-1000, 0.125, 12, 100)
    -251536765.48
    """
    return principal * (1 + (rate / n)) ** (n * time)

# =======================================================
# Exercise 4


def area_of_cone(height: float, radius: float) -> float:
    """ Return the volume of a cone with the specified height and radius.
    Precondition: height, radius >= 0
    >>> area_of_cone(4, 4)
    71.09
    >>> area_of_cone(0, 1)
    3.14
    >>> area_of_cone(1, -1)
    -4.44
    """
    return math.pi * radius * math.sqrt(radius * radius + height * height)


# =======================================================
# Exercise 5
def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """Return the distance between 2 points with the specified x and y coordinates.
    >>> distance(1, 6, 2, 7)
    (1.41)
    >>> distance(0, -5, 4, -1)
    (5.66)
    >>> distance(3, 6, -1, -7)
    (13.60)
    """
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def area_of_circle(xc: int, yc: int, xp: int, yp: int) -> float:
    """Returns the area of a circle with the specified centre of the circle and point on the perimeter.
    >>> area_of_circle(1, 6, 2, 7)
    8.89
    >>> area_of_circle(0, -5, 4, -1)
    35.5
    >>> area_of_circle(3, 6, -1, -7)
    85.46
    """
    return math.pi * pow(distance(xc, yc, xp, yp), 2)