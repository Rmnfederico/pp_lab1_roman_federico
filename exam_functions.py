import copy
import re
import os
from files_handling_functions import *

########## Validations / Get Inputs ##########

def clear_console() -> None:
    """
    waits for the user to press any key 
    to clear the console and continue program execution.
    """
    _ = input('\nPress a key to continue...')
    os.system('cls')

def check_int_string(string: str) -> bool:
    """
    The function checks if a given string can be converted to an integer.
    
    :param string: The input parameter to the function `check_int_string()`. It is expected to be a
    string or an integer. If it is a string, the function checks if it can be converted to an integer.
    If it is already an integer, the function returns `True` with a warning message. If
    :type string: str
    :return: a boolean value. It returns True if the input string can be converted to an integer, and
    False otherwise.
    """
    try:
        #iterable objects that can be traversed with "for in" and could contain ints
        if isinstance(string, (list, tuple)):
            return False
        
        for letter in string:
            if not isinstance(int(letter), int):
                return False
        return True
    except TypeError as e1:
        if isinstance(string, int):
            print(f"{e1}: WARNING! param. is already an int")
            return True
        else:
            print(f"TypeError: {e1}: string can't be converted to int.")
            return False
    except ValueError as e2:
            print(f"ValueError: {e2}: string can't be converted to int.")
            return False

def check_float_string(string: str) -> bool:
    """
    The function checks if a given string can be converted to a float. 
    returns True if it can, and False otherwise.
    
    :param string: A string that may or may not represent a float number
    :type string: str
    :return: a boolean value indicating whether the input string can be converted to a float or not. If
    the input string is already a float or int type, a warning message is printed but the function still
    returns True. If there is a TypeError, ValueError, or AttributeError during the conversion process,
    an error message is printed and the function returns False.
    """
    try:
        if isinstance(string, (float, int)):
            print("WARNING! param. is already a float or int type")
        float(string)
        return True
    except TypeError as e1:
        print(f'TypeError: {e1}')
        return False
    except ValueError as e2:
        print(f'ValueError: {e2}')
        return False
    except AttributeError as e3:
        print(f'AttributeError: {e3}')
        return False

def get_int(input_msg: str, retries: int = 0) -> int:
    """
    This function prompts the user to input an integer and allows
    for a specified number of retries if the input is invalid.
    
    :param input_msg: A string message that will be displayed to the user when asking for input
    :type input_msg: str
    :param retries: The `retries` parameter is an optional integer parameter that specifies the number
    of times the user can retry entering a valid input before the function returns `None`. If `retries`
    is not specified, it defaults to 0, defaults to 0
    :type retries: int (optional)
    :return: an integer value if a valid integer input is provided by the user, and it is returning None
    if no valid input is provided within the specified number of retries.
    """
    retries += 1
    while retries > 0:
        string = input(input_msg)
        if check_int_string(string):
            return int(string)
        else:
            retries -= 1
            print(f"ERROR: {string} is not a valid input. {retries} retries left.")
    print("no retries left.")
    return None

def get_float(input_msg: str, retries: int = 0) -> float:
    """
    The function takes an input message and optional number of retries, prompts the user to
    input a float value, and returns the float value or None if the input is not a valid float after the
    specified number of retries.
    
    :param input_msg: A string message that will be displayed to the user when asking for input
    :type input_msg: str
    :param retries: An integer that specifies the number of times the user
    can retry entering a valid float value before the function returns `None`. It has a default value of
    0, which means that if the user enters an invalid float value, the function will not allow any
    retries and, defaults to 0
    :type retries: int (optional)
    :return: a float value if the input string can be converted to a float, and None if all retries have
    been exhausted and the input string cannot be converted to a float.
    """
    retries += 1
    while retries > 0:
        string = input(input_msg)
        if check_float_string(string):
            return float(string)
        else:
            retries -= 1
            print(f"ERROR: {string} is not a float. {retries} retries left.")
    print("no retries left.")
    return None

def validate_range(number: int, min, max) -> bool:
    """
    The function validates if a given number is within a specified range.
    
    :param number: an integer that needs to be validated within a certain range
    :type number: int
    :param min: The minimum value that the "number" parameter can take
    :param max: The parameter "max" is the maximum value that the "number" parameter can take. It is
    used in the function "validate_range" to check if the "number" parameter is within the specified
    range (between "min" and "max")
    :return: a boolean value (True or False) depending on whether the input number is within the
    specified range (between min and max, inclusive) and is an integer.
    """
    if not isinstance(number, int) or number < min or number > max:
        return False
    else:
        return True
    
def get_string(input_msg: str,retries: int = 0) -> str:
    """
    Takes an input message and number of retries as arguments, prompts the
    user to input a non-empty string, and returns the string or None if all retries are exhausted.
    
    :param input_msg: A string that will be displayed as a prompt to the user when asking for input
    :type input_msg: str
    :param retries: The parameter "retries" is an integer that specifies the number of times the user
    can retry entering a non-empty string if they initially enter an empty string, defaults to 0
    :type retries: int (optional)
    :return: a string value. If the user enters a non-empty string, the function returns that string. If
    the user enters an empty string, the function prompts the user to enter a non-empty string again, up
    to the number of retries specified. If the user still enters an empty string after all retries, the
    function returns None.
    """
    retries += 1
    while retries > 0:
        string = input(input_msg)
        if(len(string) > 0):
            return string
        else:
            retries -= 1
            print(f"ERROR: string can't be empty. {retries} retries left.")
    print("no retries left.")
    return None

