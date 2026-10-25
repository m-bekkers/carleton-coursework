# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Matthé Bekkers, James Houghton, Alyssa Eaton, Lelosa Lucky-Ekeka"

# Update "" with your team (e.g. T102)
__team__ = "T091"


#==========================================#
# Place your character_occupation_list function after this line

def character_occupation_list(file_name: str, Occupation: str) -> list[dict]:
    """
    Returns all the lines with the same Occupation requested by the input
    Precondition: all feilds must be present


    >>> character_occupation_list("characters-mat.csv", "AT")
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 
    'Staff'}, ... {next element}

        >>> character_occupation_list("characters-mat.csv", "DB")
    [{'Strength': 17, 'Agility': 5, 'Stamina': 10, 
    'Personality': 11, 'Intelligence': 11, 'Luck': 0.67, 'Armor': 9, 'Weapon': 
    'Club'}, ...{next element}

        >>> character_occupation_list("characters-mat.csv", "WA")
    [{'Strength': 14, 'Agility': 6, 'Stamina': 2, 
    'Personality': 8, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 9, 'Weapon': 
    'Short sword'}, ... {next element}

    """

    characters = []
    file = open(file_name, 'r')

    for line in file:
        occupation_requested = line.strip().split(',')
        if occupation_requested[0] == Occupation:
            character = {
                "Strength": int(occupation_requested[1]),
                "Agility": int(occupation_requested[2]),
                "Stamina": int(occupation_requested[3]),
                "Personality": int(occupation_requested[4]),
                "Intelligence": int(occupation_requested[5]),
                "Luck": float(occupation_requested[6]),
                "Armor": int(occupation_requested[7]),
                "Weapon": occupation_requested[8]
            }
            characters.append(character)

    file.close()

    return characters

#==========================================#
# Place your character_strength_list function after this line

file_name = 'characters-mat.csv'

def character_strength_list(file_name: str, strength_range: tuple) -> list[dict]:
    """Returns  a list of characters using the specified file_name and strength_range.
    Preconditions: file_name != "", strength_range != ().
    >>>character_strength_list ('characters-mat.csv', (8, 11))
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, ... , {next element}
    >>> character_strength_list ('characters-mat.csv', (1000, 10001))
    []
    """
    strength_list = []
    min_strength, max_strength = strength_range

    in_file = open(file_name, 'r')
    labels = True
    for line in in_file:
        line = line.strip().split(',')
        line = [str(val) for val in line]
        for i in range(len(line)):
            try:
                line[i] = int(line[i])
            except ValueError:
                try:
                    line[i] = float(line[i])
                except ValueError:
                    pass
        if labels:
            labels = False
            headers = line
            continue
        strength = float(line[headers.index("Strength")])
        if min_strength <= strength <= max_strength:
            strength_list_data = {headers[i]: line[i]
                                  for i in range(len(headers))}
            del strength_list_data["Strength"]
            strength_list.append(strength_list_data)
    in_file.close()
    return strength_list

#==========================================#
# Place your character_luck_list function after this line


file_name = 'characters-mat.csv'


def character_luck_list(file_name: str, luck: float) -> list[dict]:
    """Return the list of characters from the file whose luck is less than the input luck value.

    Preconditions: file must have all elements present.

    >>> character_luck_list('characters-mat.csv', 0.4)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'}, {another element}, 

    >>> character_luck_list('characters-mat.csv', 0.35)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 8, 'Agility': 10, 'Stamina': 11, 'Personality': 16, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Dagger'}, {another element},

    >>> character_luck_list('characters-mat.csv', 0.1)
    []
    """

    file = open(file_name, 'r')
    first_line = True
    characters = []
    for line in file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            character_luck = {}
            if luck > float(line[6]):
                character_luck[table_header[0]] = str(line[0])
                character_luck[table_header[1]] = int(line[1])
                character_luck[table_header[2]] = int(line[2])
                character_luck[table_header[3]] = int(line[3])
                character_luck[table_header[4]] = int(line[4])
                character_luck[table_header[5]] = int(line[5])
                character_luck[table_header[7]] = int(line[7])
                character_luck[table_header[8]] = str(line[8])
                characters.append(character_luck)
    file.close()
    return characters

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file_name: str, weapon: str) -> list[dict]:
    """Returns a list of dictionaries containing the attributes of all characters whose weapon is the provided one.
    Preconditions: All fields are present.
    >>> character_weapon_list("characters-mat.csv", "staff")
    [{'occupation': 'at', 'strength': 13, 'agility': 2, 'stamina': 6, 'personality': 7, 'intelligence': 8, 'luck': 0.67}, ... {next element}]
    >>> character_weapon_list("characters-mat.csv", "club")
    [{'occupation': 'at', 'strength': 14, 'agility': 2, 'stamina': 8, 'personality': 11, 'intelligence': 5, 'luck': 0.78}, ... {next element}]
    >>> character_weapon_list("characters-mat.csv", "dagger")
    [{'occupation': 'at', 'strength': 7, 'agility': 5, 'stamina': 9, 'personality': 12, 'intelligence': 14, 'luck': 0.78}, ... {next element}]
    """
    file = open(file_name, "r")
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
                    table_header[0]: line[0],
                    table_header[1]: int(line[1]),
                    table_header[2]: int(line[2]),
                    table_header[3]: int(line[3]),
                    table_header[4]: int(line[4]),
                    table_header[5]: int(line[5]),
                    table_header[6]: float(line[6]),
                    table_header[7]: int(line[7])
                }
                character_list.append(character_weapons)

    file.close()
    return character_list

