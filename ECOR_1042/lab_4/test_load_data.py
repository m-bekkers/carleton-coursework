# ECOR 1042 Lab 4 - team submission

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your the name of the active members of the team
__author__ = "Matthé Bekkers, James Houghton, Alyssa Eaton, Lelosa Lucky-Ekeka"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-091"

#==========================================#

# Place test_return_list function here 

def test_return_list():
    #Complete the function with your test cases
    
    #test that character_occupation_list returns a list (3 different test cases required)
   
    check.equal(type(load_data.character_occupation_list("characters-test.csv","AT")), list, "Test Failed")

    check.equal(type(load_data.character_occupation_list("characters-test.csv","DB")), list, "Test Failed")
    
    check.equal(type(load_data.character_occupation_list("characters-test.csv","WA")), list, "Test Failed")
    
    #test that character_strength_list returns a list (3 different test cases required)
    
    check.equal(type(load_data.character_strength_list("characters-test.csv", (5,12))), list, "Test Failed")

    check.equal(type(load_data.character_strength_list("characters-test.csv", (7,11))), list, "Test Failed")
    
    check.equal(type(load_data.character_strength_list("characters-test.csv", (8,10))), list, "Test Failed")    
    
    #test that character_luck_list returns a list (3 different test cases required)
    
    check.equal(type(load_data.character_luck_list("characters-test.csv", 0.4)), list, "Test Failed")

    check.equal(type(load_data.character_luck_list("characters-test.csv", 0.7)), list, "Test Failed")
    
    check.equal(type(load_data.character_luck_list("characters-test.csv", 0.9)), list, "Test Failed")     
    
    #test that character_weapon_list returns a list (3 different test cases required)
    
    check.equal(type(load_data.character_weapon_list("characters-test.csv", "Staff")), list, "Test Failed")
    
    check.equal(type(load_data.character_weapon_list("characters-test.csv", "Dagger")), list, "Test Failed")
    
    check.equal(type(load_data.character_weapon_list("characters-test.csv", "Axe")), list, "Test Failed")
    
    #test that load_data returns a list (6 different test cases required)
    
    check.equal(type(load_data.load_data("characters-test.csv", ("Occupation", "AT"))), list, "Test Failed")
    
    check.equal(type(load_data.load_data("characters-test.csv", ("Weapon", "Mace"))), list, "Test Failed")
    
    check.equal(type(load_data.load_data("characters-test.csv", ("Weapon", "Staff"))), list, "Test Failed")
                
    check.equal(type(load_data.load_data("characters-test.csv", ("Luck", 0.5))), list, "Test Failed")
    
    check.equal(type(load_data.load_data("characters-test.csv", ("Strength", (11, 13)))), list, "Test Failed")
                            
    check.equal(type(load_data.load_data("characters-test.csv", ("All", 17))), list, "Test Failed")    
    

    #test that calculate_health returns a list (3 different test cases required)
    
    check.equal(type(load_data.calculate_health(load_data.character_weapon_list("characters-test.csv", "Staff"))), list, "Test Failed")

    check.equal(type(load_data.calculate_health(load_data.character_occupation_list("characters-test.csv","AT"))), list, "Test Failed")
    
    check.equal(type(load_data.calculate_health(load_data.load_data("characters-test.csv", "All"))), list, "Test Failed")

# Place test_return_list_correct_length function here