def get_name_data(dictionary: dict, search_key: str) -> str:
    """
    The function takes a dictionary and a search key as input and returns a formatted string containing
    the name and value of the search key if it exists in the dictionary.
    
    :param dictionary: A dictionary containing information about a person, including their name and
    other attributes
    :type dictionary: dict
    :param search_key: The parameter search_key is a string that represents the key that we want to
    search for in the dictionary. It is used to retrieve the value associated with that key in the
    dictionary
    :type search_key: str
    :return: a formatted string that includes the name from the dictionary and the value associated with
    the search_key parameter. The name is left-justified and padded with spaces to a length of 15
    characters, and the search_key is capitalized. If the search_key is not found in the dictionary, a
    KeyError is raised.
    """
    try:
        if search_key in dictionary and isinstance(dictionary, dict):
            return f'Name: {str(dictionary["nombre"]).ljust(15)}' + "\t|\t".center(5) + f'{search_key.capitalize()}:{dictionary[search_key]}'
    except KeyError as err:
        print(f"KeyError: {err} not in dict.")

def get_formatted_key_value(dictionary: dict, search_key: str) -> str:
    """
    This function takes a dictionary and a search key, and returns a formatted string with the
    capitalized search key and its corresponding value, with underscores replaced by spaces.
    
    :param dictionary: A dictionary object that contains key-value pairs
    :type dictionary: dict
    :param search_key: The key that we want to search for in the dictionary
    :type search_key: str
    :return: a formatted string that contains the capitalized search key and its corresponding value
    from the input dictionary, with underscores replaced by spaces. If the input dictionary is empty,
    not a dictionary, or the search key is not found in the dictionary, the function returns None.
    """
    if not dictionary or not isinstance(dictionary, dict) or search_key not in dictionary:
        return None
    else:
        return f'{search_key.capitalize()}: {dictionary.get(search_key, "N/A")}'.replace("_", " ")

########## Sorting Functions ##########

def quicksort_for_dicts(origin_dict_list:list, comp_key, asc: bool = True) -> list:
    """
    This function performs quicksort algo on a list of dictionaries sorting order based on a specified key.
    
    :param origin_dict_list: a list of dictionaries that need to be sorted
    :type origin_dict_list: list
    :param comp_key: The key in the dictionary that will be used for comparison during the sorting
    process
    :param asc: A boolean parameter that determines whether the sorting should be in ascending order
    (True) or descending order (False), defaults to True
    :type asc: bool (optional)
    :return: a sorted list of dictionaries based on the value of a specified key in each dictionary. The
    sorting order (ascending or descending) is determined by the `asc` parameter.
    """
    if len(origin_dict_list) <= 1:
        return origin_dict_list
    else:
        dict_list = origin_dict_list.copy()
        pivot = dict_list[0]
        if asc:
            lesser = [x for x in dict_list[1:] if x[comp_key] <= pivot[comp_key]]
            greater = [x for x in dict_list[1:] if x[comp_key] > pivot[comp_key]]
        else:
            lesser = [x for x in dict_list[1:] if x[comp_key] >= pivot[comp_key]]
            greater = [x for x in dict_list[1:] if x[comp_key] < pivot[comp_key]]
        return quicksort_for_dicts(lesser, comp_key, asc) + [pivot] + quicksort_for_dicts(greater, comp_key, asc)

def quicksort_for_dicts_double_key(origin_dict_list:list, comp_key: str, sub_comp_key:str, asc: bool = True) -> list:
    """
    This is a Python function that performs a quicksort algorithm on a list of dictionaries based on a
    double key comparison.
    
    :param origin_dict_list: a list of dictionaries that need to be sorted
    :type origin_dict_list: list
    :param comp_key: The key in the dictionary that will be used as the primary basis for comparison
    during sorting
    :type comp_key: str
    :param sub_comp_key: The sub_comp_key parameter is a string that represents the secondary key to be
    used for sorting the list of dictionaries. It is used in conjunction with the comp_key parameter to
    sort the list of dictionaries based on two keys
    :type sub_comp_key: str
    :param asc: A boolean parameter that determines whether the sorting should be in ascending order
    (True) or descending order (False), defaults to True
    :type asc: bool (optional)
    :return: a sorted list of dictionaries based on two keys: `comp_key` and `sub_comp_key`. The sorting
    order is determined by the `asc` parameter, which is set to `True` by default.
    """
    if len(origin_dict_list) <= 1:
        return origin_dict_list
    else:
        dict_list = origin_dict_list.copy()
        pivot = dict_list[0]
        if asc:
            lesser = [x for x in dict_list[1:] if x[comp_key][sub_comp_key] <= pivot[comp_key][sub_comp_key]]
            greater = [x for x in dict_list[1:] if x[comp_key][sub_comp_key] > pivot[comp_key][sub_comp_key]]
        else:
            lesser = [x for x in dict_list[1:] if x[comp_key][sub_comp_key] >= pivot[comp_key][sub_comp_key]]
            greater = [x for x in dict_list[1:] if x[comp_key][sub_comp_key] < pivot[comp_key][sub_comp_key]]
        return quicksort_for_dicts_double_key(lesser, comp_key, sub_comp_key, asc) + [pivot] + quicksort_for_dicts_double_key(greater, comp_key, sub_comp_key, asc)


########## Calculate Functions ##########

