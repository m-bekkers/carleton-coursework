# ECOR 1042 Lab 5 - Individual submission for sort_characters_armor_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Rami Sabouni)
__author__ = "Matthé Bekkers"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297066"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-091"

#==========================================#
# Place your sort_characters_armor_bubble function after this line

#x = [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}, {'Strength': 9, 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 14, 'Agility': 2, 'Stamina': 8, 'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8, 'Weapon': 'Club'}, {'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}, {'Strength': 18, 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Club'}, {'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 14, 'Intelligence': 11, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Club'}, {'Strength': 15, 'Agility': 11, 'Stamina': 10, 'Personality': 13, 'Intelligence': 9, 'Luck': 0.94, 'Armor': 11, 'Weapon': 'Club'}, {'Strength': 15, 'Agility': 11, 'Stamina': 8, 'Personality': 16, 'Intelligence': 9, 'Luck': 0.78, 'Armor': 11, 'Weapon': 'Club'}, {'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}, {'Strength': 7, 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9, 'Weapon': 'Dagger'}, {'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 16, 'Agility': 8, 'Stamina': 8, 'Personality': 7, 'Intelligence': 9, 'Luck': 0.94, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 13, 'Agility': 8, 'Stamina': 8, 'Personality': 6, 'Intelligence': 10, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 8, 'Agility': 10, 'Stamina': 11, 'Personality': 16, 'Intelligence': 8, 'Luck': 0.33, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 10, 'Agility': 7, 'Stamina': 12, 'Personality': 6, 'Intelligence': 16, 'Luck': 0.56, 'Armor': 10, 'Weapon': 'Club'}, {'Strength': 13, 'Agility': 5, 'Stamina': 10, 'Personality': 12, 'Intelligence': 12, 'Luck': 0.44, 'Armor': 9, 'Weapon': 'Club'}, {'Strength': 15, 'Agility': 7, 'Stamina': 7, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Club'}, {'Strength': 14, 'Agility': 3, 'Stamina': 8, 'Personality': 14, 'Intelligence': 8, 'Luck': 0.78, 'Armor': 8, 'Weapon': 'Club'}, {'Strength': 16, 'Agility': 5, 'Stamina': 6, 'Personality': 17, 'Intelligence': 10, 'Luck': 0.39, 'Armor': 9, 'Weapon': 'Club'}, {'Strength': 12, 'Agility': 6, 'Stamina': 10, 'Personality': 11, 'Intelligence': 12, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Dagger'}, {'Strength': 14, 'Agility': 12, 'Stamina': 4, 'Personality': 12, 'Intelligence': 10, 'Luck': 0.33, 'Armor': 11, 'Weapon': 'Dagger'}, {'Strength': 12, 'Agility': 6, 'Stamina': 10, 'Personality': 8, 'Intelligence': 8, 'Luck': 0.72, 'Armor': 9, 'Weapon': 'Dagger'}, {'Strength': 16, 'Agility': 12, 'Stamina': 10, 'Personality': 15, 'Intelligence': 11, 'Luck': 0.5, 'Armor': 11, 'Weapon': 'Dagger'}, {'Strength': 14, 'Agility': 9, 'Stamina': 11, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 11, 'Agility': 8, 'Stamina': 11, 'Personality': 12, 'Intelligence': 11, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 15, 'Agility': 7, 'Stamina': 7, 'Personality': 6, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Dagger'}, {'Strength': 13, 'Agility': 5, 'Stamina': 5, 'Personality': 7, 'Intelligence': 12, 'Luck': 0.5, 'Armor': 9, 'Weapon': 'Staff'}, {'Strength': 14, 'Agility': 2, 'Stamina': 6, 'Personality': 9, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 8, 'Weapon': 'Staff'}, {'Strength': 14, 'Agility': 10, 'Stamina': 4, 'Personality': 13, 'Intelligence': 8, 'Luck': 0.78, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 15, 'Agility': 6, 'Stamina': 12, 'Personality': 9, 'Intelligence': 11, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Staff'}, {'Strength': 18, 'Agility': 10, 'Stamina': 7, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 9, 'Agility': 6, 'Stamina': 10, 'Personality': 13, 'Intelligence': 10, 'Luck': 0.5, 'Armor': 9, 'Weapon': 'Staff'}, {'Strength': 12, 'Agility': 15, 'Stamina': 11, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.5, 'Armor': 12, 'Weapon': 'Staff'}, {'Strength': 15, 'Agility': 11, 'Stamina': 9, 'Personality': 15, 'Intelligence': 4, 'Luck': 0.56, 'Armor': 11, 'Weapon': 'Staff'}, {'Strength': 11, 'Agility': 6, 'Stamina': 8, 'Personality': 10, 'Intelligence': 10, 'Luck': 0.78, 'Armor': 9, 'Weapon': 'Staff'}, {'Strength': 15, 'Agility': 9, 'Stamina': 6, 'Personality': 8, 'Intelligence': 10, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 14, 'Agility': 5, 'Stamina': 6, 'Personality': 13, 'Intelligence': 9, 'Luck': 0.22, 'Armor': 9, 'Weapon': 'Staff'}, {'Strength': 16, 'Agility': 8, 'Stamina': 3, 'Personality': 10, 'Intelligence': 7, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Strength': 13, 'Agility': 5, 'Stamina': 4, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.61, 'Armor': 9, 'Weapon': 'Staff'}, {'Strength': 15, 'Agility': 9, 'Stamina': 5, 'Personality': 18, 'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Axe'}, {'Strength': 11, 'Agility': 7, 'Stamina': 9, 'Personality': 9, 'Intelligence': 10, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Axe'}, {'Strength': 17, 'Agility': 7, 'Stamina': 8, 'Personality': 12, 'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Axe'}, {'Strength': 12, 'Agility': 8, 'Stamina': 7, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Axe'}]

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

# Do NOT include a main script in your submission
