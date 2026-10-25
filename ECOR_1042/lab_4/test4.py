# ECOR 1042 Lab 4 - Individual submission for test4 function

# import check module here
import check

# import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Matthé Bekkers"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297066"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T091"

#==========================================#
# Do not modify the code already provided.


def test_calculate_health():
    # Complete the function with your test cases

    # test that the function does not change the length of the list provided as input parameter (5 different test cases required)

    # Case for 'Occupation'.
    check.equal(len(load_data.calculate_health("characters-test.csv", ("Occupation", "AT"))), len(load_data("characters-test.csv", ("Occupation", "AT"))), 
                "Checks if the 'calculate_health' function changes the length of the list.")
    
    # Case where Strength is not a key in the dictionary.
    try:
        load_data.calculate_health("characters-test.csv", ("Strength", (11, 13)))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Luck is not a key in the dictionary
    try:
        load_data.calculate_health("characters-test.csv", ("Luck", 0.67))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)
    
    # Case where Weapon is not a key in the dictionary
    check.equal(len(load_data.calculate_health("characters-test.csv", ("Weapon", "Sling"))), len(load_data("characters-test.csv", ("Weapon", "Sling"))), 
                "Checks if the 'calculate_health' function changes the length of the list.")
    
    # Case where All is called
    check.equal(len(load_data.calculate_health("characters-test.csv", ("All"))), len(load_data("characters-test.csv", ("All"))), 
                "Checks if the 'calculate_health' function changes the length of the list.")

    # test that the function returns an empty list when it is called whith an empty list

    check.equal(load_data.calculate_health("characters-mat.csv", "Value"), [], 
                "Checks if the 'calculate health' function returns an empty list if an empty list is provided.")

    # test that the function incrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)

    # Case where Occupation is not a key in the dictionary
    check.equal(len((load_data.calculate_health("characters-test.csv", ("Occupation", "AT")))[0]), len(load_data("characters-test.csv", ("Occupation", "AT"))[0]) + 1, 
                "Checks if the 'calculate_health' funciton adds a key to the dictionary")
    
    # Case where Strength is not a key in the dictionary
    try:
        load_data.calculate_health("characters-test.csv", ("Strength", (11, 13)))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Luck is not a key in the dictionary
    try:
        load_data.calculate_health("characters-test.csv", ("Luck", 0.67))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Weapon is not in the dictionary
    check.equal(len(load_data.calculate_health("characters-test.csv", ("Weapon", "Sling"))[0]), len(load_data("characters-test.csv", ("Weapon", "Sling"))[0]) + 1, 
                "Checks if the 'calculate_health' funciton adds a key to the dictionary")

    # Case where All is called
    check.equal(len(load_data.calculate_health("characters-test.csv", ("All", ("Value")))[0]), len(load_data("characters-test.csv", ("All", ("value", "value")))[0]) + 1, 
                "Checks if the 'calculate_health' funciton adds a key to the dictionary")

    # test that the Health value is properly calculated  (5 different test cases required)

    # Case where Occupation is not a key in the dictionary
    check.equal((load_data.calculate_health("characters-test.csv", ("Occupation", "AT"))[0]).get("Health"), 115.0)

    # Case where Strength is not a key in the dictionary
    try:
        load_data.calculate_health("characters-test.csv", ("Strength", (11, 13)))[0]["Health"]
    except KeyError:
        print("excepted")
        check.equal(True, True)
    else:
        print("elsed")
        check.equal(True, False)

    # Case where Luck is not a key in the dictionary
    try:
        load_data.calculate_health("characters-test.csv", ("Luck", 0.67))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Weapon is not in the dictionary
    check.equal((load_data.calculate_health("characters-test.csv", ("Weapon", "Sling"))[0]).get("Health"), 141.0)

    #Case where All is called
    check.equal((load_data.calculate_health("characters-test.csv", ("All", "Value"))[0]).get("Health"), 115.0)

    check.summary(False)

    # Do NOT include a main script in your submission