def calculate_max_min_data_dicts(dict_list: list[dict], search_key: str, search_sub_key: str, pick_max: bool = True) -> list:
    """
    This function takes a list of dictionaries, a search key, and a search sub-key, and returns a list
    of dictionaries that have the maximum or minimum value for the specified sub-key.
    
    :param dict_list: A list of dictionaries that contain data to be searched and compared
    :type dict_list: list[dict]
    :param search_key: The key in the dictionary that we want to search for a maximum or minimum value
    in
    :type search_key: str
    :param search_sub_key: The sub-key within the dictionary's value that we want to search for the
    maximum or minimum value
    :type search_sub_key: str
    :param pick_max: A boolean parameter that determines whether to pick the maximum or minimum value
    for the search sub-key. If pick_max is True, the function will return the dictionary(s) with the
    highest value for the search sub-key. If pick_max is False, the function will return the
    dictionary(s) with the lowest, defaults to True
    :type pick_max: bool (optional)
    :return: a list of dictionaries that have the maximum or minimum value for a given sub-key within a
    list of dictionaries. The number of dictionaries in the returned list depends on how many
    dictionaries have the same maximum or minimum value for the given sub-key.
    """
    if not dict_list:
        return []
    else:
        try:
            if isinstance(dict_list, list) and all(isinstance(d , dict) for d in dict_list):
                search_value = None
                search_list = []
                for dictionary in dict_list:
                    value = dictionary[search_key][search_sub_key]
                    if search_value is None or (value > search_value if pick_max else value < search_value):
                        search_value = value
                        search_list = [dictionary]
                    elif value == search_value:
                        search_list.append(dictionary)
                return search_list
        except KeyError as e1:
            print(f"KeyError: {e1} not in dict.")
        except ValueError as e2:
            print(f"ValueError: {e2} for '{search_key}' key ")

def sum_dicts_data(dict_list:list[dict], search_key:str, sub_search_key: str, double_key: bool = True) -> float:
    """
    This function takes a list of dictionaries, a search key, and a sub-search key, and returns the sum
    of all values associated with the search key and sub-search key in the dictionaries, with an option
    to double-check the sub-search key.
    
    :param dict_list: A list of dictionaries that contain data to be summed
    :type dict_list: list[dict]
    :param search_key: The key to search for in the dictionaries within the list
    :type search_key: str
    :param sub_search_key: The sub_search_key parameter is a string that represents the key to search
    for within a nested dictionary. It is used in conjunction with the search_key parameter to locate
    the value to be summed
    :type sub_search_key: str
    :param double_key: double_key is a boolean parameter that determines whether the function should
    look for a nested key in the dictionaries or not. If double_key is True, the function will look for
    a key (search_key) in the dictionaries and then look for a sub-key (sub_search_key) within the value
    of that, defaults to True
    :type double_key: bool (optional)
    :return: a float value which is the sum of all the values in the dictionaries that match the search
    key and sub-search key criteria. If the input is invalid or there is an error, the function returns
    None and prints an error message.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        try:
            sum = 0
            for dictionary in dict_list:
                if not dictionary:
                    return None
                elif double_key:
                    if search_key in dictionary and sub_search_key in dictionary[search_key] and isinstance(float(dictionary[search_key][sub_search_key]), float):
                        sum += dictionary[search_key][sub_search_key]
                else:
                    if search_key in dictionary and isinstance(float(dictionary[search_key]), float):
                        sum += dictionary[search_key]
            return sum 
        
        except ValueError as err:
            print(f"ValueError: {err} for '{search_key}' key")
        except ZeroDivisionError as err2:
            print(f"ZeroDivisionError: attempted {err2} as no '{search_key}' key was found.")
        except TypeError as err3:
            print(f"TypeError: {err3}")

def divide(dividend:int, divider:int) -> float:
    """
    The function takes two integer inputs and returns their quotient as a float, handling division by
    zero and catching any value or type errors.
    
    :param dividend: an integer representing the number being divided
    :type dividend: int
    :param divider: The parameter "divider" is an integer representing the number that will be used to
    divide the "dividend" parameter
    :type divider: int
    :return: a float value which is the result of dividing the dividend by the divider. If the divider
    is 0, the function returns 0. If there is a ValueError or TypeError exception raised during the
    division, the function prints the error message and returns 0.
    """
    if divider == 0:
        return 0
    else:
        try:
            return float(dividend)/float(divider)
        except ValueError as err:
            print(err)
            return 0
        except TypeError as err2:
            print(err2)
            return 0

def calculate_avg(dict_list: list[dict], search_key, sub_search_key, double_key: bool = True) -> float:
    """
    This function calculates the average of a specific value in a list of dictionaries based on a search
    key and a sub-search key.
    
    :param dict_list: a list of dictionaries that contain data to be averaged
    :type dict_list: list[dict]
    :param search_key: The key to search for in the dictionaries within the list
    :param sub_search_key: The sub_search_key parameter is a string that represents a key in the
    dictionaries within the dict_list parameter. This key is used to access a specific value within each
    dictionary that corresponds to the search_key parameter
    :param double_key: A boolean parameter that determines whether the function should look for a
    sub_search_key within the values of the search_key in the dictionaries. If double_key is True, the
    function will sum the values of the sub_search_key for each dictionary that has the search_key and
    then divide by the number of dictionaries that, defaults to True
    :type double_key: bool (optional)
    :return: a float value, which is the average of the values in the dictionaries in the input list
    that match the search key and sub-search key. If no matching dictionaries are found, the function
    returns None.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        counter = 0
        for dictionary in dict_list:
            if search_key in dictionary:
                counter += 1
        if counter == 0:
            return None
        else:
            if double_key:
                return divide(sum_dicts_data(dict_list, search_key, sub_search_key), counter)
            else:
                return divide(sum_dicts_data(dict_list, search_key, sub_search_key, False), counter)

