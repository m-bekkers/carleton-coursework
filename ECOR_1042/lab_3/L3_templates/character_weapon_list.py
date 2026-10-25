# ECOR 1042 Lab 3 - Individual submission for character_weapon_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Matthé Bekkers"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297066"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-091"

#==========================================#
# Place your character_weapon_list function after this line

def character_weapon_list(filename: str, weapon: str) -> list[dict]:
    """Returns a list of dictionaries containing the attributes of all characters whose weapon is the provided one.
    Preconditions: All fields are present.
    >>> character_weapon_list("characters-mat.csv", "staff")
    [{'occupation': 'at', 'strength': 13, 'agility': 2, 'stamina': 6, 'personality': 7, 'intelligence': 8, 'luck': 0.67}, ... {next element}]
    >>> character_weapon_list("characters-mat.csv", "club")
    [{'occupation': 'at', 'strength': 14, 'agility': 2, 'stamina': 8, 'personality': 11, 'intelligence': 5, 'luck': 0.78}, ... {next element}]
    >>> character_weapon_list("characters-mat.csv", "dagger")
    [{'occupation': 'at', 'strength': 7, 'agility': 5, 'stamina': 9, 'personality': 12, 'intelligence': 14, 'luck': 0.78}, ... {next element}]
    """
    file = open(filename, "r")
    first_line = True
    character_list = []
    for line in file:
        line = line.strip("\n").split(",")
        if first_line:
            first_line = False
            table_header = line
        else:
            if line[8] == weapon:
                character_weapons = {
                    table_header[0] : line[0],
                    table_header[1] : int(line[1]),
                    table_header[2] : int(line[2]),
                    table_header[3] : int(line[3]),
                    table_header[4] : int(line[4]),
                    table_header[5] : int(line[5]),
                    table_header[6] : float(line[6]),
                    table_header[7] : int(line[7])
                }
                character_list.append(character_weapons)

    file.close() 
    return character_list

# Do NOT include a main script in your submission
