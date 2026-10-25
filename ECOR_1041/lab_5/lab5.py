# ECOR 1041 Lab 5

__author__ = "Matthé Bekkers"
__student_number__ = "101297066"

#======================================================
# Exercise 1


def tip(cost: float, satisfaction: int) -> float:
    """Returns the value of the tip based on the provided cost and satisfaction level.
    Precondition: cost > 0
    Precondition: 1 <= satisfaction <= 3
    >>> tip(15.99, 1)
    8.00
    >>> tip(103.26, 3)
    20.65
    >>> tip(45.56, 2)
    6.83
    """
    if satisfaction == 3:
        return cost * 0.05
    elif satisfaction == 2:
        return cost * 0.15
    elif satisfaction == 1:
        return cost * 0.2
    
#======================================================
# Exercise 2
    

def coupon(amount_spent: float) -> float:
    """Return the value of a coupon based on the provided amount of groceries spent.
    Precondition: amount_spent > 0
    >>> coupon(15)
    1.2
    >>> coupon(399.99)
    56.00
    >>> coupon(69.99)
    7.00
    """
    if amount_spent < 10:
        return 0
    elif 10 <= amount_spent <= 60:
        return amount_spent * 0.08
    elif 60 < amount_spent <= 150:
        return amount_spent * 0.1
    elif 150 < amount_spent <= 210:
        return amount_spent * 0.12
    else:
        return amount_spent * 0.14


#======================================================
# Exercise 3
    

def bakers_party(weekend: bool, number_of_pastries: int) -> bool:
    """Return whether the baker's party was a success depending on the provided day of the week and number of pastries consumed.
    Precondition: number_of_pastries >= 0
    >>> bakers_party(False, 235)
    False
    >>> bakers_party(True, 1)
    False
    >>> bakers_party(False, -4)
    False
    """
    if weekend:
        if number_of_pastries < 40:
            return False
        else:
            return True
    else:
        if number_of_pastries < 40:
            return False
        elif 40 <= number_of_pastries <= 60:
            return True
        else:
            return False

#======================================================
# Exercise 4

def squirrel_play(season: bool, temperature: int) -> float:
    """Returns whether the squirrels are playing based on the provided season and temperature.
    No preconditions.
    >>> squirrel_play(False, 69)
    True
    >>> squirrel_play(True, 102)
    False
    >>> squirrel_play(False, 4)
    False
    """
    if season:
        if temperature < 60:
            return False
        elif 60 <= temperature <= 100:
            return True
        else:
            return False
    else:
        if temperature < 60:
            return False
        elif 60 <= temperature <= 90:
            return True
        else:
            return False


#======================================================
# Exercise 5
    

def great_42(a: int, b: int) -> bool:
    """Return 'True' if the absolute value of the 2 provided integers is equal to 42.
    No preconditions.
    >>> great_42(1, 2)
    False
    >>> great_42(12, 30)
    True
    >>> great_42(-12, -30)
    True
    """
    return abs(a - b) == 42 or a == 42 or b == 42 or a + b == 42


#======================================================
# Exercise 6


def multiply_uniques(a: int, b: int, c: int) -> int:
    """Returns the product of the three given integer values. However, if there are duplicates, the value of one of the duplicates is not calculated.
    >>> multiply_uniques(1, 2, 2)
    2
    >>> multiply_uniques(1, 2, 3)
    6
    >>> multiply_uniques(5, 5, 5)
    5
    """
    if a == b and a == c and c == b:
        return 1
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a * b * c