########## Printing / Listing ##########

def list_name_stat(dict_list: list[dict], stat: str, header:str = None) -> None:
    """
    The function takes a list of dictionaries and a specific statistic, and prints out the name and
    value of that statistic for each dictionary in the list.
    
    :param dict_list: A list of dictionaries containing information about individuals, including their
    names and statistics
    :type dict_list: list[dict]
    :param stat: The parameter "stat" is a string that represents the name of the statistic that we want
    to retrieve from the dictionaries in the list
    :type stat: str
    :param header: The header parameter is an optional string that can be passed to the function to
    print a header before the list of names and their corresponding statistics. If no header is
    provided, the function will not print a header
    :type header: str
    :return: If the input is invalid (empty list or non-dict elements), the function returns None. If
    the input is valid but the specified stat is not present in all dictionaries, the function prints a
    message and returns None. Otherwise, the function prints the name and the value of the specified
    stat for each dictionary in the list. No value is returned explicitly.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        if header:
            print(f'\n{header}:\n')
        for dictionary in dict_list:
            if stat in dictionary["estadisticas"]:
                print(f'{get_formatted_key_value(dictionary, "nombre")}'+" | "+f'{get_formatted_key_value(dictionary["estadisticas"], stat)}')
            else:
                print("stat not present in all dictionaries.")
                return None
#1.
def list_names_data(dict_list: list[dict], search_key: str) -> None:
    """
    This function takes a list of dictionaries and a search key, and prints the name data of the
    dictionary that contains the search key.
    
    :param dict_list: A list of dictionaries containing information about players
    :type dict_list: list[dict]
    :param search_key: The search_key parameter is a string that is used to search for a specific key in
    the dictionaries within the dict_list parameter. The function will print out the values associated
    with the search_key in each dictionary that contains it
    :type search_key: str
    :return: The function does not return anything, it only prints the output to the console.
    """
    if not dict_list or not isinstance(dict_list, list):
        print("empty list/ not all elements in list are dicts.")
        return None
    else:
        print(f'*** PLAYERS LIST ***'.center(60))
        for index, dictionary in enumerate(dict_list):
            if search_key in dictionary:
                print(f'{index+1}-{get_name_data(dictionary, search_key)}')

#2.
def list_index_kv_pair(dict_list: list[dict], search_key) -> None:
    """
    The function takes a list of dictionaries and a search key, and prints the index and formatted
    key-value pair of each dictionary in the list that contains the search key.
    
    :param dict_list: A list of dictionaries containing key-value pairs
    :type dict_list: list[dict]
    :param search_key: The parameter "search_key" is a variable that represents the key that we want to
    search for in the dictionaries within the list "dict_list". It is used to retrieve the value
    associated with that key in each dictionary
    :return: The function is not returning anything, it is printing the formatted key-value pairs of the
    search_key in each dictionary of the dict_list.
    """
    if not dict_list or not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        for index, player in enumerate(dict_list):
            print(f'{index+1}-{get_formatted_key_value(player, search_key)}')

def print_column_key_values(statistics: dict, name: str) -> None:
    """
    This function takes in a dictionary of statistics and a name, and prints out the key-value pairs of
    the dictionary with the keys capitalized and underscores replaced with spaces.
    
    :param statistics: A dictionary containing statistical data
    :type statistics: dict
    :param name: The name of the entity for which the statistics are being displayed
    :type name: str
    :return: If the input `statistics` is empty or not a dictionary, the function returns `None`.
    Otherwise, the function does not return anything (`None` is implicitly returned).
    """
    if not statistics or not isinstance(statistics, dict):
        return None
    else:
        print(f'\nShowing statistics for {name}:\n')
        for key, value in statistics.items():
            print(f'{key.capitalize().replace("_", " ")}: {value}')

def get_player_statistics(dict_list: list[dict]) -> dict:
    """
    This function takes a list of dictionaries containing player statistics, prompts the user to select
    a player by index, and returns the selected player's dictionary.
    
    :param dict_list: A list of dictionaries containing player statistics. Each dictionary represents a
    player and contains keys such as "nombre" (name), "edad" (age), "posicion" (position), "goles"
    (goals), etc
    :type dict_list: list[dict]
    :return: a dictionary containing the statistics of a selected player from a list of dictionaries. If
    the input list is empty or contains non-dictionary elements, an empty dictionary is returned. If the
    selected player index is out of range, a message is printed and an empty dictionary is returned.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return {}
    else:
        list_index_kv_pair(dict_list, "nombre")
        player_index = get_int("Enter the index of the player to show:")
        if validate_range((player_index-1), 0, (len(dict_list)-1)):
            selected_player = dict_list[player_index-1]
            return selected_player
        else: 
            print("index not found in list.")
            return {}