def test_return_list_correct_length():
    # Complete the function with your test cases

    # test that character_occupation_list returns a list with the correct length (3 different test cases required)

    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "F")), 0)
    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "AT")), 3)
    check.equal(len(load_data.character_occupation_list(
        "characters-test.csv", "WA")), 5)

    # test that character_strength_list returns a list with the correct length (3 different test cases required)

    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (8, 11))), 5)
    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (12, 15))), 12)
    check.equal(len(load_data.character_strength_list(
        "characters-test.csv", (1, 1))), 0)
    # test that character_luck_list returns a list with the correct length (3 different test cases required)

    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0.44)), 2)
    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0)), 0)
    check.equal(len(load_data.character_luck_list(
        "characters-test.csv", 0.5)), 5)

    # test that character_weapon_list returns a list with the correct length(3 different test cases required)

    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Staff")), 4)
    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Club")), 5)
    check.equal(len(load_data.character_weapon_list(
        "characters-test.csv", "Saber")), 0)

    # test that load_data returns a list with the correct length (6 different test cases required)

    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Occupation", "F"))), 0)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Strength", (3, 10)))), 4)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Weapon", "Mace"))), 0)
    check.within(len(load_data.load_data(
        "characters-test.csv", ("Luck", 0.7))), 19.0, 1)
    check.equal(len(load_data.load_data("characters-test.csv", ("All"))), 0)
    check.equal(len(load_data.load_data(
        "characters-test.csv", ("Invalid Filter", "Test"))), 0)

    # test that calculate_health returns a list with the correct length (3 different test cases required)

    characters = load_data.load_data("characters-test.csv", ("All"))
    check.equal(len(load_data.calculate_health(characters)), len(characters))

    characters = load_data.load_data(
        "characters-test.csv", ("Occupation", "AT"))
    health = load_data.calculate_health(characters)
    check.equal(isinstance(health, list), True)

    health = load_data.calculate_health([])
    check.equal(len(health), 0)

#Place test_return_correct_dict_inside_list function here

