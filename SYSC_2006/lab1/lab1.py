# SYSC 2006 - Lab 1 Solution template

__author__ = "Matthé Bekkers"
__student_number__ = "101297066"

# Type your solution to exercise 1 after this line
def alarm_clock(day: int, vacation: bool) -> str:
    """This function takes the current day of the week and whether it is a vacation period.
    It returns a string containing the time at which the alarm will go off.
    Precondition: 0 <= day <= 6
    >>> alarm_clock(1, True)
    "10:00"
    >>> alarm_clock(3, False)
    "7:00"
    >>> alarm_clock(6, True)
    "off"
    """

    if vacation:
        if 1 <= day <= 5:
            return "10:00"
        else:
            return "off"
    else:
        if 1 <= day <= 5:
            return "07:00"
        else:
            return "10:00"

# Type your solution to exercise 2 after this line
def count_replace():
    """This function asks the user for input. This input determines how long the program will run. The program displays the numbers leading up to the user-provided number, replacing 
    multiples of 3 with Fizz, multiples of 5 with Buzz, and multiples of both with FizzBuzz.
    Preconditions: The user input must be positive.
    >>> count_replace()
    "Please input a target number: 
    10
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz
    >>> count_replace()
    "Please input a target number: 
    4
    1 2 Fizz 4
    >>> count_replace()
    "Please input a target number: 
    15
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
    """
    num = int(input("Please input a target number: "))

    for i in range(1, num + 1):
        string = ""
        if i % 3 == 0:
            string = string + "Fizz"
        if i % 5 == 0:
            string = string + "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            string = string + str(i)
        
        print(string, end= " ")
        
# Type your solution to exercise 3 after this line
def is_prime(num: int) -> bool:
    """This function checks to see if the provided number is a prime number.
    Preconditions: num >= 0
    >>> is_prime(2)
    False
    >>> is_prime(15)
    False
    >>> is_prime(7)
    True
    """
    print(str(num))
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if num > 2:
        return False
    else:
        return prime



# Type your solution to exercise 4 after this line
def divisors(num: int) -> list[int]:
    """This function takes an integer and returns a list of its positive divisors.
    Preconditions: num >= 0
    >>> divisors(4)
    [1, 2, 4]
    >>> divisors(8)
    [1, 2, 4, 8]
    >>> divisors(15)
    [1, 3, 5, 15]
    """
    divs = []

    for i in range(num, 0, -1):
        if num % i == 0:
            divs.insert(0, i)
    
    return divs