#3. Save name, position & player statistics
def extract_statistics_dict(dictionary: dict) -> dict:
    """
    The function extracts statistics from a dictionary and returns a new dictionary with the player's
    name, position, and all the statistics.
    
    :param dictionary: A dictionary containing information about a player's name, position, and
    statistics
    :type dictionary: dict
    :return: The function `extract_statistics_dict` returns a dictionary containing the player's name,
    position, and statistics if the input `dictionary` is not empty and is a dictionary. If the input is
    empty or not a dictionary, an empty dictionary is returned.
    """
    if dictionary and isinstance(dictionary, dict):
        player_statistics_dict = dict()
        player_statistics_dict["nombre"] = dictionary.get("nombre")
        player_statistics_dict["posicion"] = dictionary.get("posicion")
        for key, value in dictionary["estadisticas"].items():
            player_statistics_dict[key] = value
        return player_statistics_dict
    else:
        return {}

def save_player_statistics_as_csv(dictionary: dict) -> bool:
    """
    This function prompts the user to save a player's statistics as a CSV file and returns a boolean
    indicating whether the file was successfully saved.
    
    :param dictionary: A dictionary containing player statistics, with keys such as 'nombre' (name),
    'edad' (age), 'goles' (goals), etc
    :type dictionary: dict
    :return: a boolean value. It returns True if the player's statistics are successfully saved as a CSV
    file, and False if they are not saved.
    """
    option = get_string(f"\nDo you want to save {dictionary['nombre']}'s statistics as csv? (y/n) ")
    if re.match(r"^[y]$", option, re.I):
        player_statistics_dict = extract_statistics_dict(dictionary)
        if save_dict_as_csv(f'{player_statistics_dict.get("nombre")}.csv'.replace(" ", "_"), player_statistics_dict):
            return True
    
    else:
        print("player's statistics not saved.")
        return False
    
#4. let user select a player by name, then list achievements for that player/s
def find_name_by_string_comp(dict_list: list[dict]) -> list:
    """
    This function takes a list of dictionaries containing player information and returns a filtered list
    of players whose names match a given search string.
    
    :param dict_list: A list of dictionaries, where each dictionary represents a player and contains
    information about the player such as their name, age, and team
    :type dict_list: list[dict]
    :return: The function `find_name_by_string_comp` returns a list of dictionaries that match the
    search parameter entered by the user. If no matches are found, an empty list is returned.
    """
    if not dict_list:
        return []
    else: 
        search_name = get_string("enter the name of the player:")
        if search_name:
            filtered_list = list()
            for player in dict_list:
                search = re.search(search_name.replace(" ", ""), player["nombre"], re.I) 
                if search:
                    start, end = search.span()
                    if end-start >= 4:
                        filtered_list.append(player)
    if filtered_list:
        print(f'{len(filtered_list)} player/s matched search parameter:\n')
        list_index_kv_pair(filtered_list, "nombre")
        return filtered_list
    else:
        print(f"no matches found for '{search_name}' in the list.")
        return []

def show_player_achievements_by_name(dict_list: list[dict]) -> None:
    """
    This function takes a list of dictionaries containing player information and allows the user to
    search for a player by name and display their achievements.
    
    :param dict_list: The parameter dict_list is a list of dictionaries, where each dictionary
    represents a player and their achievements. The dictionaries have two keys: "nombre" (name of the
    player) and "logros" (list of achievements)
    :type dict_list: list[dict]
    :return: None in some cases, and printing the achievements of the selected player or players in
    other cases.
    """
    if not dict_list or not all((d, dict) for d in dict_list):
        return None
    else:
        filtered_list = find_name_by_string_comp(dict_list)
        if not filtered_list:
            return None
        elif len(filtered_list) == 1:
            for achievement in filtered_list[0]["logros"]:
                print(f'* {achievement}') 
        else:
            sub_option = get_int("\nselect index from found players or 0 to print all:")
            if sub_option == 0:
                for player in filtered_list:
                    print(f'\nAchievements for {player["nombre"]}:\n')
                    for achievement in player["logros"]:
                        print(f'* {achievement}') 
            elif validate_range(sub_option, 1, len(filtered_list)):
                print(f'\nAchievements for {filtered_list[sub_option-1].get("nombre")}:\n')
                for achievement in filtered_list[sub_option-1]["logros"]:
                    print(f'* {achievement}') 
            else:
                print(f"index {sub_option} not found.")
                return None

#5. calc. & show avg. points per game (per dream team player) sorted by name (asc)
def calc_avg_points_list_players(dict_list: list[dict]) -> list:
    """
    This function takes a list of dictionaries containing player statistics, sorts them by name,
    calculates the average points per game for the team, and returns the sorted list.
    
    :param dict_list: A list of dictionaries, where each dictionary represents a player and their
    statistics
    :type dict_list: list[dict]
    :return: a sorted list of dictionaries with the average points per game for the whole team printed
    to the console.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        print("empty list/ not all elements in list are dicts.")
        return []
    else:
        sorted_list = quicksort_for_dicts(dict_list, "nombre", True)
        points_avg = calculate_avg(sorted_list, "estadisticas", "promedio_puntos_por_partido")
        print(f'\nThe average points per game for the whole team is {points_avg}\n')
        return sorted_list

#6. let user select a player by name and show if he belongs to hall of fame
def filter_values_from_dict_list(dict_list: list[dict], search_key, filter_string: str) -> list:
    """
    The function filters a list of dictionaries based on a search key and a filter string.
    
    :param dict_list: A list of dictionaries that will be searched for values matching the filter_string
    :type dict_list: list[dict]
    :param search_key: The key in the dictionaries of the input list that will be searched for the
    filter string
    :param filter_string: The string that will be used to filter the values in the dictionary list. It
    will be matched against the end of each value in the search_key
    :type filter_string: str
    :return: a list of dictionaries from the input `dict_list` where the value of the `search_key`
    matches the `filter_string` pattern.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        pattern = fr'({filter_string})$'
        return [d for d in dict_list if any(re.search(pattern, item, re.I) for item in d.get(search_key, []))]