def test_return_correct_dict_inside_list():
    #Complete the function with your test cases
    
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    
    check.equal(((load_data.character_occupation_list("characters-test.csv", "AT")[0])), {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(((load_data.character_occupation_list("characters-test.csv", "AT")[-1])), {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'})
    check.equal(((load_data.character_occupation_list("characters-test.csv", "DB")[0])), {'Strength': 15, 'Agility': 4, 'Stamina': 10, 'Personality': 11, 'Intelligence': 3, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Club'})
    check.equal(((load_data.character_occupation_list("characters-test.csv", "DB")[-1])), {'Strength': 10, 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'})
    
    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
    
    check.equal(((load_data.character_strength_list("characters-test.csv", (7, 13))[0])), {'Occupation': 'AT', 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'})
    check.equal(((load_data.character_strength_list("characters-test.csv", (7, 13))[-1])), {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'})
    check.equal(((load_data.character_strength_list("characters-test.csv", (8, 11))[0])), {'Occupation': 'DB', 'Agility': 10, 'Stamina': 11, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'})
    check.equal(((load_data.character_strength_list("characters-test.csv", (8, 11))[-1])), {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'})    
    
    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    
    check.equal(((load_data.character_luck_list("characters-test.csv", 0.4)[0])), {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'})
    check.equal(((load_data.character_luck_list("characters-test.csv", 0.4)[-1])), {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(((load_data.character_luck_list("characters-test.csv", 0.53)[0])), {'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Club'})
    check.equal(((load_data.character_luck_list("characters-test.csv", 0.53)[-1])), {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'})
    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)
    
    check.equal(((load_data.character_weapon_list("characters-test.csv", "Staff")[0])), {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10})
    check.equal(((load_data.character_weapon_list("characters-test.csv", "Staff")[-1])), {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10})
    check.equal(((load_data.character_weapon_list("characters-test.csv", "Club")[0])), {'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10})
    check.equal(((load_data.character_weapon_list("characters-test.csv", "Club")[-1])), {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10})    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    
    check.equal(((load_data.load_data("characters-test.csv", ("Occupation", "AT"))[0])), {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'})
    check.equal(((load_data.load_data("characters-test.csv", ("Occupation", "AT"))[-1])), {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'})
    check.equal(((load_data.load_data("characters-test.csv", ("Weapon", "Staff"))[0])), {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10})
    check.equal(((load_data.load_data("characters-test.csv", ("Weapon", "Staff"))[-1])), {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10})    
    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
    
    check.equal((load_data.calculate_health(load_data.character_weapon_list("characters-test.csv", "Staff"))[0]), {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Health': 115.0})
    check.equal((load_data.calculate_health(load_data.character_weapon_list("characters-test.csv", "Staff"))[-1]), {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Health': 83.0})
    check.equal((load_data.calculate_health(load_data.character_occupation_list("characters-test.csv", "AT"))[0]), {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff', 'Health': 115.0})
    check.equal((load_data.calculate_health(load_data.character_occupation_list("characters-test.csv", "AT"))[-1]), {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger', 'Health': 98.0})

#Place test_calculate_health function here

def test_calculate_health():
    # Complete the function with your test cases

    # test that the function does not change the length of the list provided as input parameter (5 different test cases required)

    # Case for 'Occupation'.
    check.equal(len(load_data.calculate_health(load_data.load_data("characters-test.csv", ("Occupation", "AT")))), len(load_data.load_data("characters-test.csv", ("Occupation", "AT"))), 
                "Checks if the 'calculate_health' function changes the length of the list.")
    
    # Case where Strength is not a key in the dictionary.
    try:
        load_data.calculate_health(load_data.load_data("characters-test.csv", ("Strength", (11, 13))))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Luck is not a key in the dictionary
    try:
        load_data.calculate_health(load_data.load_data("characters-test.csv", ("Luck", 0.67)))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)
    
    # Case where Weapon is not a key in the dictionary
    check.equal(len(load_data.calculate_health(load_data.load_data("characters-test.csv", ("Weapon", "Sling")))), len(load_data.load_data("characters-test.csv", ("Weapon", "Sling"))), 
                "Checks if the 'calculate_health' function changes the length of the list.")

    # Case where All is called
    check.equal(len(load_data.calculate_health(load_data.load_data("characters-test.csv", ("All")))), len(load_data.load_data("characters-test.csv", ("All"))), 
                "Checks if the 'calculate_health' function changes the length of the list.")

    # test that the function returns an empty list when it is called whith an empty list

    check.equal(load_data.calculate_health(load_data.load_data("characters-mat.csv", "Value")), [], 
                "Checks if the 'calculate health' function returns an empty list if an empty list is provided.")

    # test that the function incrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)

    # Case where Occupation is not a key in the dictionary
    check.equal(len((load_data.calculate_health(load_data.load_data("characters-test.csv", ("Occupation", "AT"))))[0]), len(load_data.load_data("characters-test.csv", ("Occupation", "AT"))[0]) + 1, 
                "Checks if the 'calculate_health' funciton adds a key to the dictionary")

    # Case where Strength is not a key in the dictionary
    try:
        load_data.calculate_health(load_data.load_data("characters-test.csv", ("Strength", (11, 13))))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Luck is not a key in the dictionary
    try:
        load_data.calculate_health(load_data.load_data("characters-test.csv", ("Luck", 0.67)))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)

    # Case where Weapon is not in the dictionary
    check.equal(len(load_data.calculate_health(load_data.load_data("characters-test.csv", ("Weapon", "Sling")))[0]), len(load_data.load_data("characters-test.csv", ("Weapon", "Sling"))[0]) + 1, 
                "Checks if the 'calculate_health' funciton adds a key to the dictionary")

    # Case where All is called
    check.equal(len(load_data.calculate_health(load_data.load_data("characters-test.csv", ("All", ("Value"))))[0]), len(load_data.load_data("characters-test.csv", ("All", ("value", "value")))[0]) + 1, 
                "Checks if the 'calculate_health' funciton adds a key to the dictionary")

    # test that the Health value is properly calculated  (5 different test cases required)

    # Case where Occupation is not a key in the dictionary
    check.equal((load_data.calculate_health(load_data.load_data("characters-test.csv", ("Occupation", "AT")))[0]).get("Health"), 115.0)
   
    # Case where Strength is not a key in the dictionary
    try:
        load_data.calculate_health(load_data.load_data("characters-test.csv", ("Strength", (11, 13))))[0]["Health"]
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)
   
    # Case where Luck is not a key in the dictionary
    try:
        load_data.calculate_health(load_data.load_data("characters-test.csv", ("Luck", 0.67)))
    except KeyError:
        check.equal(True, True)
    else:
        check.equal(True, False)
   
    # Case where Weapon is not in the dictionary
    check.equal((load_data.calculate_health(load_data.load_data("characters-test.csv", ("Weapon", "Sling")))[0]).get("Health"), 141.0)
   
    #Case where All is called
    check.equal((load_data.calculate_health(load_data.load_data("characters-test.csv", ("All", "Value")))[0]).get("Health"), 115.0)
   
    check.summary(False)

# Do NOT include a main script in your submission
