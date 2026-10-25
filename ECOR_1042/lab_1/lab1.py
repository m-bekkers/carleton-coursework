# ECOR 1041 - Bonus

__author__ = "Matthé Bekkers"
__student_number__ = "101297066"

# ======================================================
# Exercise 1

def replicate(x: str) -> str:
    """Returns a string with n copies of the argument, where n is the amount of characters in the argument.
    >>> replicate("abc")
    "abcabcabc"
    >>> replicate("sentence")
    "sentencesentencesentencesentencesentencesentencesentencesentence"
    >>> replicate("cd")
    "cdcd"
    """
    x = str(x) # Ensures that x is a string
    y = ""
    for i in range(len(x)):
        y = y + x

    return y

# ======================================================
# Exercise 2

def repeat_separator(word: str, sep: str, n: int) -> str:
    """Returns a string with word printed n amount of times, separated by the provided sep.
    >>> repeat_separator("hello", "-", 2)
    "hello-hello"
    >>> repeat_separator("sky", "up", 4)
    "skyupskyupskyupsky"
    >>> repeat_separator("up", "dog", 3)
    "updogupdogup:
    """
    word = str(word)
    sep = str(sep)
    x = ""
    for i in range(n):
        if i < n - 1:
            x = x + word + sep
        else:
            x = x + word

    return x


# ======================================================
# Exercise 3

def has_pair(s: str, ch: str) -> bool:
    """Returns True if s contains 2 iterations of ch side-by-side
    Preconditions: len(s) >= 2, len(ch) == 1
    >>> has_pair("accd", "c")
    True
    >>> print(has_pair("fdatdg", "d"))
    False
    >>> print(has_pair("adddsiiii", "i"))
    True
    """
    found = False

    for i in range(len(s) -1):
        if s[i] == ch and s[i + 1] == ch:
            found = True
            break

    return found


# ======================================================
# Exercise 4

def middle_way(a: list, b: list) -> list:
    """Returns a new list containing the middle elements of the provided lists.
    Preconditions, len(a) == 3, len(b) == 2, the list must contain only integers.
    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    >>> middle_way([-4, 2, 1], [4, 7, 6])
    [2, 7]
    >>> middle_way([-1, 2, 6], [-4, -5, 0])
    [2, -5]
    """

    return [a[1], b[1]]

# ======================================================
# Exercise 5

def make_ends(a: list) -> list:
    """Returns a new list containing the first and last elements from the provided list.
    Preconditions: len(a) > 0, the list must contain only integers..
    >>> make_ends([2, 5, 1, 6, 6])
    [2, 6]
    >>> make_ends([4, 5, 2, 6, -8])
    [4, -8]
    >>> make_ends([-6, 35, 100, 65, 26])
    [-6, 26]
    """

    return [a[0], a[-1]]

# ======================================================
# Exercise 6

def common_end(a: list, b: list) -> bool:
    """Returns whether the the two provided lists have matching first entries, last entries, or if the first entry in a list matches the last entry in the other.
    Precondition: len(a) > 0, len(b) > 0, the list must contain only integers.
    >>> common_end([1, 2, 3], [4, 2, 3])
    True
    >>> common_end([1, 2, 1], [4, 2, 3])
    False
    >>> print(common_end([1, 2, 3], [4, 2, 1]))
    True
    """

    return a[0] == b[0] or a[-1] == b[-1]


# ======================================================
# Exercise 7

def count_evens(a: list) -> int:
    """Returns the amount of even numbers in the provided list.
    Precondition: the list must contain only integers..
    >>> count_evens([1, 2, 3])
    1
    >>> count_evens([4, 4, 4])
    3
    >>> count_evens([3, 7, 5])
    0
    """

    count = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            count += 1
    
    return count


# ======================================================
# Exercise 8

def big_diff(nums: list) -> int:
    """Retuns the difference between the smallest item in the provided list and the largest item in the provided list.
    Precondtions: len(nums) > 1, the list must contain only integers.
    >>> big_diff([1, 2, 3, 4, 5])
    4
    >>> big_diff([5, 2, 25, 9, 6])
    23
    >>> big_diff([152, 152, 992, 19, 4419])
    4400
    """

    big = nums[0]
    small = nums[0]

    for i in range(len(nums)):
        if nums[i] > big:
            big = nums[i]
        elif nums[i] < small:
            small = nums[i]

    return big - small


# ======================================================
# Exercise 9
def has22(nums: list) -> bool:
    """Returns whether the list contains two instances of the number '2' next to each other.
    >>> has22([2, 2, 5, 3])
    True
    >>> has22([6, 2, 6, 2])
    False
    >>> has22([1, 2, 2])
    True
    """

    for i in range(len(nums) - 1):
        if nums[i + 1] == 2 and nums[i + 2] == 2:
            return True
        else:
            return False
        

# ======================================================
# Exercise 10

def centered_average(nums: list) -> float:
    """Returns the centred average of the provided list.
    Preconditions: len(nums) > 2, the list must contain only integers.
    >>> centered_average([11, 25, 2, 6, 24])
    13.67
    >>> centered_average([1, 5, 2, 76, 2])
    3
    >>> centered_average([1421, 512, 241, 71246, 222])
    274.67
    """
    
    average = 0
    nums_max = max(nums)
    nums_min = min(nums)

    for i in range(len(nums)):
        average += nums[i]

    average -= nums_max
    average -= nums_min

    return round((average / (len(nums) - 2)), 2)


# ======================================================
# Exercise 11

def bank_statement(transactions: list) -> list:
    """Returns a list with three elements: the sum of all deposits, the sum of all withdrawals, and the sum of all transactions.
    Preconditions: len(transactions) > 0, all list elements must be floats.
    >>> bank_statement([2837, -17573, 1, 882, -572])
    [3720, 18145, -14425]
    >>> bank_statement([283, -173, 11424, -182, -252])
    [11706, 607, 11099]
    >>> bank_statement([-2230, 1733, 2144, 2342, -5722])
    [7952, -7952, 0]
    """

    deposits = 0
    withdrawals = 0
    total = 0

    for i in range(len(transactions)):
        if transactions[i] > 0:
            deposits += float(transactions[i])
        elif transactions[i] < 0:
            withdrawals += float(transactions[i])

        total += transactions[i]

    return [round(deposits, 2), round(withdrawals, 2), round(total, 2)]


# ======================================================
# Exercise 12

def reverse(nums: list) -> list:
    """Returns the provided list in reverse order.
    No preconditions.
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([6, 4, 15, 6])
    [6, 15, 4, 6]
    >>> reverse([11, 22, 33, 44])
    [44, 33, 22, 11]
    """

    new_list = [None] * len(nums)
    n = -1

    for i in range(len(nums)):
        new_list[n] = nums[i]
        n -= 1

    return new_list