def show_player_hall_of_fame(dict_list: list[dict]) -> None:
    """
    The function takes a list of dictionaries, filters it based on a specific string, and prints the
    names of players who belong to a hall of fame.
    
    :param dict_list: A list of dictionaries containing information about basketball players
    :type dict_list: list[dict]
    :return: The function does not return anything, it only prints output to the console.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        print("empty list/ not all elements in list are dicts.")
        return None
    else:
        filtered_list = find_name_by_string_comp(dict_list)
        if not filtered_list:
            return None
        else:
            hall_of_fame_list = filter_values_from_dict_list(filtered_list, "logros", "salon de la fama del baloncesto")
            if hall_of_fame_list:
                print("\nShowing players from the list that belong to hall of fame:\n")
                for player in hall_of_fame_list:
                    print(f'{player["nombre"]} belongs to hall of fame.')
            else:
                print("\nplayer/s do not belong to the hall of fame.\n")

#7. calculate and print player w/ the highest total rebounds count
def get_highest_stat_player(dict_list: list[dict], search_key: str, search_sub_key: str) -> list:
    """
    This function takes a list of dictionaries and returns a list of players with the highest value for
    a specified key and sub-key.
    
    :param dict_list: A list of dictionaries containing player data, where each dictionary represents a
    player and their stats
    :type dict_list: list[dict]
    :param search_key: The key in the dictionary that we want to search for the highest value of
    :type search_key: str
    :param search_sub_key: The search_sub_key parameter is a string that represents the sub-key within
    the dictionary that contains the value to be compared when searching for the highest stat player
    :type search_sub_key: str
    :return: a list of dictionaries containing the player(s) with the highest value for a given search
    key and sub-key within a list of dictionaries. If the input list is empty or not a list of
    dictionaries, an empty list is returned. If there are no players with the given search key and
    sub-key, an empty list is also returned.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return []
    else:
        max_stat_players = calculate_max_min_data_dicts(dict_list, search_key, search_sub_key, True)
        if not max_stat_players:
            return []
        else:
            return max_stat_players

def filter_greater_or_lesser(dict_list: list[dict], search_key, search_sub_key, greater: bool = True) -> list:
    """
    This function filters a list of dictionaries based on whether a specified sub-key's value is greater
    or lesser than a given value.
    
    :param dict_list: a list of dictionaries
    :type dict_list: list[dict]
    :param search_key: The key in the dictionary that contains the sub-key to search for
    :param search_sub_key: The sub-key to search for within the dictionary's value associated with the
    search_key
    :param greater: A boolean parameter that determines whether the function should filter for values
    greater than or less than the input value. If greater is True, the function will filter for values
    greater than the input value. If greater is False, the function will filter for values less than the
    input value, defaults to True
    :type greater: bool (optional)
    :return: a list of dictionaries that have a value for the specified search_key and search_sub_key
    that is either greater or lesser than the input value, depending on the value of the greater
    parameter.
    """
    if not dict_list:
        return []
    else:
        value = get_float("Enter a points per game value (can be float):")
        lesser_list = list()
        greater_list = list()
        for dictionary in dict_list:
            if search_key in dictionary and search_sub_key in dictionary[search_key]:
                if dictionary[search_key][search_sub_key] < value:
                    lesser_list.append(dictionary)
                else:
                    greater_list.append(dictionary)
        
        if not lesser_list and not greater_list:
            print("search key / search sub key not found in any dict.")
            return []
        else:
            if greater: #IMPLEMENT TERNARY OPERATOR?
                return greater_list
            else:
                return lesser_list

def get_higher_stats_per_game_list(dict_list: list[dict], search_key: str, sub_search_key: str) -> list:
    """
    This function returns a filtered list of dictionaries based on a search key and sub-search key,
    where the values of the sub-search key are greater than the search key.
    
    :param dict_list: A list of dictionaries containing data for each game, where each dictionary
    represents a game and its attributes
    :type dict_list: list[dict]
    :param search_key: The key in the dictionary to search for higher or lower values
    :type search_key: str
    :param sub_search_key: The sub_search_key is a string representing the key of a nested dictionary
    within each dictionary in the dict_list parameter. It is used to filter the list of dictionaries
    based on a specific value within the nested dictionary
    :type sub_search_key: str
    :return: The function `get_higher_stats_per_game_list` returns a list of dictionaries that have a
    value greater than or equal to the specified search value for the specified key and sub-key. If
    there are no matches found, an empty list is returned.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return []
    else:
        filtered_list = filter_greater_or_lesser(dict_list, search_key, sub_search_key, True)
        if not filtered_list:
            print("no matches found for the entered value.")
            return []
        else:
            return filtered_list
#16.
def show_points_per_game_avg_less_lower(dict_list: list[dict]) -> None:
    """
    The function takes a list of dictionaries containing statistics of players and prints the average
    points per game for all players except the one with the lowest score.
    
    :param dict_list: A list of dictionaries, where each dictionary represents statistics for a player
    in a game. The dictionaries should have the following keys: 'nombre' (player name),
    'promedio_puntos_por_partido' (average points per game), and any other statistics relevant to the
    game
    :type dict_list: list[dict]
    :return: The function does not return anything, it only prints the result.
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        sorted_list = quicksort_for_dicts([extract_statistics_dict(d) for d in dict_list], "promedio_puntos_por_partido", True)
        lowest_name, lowest_score = sorted_list[0]['nombre'], sorted_list[0]['promedio_puntos_por_partido']
        print(f"\nAvg w/o {lowest_name}'s score ({lowest_score}):\n{calculate_avg(sorted_list[1:], 'promedio_puntos_por_partido', '', False)}")

