# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Matthé Bekkers, Alyssa Eaton, Lelosa Lucky-Ekeka, James Houghton"

# Update "" with your team (e.g. T102)
__team__ = "t-091"

#==========================================#
# Place your sort_characters_agility_bubble function after this line

def sort_characters_agility_bubble(characters: list[dict], order: str) -> list[dict]:
    """
    Takes the dictionary list of characters with an order command of ascending or descending  
    (in the form of a string) and bubble sorts the list in that order. If agility
    is not in the list, its returns '"agility" is not a key in the dictionary'.
    
    >>>sort_characters_agility_bubble([{'Occupation': 'EB',
    'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]
    
        >>>sort_characters_agility_bubble([{'Occupation': 'EB',
    'Agility': 14}, {'Occupation': 'H', 'Agility': 10}], "A")
    [{'Occupation': 'H', 'Agility': 10}, {'Occupation': 'EB', 'Agility': 14}]
    
    >>>sort_characters_agility_bubble([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    "Agility" key is not present.
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    """

    if characters == []:
        return(characters)
    n = len(characters)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if 'Agility' in characters[j] and 'Agility' in characters[j + 1]:
                if order == 'A':
                    if characters[j]['Agility'] > characters[j + 1]['Agility']:
                        characters[j], characters[j + 1] = characters[j + 1], characters[j]
                elif order == 'D':
                    if characters[j]['Agility'] < characters[j + 1]['Agility']:
                        characters[j], characters[j + 1] = characters[j + 1], characters[j]
            else:
                print('"Agility" key is not present')
                return (characters)
    return (characters)

#==========================================#
# Place your sort_characters_intelligence_selection function after this line

def sort_characters_intelligence_selection(characters_list: list[dict], order: str) -> list[dict]:
    """Returns the sorted list using the specified input_list and order if the key "Intelligence" is present otherwise returns the original unsorted list together with a print statement. 
    Preconditions: 
        - characters_list should be a list of dictionaries,
        - characters_list should not be empty,
        - each dictionary with the "Intelligence" key should have a numerical value associated with it,
        - order must be "D" or "A".
    >>> sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]
    >>> sort_characters_intelligence_selection([{'Occupation':'EB'}, {Occupation': 'M'}], "D")
    'Intelligence' key is not present.
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    >>>sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}], "A")
    [{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}]
    """
    try:
        for i in range(len(characters_list)):
                min_index = i
                min_intelligence = characters_list[i]["Intelligence"]
                for j in range(i + 1, len(characters_list)):
                    if "Intelligence" in characters_list[j]:
                        curr_intelligence = characters_list[j]["Intelligence"]
                        if((order == "A" and curr_intelligence < min_intelligence) or (order == "D" and curr_intelligence > min_intelligence)):
                            min_intelligence = curr_intelligence
                            min_index = j
                characters_list[i], characters_list[min_index] = characters_list[min_index], characters_list[i]
        return characters_list
    except KeyError:
        print("'Intelligence' key is not present.")
        return characters_list

#==========================================#
# Place your sort_characters_health_insertion function after this line


def sort_characters_health_insertion(list: list[dict], order: str) -> list[dict]:
    """Return the sorted list of characters' dictionaries by the "Health" attribute, either ascending or descending depending on the order parameter, using the insertion sort algorithm. If "Health" is a key in the dictionary, the function returns the sorted list and is "Health" is not a key in the dictionary the function prints a message stating the key is not in the dictionary and returns the original list.
    
    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]
    
    >>> sort_characters_health_insertion([{'Occupation': 'EB'}, {'Occupation':'M'}], "A")
    "Health" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """

    for dict in list:
        if "Health" not in dict:
            print('"Health" key is not present')
            return list 
    
    if order == "A":
        for i in range(1, len(list)):
            key = list[i]
            j = i-1
            while j >= 0 and key["Health"] < list[j]["Health"]:
                list[j+1] = list[j]
                j -=1
            list[j+1] = key
    elif order == "D":
        for i in range (1, len(list)):
            key = list[i]
            j = i-1
            while j >= 0 and list[j]["Health"] < key["Health"]:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key
    return list

#==========================================#
# Place your sort_characters_armor_bubble function after this line

def sort_characters_armor_bubble(org_list: list[dict], order: str) -> list[dict]:
    """Returns the provided dictionaries sorted in either ascending or descending order depending on the character's health values.
    Precondition: order must be 'A' or 'D'.
    >>> sort_characters_armor_bubble([{'Strength': 13, 'Armor': 12, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 3, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 9, 'Armor': 11, 'Weapon': 'Staff'}], "A")
    [{'Strength': 12, 'Agility': 3, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 9, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 13, 'Armor': 12, 'Weapon': 'Staff'}]
    >>> sort_characters_armor_bubble([{'Strength': 13, 'Armor': 12, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 3, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 9, 'Armor': 11, 'Weapon': 'Staff'}], "D")
    [{'Strength': 13, 'Armor': 12, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 3, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 9, 'Armor': 11, 'Weapon': 'Staff'}]
    >>> sort_characters_armor_bubble([{'Strength': 13, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 3, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 9, 'Armor': 11, 'Weapon': 'Staff'}], "D")
    KeyError: Armor is not a key in dictionary 1 of 3.
    [{'Strength': 13, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 3, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 9, 'Armor': 11, 'Weapon': 'Staff'}]
    """

    # Checks if Armor is a key in the provided dictionaries
    for j in range(len(org_list) - 1):
        if "Armor" not in org_list[j]:
            print("KeyError: Armor is not a key in dictionary " + str(j + 1) + " of " + str(len(org_list)) + ".")
            return org_list

    # Case where user wants the list sorted in ascending order
    if order == "A":
        # Bubble sort algorithm
        swap = True
        while swap:
            swap = False
            for i in range(len(org_list) - 1):
                if org_list[i]["Armor"] > org_list[i + 1]["Armor"]:
                    # Swaps the two elements
                    tmp = org_list[i]
                    org_list[i] = org_list[i + 1]
                    org_list[i + 1] = tmp
                    swap = True

    elif order == "D":
        # Bubble sort for descending order
        swap = True
        while swap:
            swap = False
            for i in range(len(org_list) - 1):
                if org_list[i]["Armor"] < org_list[i + 1]["Armor"]:
                    # Swaps the two elements
                    tmp = org_list[i]
                    org_list[i] = org_list[i + 1]
                    org_list[i + 1] = tmp
                    swap = True

    return org_list

#==========================================#
# Place your sort function after this line

def sort(dict_list: list[dict], order: str, attr: str) -> list[dict]:
    """Returns the provided list of dictionaries sorted according to the provided attribute and order.
    Precondition: order must equal either 'A' or 'D'.
    >>>

    >>>

    >>>

    """

    for i in range(len(dict_list) - 1):

        if attr not in dict_list[i]:

            print("KeyError: Cannot sort by " + attr + " since dictionary " + str(i + 1) + " does not contain " + attr + ".")
            return dict_list
        
        elif attr == "Agility":
            return sort_characters_agility_bubble(dict_list, order)

        elif attr == "Intelligence":
            pass
            return sort_characters_intelligence_selection(dict_list, order)

        elif attr == "Health":

            return sort_characters_health_insertion(dict_list, order)

        elif attr == "Armor":

            return sort_characters_armor_bubble(dict_list, order)

#print(sort(, "A", "Health"))

# Do NOT include a main script in your submission