#==========================================#

# Place your load_data function after this line


def load_data(file_name: str, filter: tuple) -> list[dict]:
    """Returns a list of dictionaries containing the requested info from the provided filepath.
    No preconditions.
    >>> load_data("characters-mat.csv", ("Occupation", "AT"))
      [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
      'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
      {next element}, ... {final element}]
    >>> load_data("characters-mat.csv", ("Weapon", "Mace"))
      [{'Occupation': 'VF', 'Strength': 9, 'Agility': 12, 'Stamina': 10,
      'Personality': 12, 'Intelligence': 5, 'Luck': 0.83, 'Armor': 11},
      {next element}, ... {final element}]
    >>> load_data("characters-mat.csv", ("Strength", (11, 13)))
      [{'Occupation': 'AT', 'Agility': 2, 'Stamina': 6, 'Personality': 7,
      'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
      {next element}, ... {final element}]
    """

    # Checks the provided filter type
    # Occupations
    if filter[0] == "Occupation":
        occupation = filter[1]
        # Returns requested list
        result = character_occupation_list(
            file_name, occupation)
        return result
    
    # Strength
    elif filter[0] == "Strength":
        strength = filter[1]
        # Returns requested list
        result = character_strength_list(
            file_name, (strength))
        return result

    # Luck
    elif filter[0] == "Luck":
        luck = filter[1]
        # Returns requested list
        result = character_luck_list(file_name, luck)
        return result

    # Weapon
    elif filter[0] == "Weapon":
        weapon = filter[1]
        # Returns requested list
        result = character_weapon_list(file_name, weapon)
        return result
    
    # Case where invaild filter is provided
    elif filter[0] not in ("Weapon", "Occupation", "Strength", "Luck", "All"):
        print("Invalid Value")
        return []
    
    # Case where "All" is provided
    elif filter[0] == "All":
        # Goes through file to re-add all attributes since no previous function covers everything
        file = open(file_name, "r")
        char_list = []
        first_line = True
        for line in file:
            line = line.strip().split(",")
            if first_line:
                first_line = False
                table_header = line
            else:
                character_attr = {
                    table_header[0]: line[0],
                    table_header[1]: int(line[1]),
                    table_header[2]: int(line[2]),
                    table_header[3]: int(line[3]),
                    table_header[4]: int(line[4]),
                    table_header[5]: int(line[5]),
                    table_header[6]: float(line[6]),
                    table_header[7]: int(line[7]),
                    table_header[8]: line[8]
                }
                char_list.append(character_attr)
        file.close()
        return char_list
    
    # "Catch-All" case
    else:
        return []


#==========================================#
# Place your calculate_health function after this line

def calculate_health(characters: list[dict]) -> list[dict]:
    """Returns the provided list of dictionaires with a new entry: health. Health is calculated with the following formula:
    health = strength + agility + stamina + personality + intelligence + armor^2 * luck
    Precondition: provided list may not be empty.
    >>> calculate_health(load_data("characters-mat.csv", ("Occupation", "AT")))
      [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
      'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff', 'Health': 78.88},
      {next element}, ... {final element}]
    >>> calculate_health(load_data("characters-mat.csv", ("Weapon", "Mace")))
      [{'Occupation': 'VF', 'Strength': 9, 'Agility': 12, 'Stamina': 10,
      'Personality': 12, 'Intelligence': 5, 'Luck': 0.83, 'Armor': 11, 'Health': 148.43},
      {next element}, ... {final element}]
    >>> calculate_health(load_data("characters-mat.csv", ("Strength", (11, 13))))
      [{'Occupation': 'AT', 'Agility': 2, 'Stamina': 6, 'Personality': 7,
      'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff', 'Health': 65.88},
      {next element}, ... {final element}]
    """
    for character in characters:
        health = round((character["Strength"]
              + character.get("Agility")
              + character.get("Stamina")
              + character.get("Personality")
              + character.get("Intelligence")) + (character.get("Armor") ** 2) * character.get("Luck"), 2)

        character.update({'Health': health})
    return characters

print(calculate_health(load_data("characters-test.csv", ("Strength", (11, 13)))))

# Do NOT include a main script in your submission