#17. 

def calc_max_data_dicts(dict_list: list[dict], search_key: str, comp_len: bool = False) -> list:
    """
    This function takes a list of dictionaries, a search key, and an optional boolean flag, and returns
    a list of dictionaries that have the maximum value for the specified search key.
    
    :param dict_list: A list of dictionaries that will be searched for the maximum value of a specified
    key
    :type dict_list: list[dict]
    :param search_key: The key in the dictionaries that the function will search for the maximum value
    :type search_key: str
    :param comp_len: A boolean parameter that determines whether to compare the length of the values in
    the dictionaries or their actual values. If set to True, the function will compare the length of the
    values instead of their actual values, defaults to False
    :type comp_len: bool (optional)
    :return: The function `calc_max_data_dicts` returns a list of dictionaries that have the maximum
    value for the specified `search_key` in the input `dict_list`. If `comp_len` is set to `True`, the
    function compares the length of the values for `search_key` instead of their actual values. If the
    input `dict_list` is empty or not all elements in the list are dictionaries
    """
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        print("empty list / not all elements in list are dicts.")
        return []
    else:
        if not all(search_key in d for d in dict_list):
            print(f"search key '{search_key}' not present in all dicts.")
            return []
        else:
            max_value = dict_list[0][search_key]
            max_list = []
            for dictionary in dict_list:
                if comp_len:
                    if len(dictionary[search_key]) > len(max_value):
                        max_value = dictionary[search_key]
                        max_list = [dictionary]
                    elif len(dictionary[search_key]) == len(max_value):
                        max_list.append(dictionary)
                else:
                    if dictionary[search_key] > max_value:
                        max_value = dictionary[search_key]
                        max_list = [dictionary]
                    elif dictionary[search_key] == max_value:
                        max_list.append(dictionary)
                   
            return max_list

def show_highest_achievements_player(dict_list: list[dict]) -> None:
    """
    This function takes a list of dictionaries containing player information and displays the player(s)
    with the highest number of achievements along with their achievements.
    
    :param dict_list: A list of dictionaries, where each dictionary represents a player and their
    achievements
    :type dict_list: list[dict]
    :return: The function is not returning anything, it is printing the highest number of achievements
    players and their achievements.
    """
    if not dict_list:
        return None
    else:
        max_achievements_list = calc_max_data_dicts(dict_list, "logros", True)
        print(f"\nHighest number of achievements players:\n")
        for player in max_achievements_list:
            print("----------------------------")
            print(f"{get_formatted_key_value(player, 'nombre')}")
            print("----------------------------")
            for achievement in player["logros"]:
                print(f'* {achievement}')

#20. 
def list_by_position_higher_stats(dict_list: list[dict]) -> None:
    """
    This function sorts a list of dictionaries containing basketball player information by their
    position and prints their name, shooting percentage, and position in a formatted way.
    
    :param dict_list: A list of dictionaries representing basketball players and their statistics. Each
    dictionary contains keys "nombre" (name), "posicion" (position), and "estadisticas" (statistics),
    where "estadisticas" is itself a dictionary containing keys "porcentaje_tiros_de_campo"
    :type dict_list: list[dict]
    :return: The function does not return anything, it prints a formatted list of players with their
    name, shooting percentage, and position.
    """
    if not dict_list:
        return None
    else:
        positions_order = {"base": 1,"escolta": 2,"alero": 3,
                           "ala-pivot": 4,"pivot": 5}
        positions_list = list(dict_list)

        for player in positions_list:
            for key, value in positions_order.items():
                if str(player["posicion"]).lower() == key:
                    player["posicion"] = value
        
        positions_list = quicksort_for_dicts(positions_list, "posicion")

        for player in positions_list:
            for key, value in positions_order.items():
                if player["posicion"] == value:
                    player["posicion"] = key.capitalize()

        for player in positions_list:
            print(f'{get_formatted_key_value(player, "nombre")} | {get_formatted_key_value(player["estadisticas"], "porcentaje_tiros_de_campo")} | {get_formatted_key_value(player, "posicion")}')

#23.
def create_sub_list_stats_rankings(dict_list: list[dict]) -> list:
    """
    This function takes a list of dictionaries containing player stats and returns a new list of
    dictionaries with each player's name and their rankings in various stats categories.
    
    :param dict_list: A list of dictionaries, where each dictionary represents a player and their
    statistics in a basketball game. The dictionaries have the following keys: "nombre" (player name),
    "estadisticas" (a dictionary with keys "puntos_totales", "rebotes_totales", "asistencias
    :type dict_list: list[dict]
    :return: a list of dictionaries containing the name of each player and their rankings for four
    different statistics: total points, total rebounds, total assists, and total steals. The rankings
    are based on the values of each statistic in the original list of dictionaries passed as an argument
    to the function.
    """
    if not dict_list:
        return []
    else:
        rankings_dict_list = []
        for player in dict_list:
            rankings_dict_list.append({"nombre": player["nombre"]})
        
        stats = ["puntos_totales", "rebotes_totales", "asistencias_totales", "robos_totales"]
        for stat in stats:
            sorted_list = quicksort_for_dicts_double_key(dict_list, "estadisticas", stat, False)
            for index, sorted_player in enumerate(sorted_list):
                for player in rankings_dict_list:
                    if player["nombre"] == sorted_player["nombre"]:
                        player[f"{stat}_ranking"] = index + 1
                        break

        return rankings_dict_list
    
# EXTRA 1. - Determinate number of players for each position

def count_players_by_position(dict_list: list[dict]):
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return {"error": "empty list / not all elements in list are dicts."}
    else:
        positions_dict = {}
        for player in dict_list:
            position = player.get("posicion")
            if position:
                if position in positions_dict:
                    positions_dict[position] += 1
                else:
                    positions_dict[position] = 1
        return positions_dict

# EXTRA 2. - Show players list sorted by All-Star amount (descending)
# Output:
# Michael Jordan (14 veces all-star)
# Magic Johnson (12 veces all-star)

def sort_by_all_stars(origin_dict_list):
    if not origin_dict_list or not all(isinstance(d, dict) for d in origin_dict_list):
        return []
    else:
        #copy_list = origin_dict_list.copy()
        #copy_list = origin_dict_list[:]
        copy_list = copy.deepcopy(origin_dict_list)

        copy_list = [copy_player for copy_player in copy_list if any(re.search("all-star", a, re.I) for a in copy_player["logros"])]
        
        # SWITCHING ACHIEVEMENTS STR LIST TO AN INT
        for index, copy_player in enumerate(copy_list):
            for achievement in copy_player["logros"]:
                if re.search("all-star", achievement, re.I):
                    copy_list[index]["logros"] = int(achievement.split(" ", 1)[0])
                    break
        # SORTING LIST BY ALL-STARS NUMBER
        copy_list = quicksort_for_dicts(copy_list, "logros", False)
        
        # SWITCHING ACHIEVEMENTS STR LIST BACK
        for copy_player in copy_list:
            for player in origin_dict_list:
                if copy_player["nombre"] == player["nombre"]:
                    copy_player["logros"] = player["logros"]
                    break
        
        # ADDING PLAYER THAT DOESN'T HAVE "ALL-STAR" AS ACHIEVEMENT
        for or_player in origin_dict_list:
            if not any(re.search("all-star", a, re.I) for a in or_player["logros"]):
                #print(or_player["nombre"])
                copy_list.append(or_player)
        
        # PRINTING SORTED PLAYERS
        for copy_player in copy_list:
            if any(re.search("all-star", a, re.I) for a in copy_player["logros"]):
                print(f'{copy_player["nombre"]} | {copy_player["logros"][1]}')
            else:
                print(copy_player["nombre"] + " | :(")

# EXTRA 3. - GET BEST STATS PLAYER FOR EVERY VALUE AND PRINT THEM.

def get_best_stats_players(dict_list: list[dict]):
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return []
    else:
        max_seasons = get_highest_stat_player(dict_list, "estadisticas", "temporadas")
        max_total_points = get_highest_stat_player(dict_list, "estadisticas", "puntos_totales")
        max_points_avg = get_highest_stat_player(dict_list, "estadisticas", "promedio_puntos_por_partido")
        max_total_rebounds = get_highest_stat_player(dict_list, "estadisticas", "rebotes_totales")
        max_rebounds_avg = get_highest_stat_player(dict_list, "estadisticas", "promedio_rebotes_por_partido")
        max_total_assists = get_highest_stat_player(dict_list, "estadisticas", "asistencias_totales")
        max_assists_avg = get_highest_stat_player(dict_list, "estadisticas", "promedio_asistencias_por_partido")
        max_total_steals = get_highest_stat_player(dict_list, "estadisticas", "robos_totales")
        max_total_blocks = get_highest_stat_player(dict_list, "estadisticas", "bloqueos_totales")
        max_field_shots_pctg = get_highest_stat_player(dict_list, "estadisticas", "porcentaje_tiros_de_campo")
        max_free_throws_pctg = get_highest_stat_player(dict_list, "estadisticas", "porcentaje_tiros_libres")
        max_three_pointers_pctg = get_highest_stat_player(dict_list, "estadisticas", "porcentaje_tiros_triples")

        max_list = [max_seasons, max_total_points, max_points_avg, max_total_rebounds,
                    max_rebounds_avg, max_total_assists, max_assists_avg, max_total_steals,
                    max_total_blocks, max_field_shots_pctg, max_free_throws_pctg, max_three_pointers_pctg]

        max_strings_list = ["Max. total points", "Max. Points per game avg.",
                            "Max. total rebounds", "Max. rebounds per game avg.", "Max. total assists",
                            "Max. assists per game avg.","Max. total steals", "Max. total blocks",
                            "Max. field shots percent.", "Max. free throws percent.", "Max. 3-pointers percent."]
        
        print("Max. Seasons:", end= " ")
        for index, player in enumerate(max_seasons):
            print(f'{player["nombre"]}({player["estadisticas"]["temporadas"]})', end= " / ")
            if index+1 == len(max_seasons):
                print(" ")
 

        for index, max_str in enumerate(max_strings_list):
            print(f'{max_str}: {max_list[index][0]["nombre"]}')
        
 
# EXTRA 4. - 

##################

players_list = read_json_file("dt.json", "jugadores")

#print(count_players_by_position(players_list)) # WORKING

#sort_by_all_stars(players_list) # WORKING

#get_best_stats_players(players_list) # WORKING