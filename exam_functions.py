import re
import json
import os


########## Menu Funcs. ##########

def print_menu() -> None:
    print("\nmain menu (first exam):\n")
    print("0. end program\n")
    print("A. Opt A")
    print("B. Opt B")
    print("C. Opt C")
    print("D. Opt D")
    print("E. Opt E")
    print("F. Opt F")



def main_menu():
    print_menu()
    option: str = input("enter your option:")
    if re.match(r'[A-F]', option.upper()) is not None:
        return option.upper()
    elif re.match(r'^[0]$', option):
        return 0
    else:
        return -1


def main_app(dict_list: list[dict]) -> None:
    selected_list = None
    while True:
        
        #TODO -> get_validated_float/int() functions
        match main_menu():
            case "A":
                opt_string = "option_a"
                #selected_list = list_N_heroes(dict_list, len(dict_list))
                pass # REMOVE
            case "B":
                opt_string = "option_b"
                #selected_list = sort_by_key_and_list(dict_list, "altura", True)
                pass # REMOVE
            case "C":
                opt_string = "option_c"
                #selected_list = sort_by_key_and_list(dict_list, "fuerza", True)
                pass # REMOVE
            case "D":
                opt_string = "option_d"
                #selected_list = calculate_avg_filter_greater_or_lesser(dict_list, "peso", True)
                pass # REMOVE
            case "E":
                opt_string = "option_e"
                #selected_list = find_heroes_by_int(dict_list, "avE RagE")
                pass # REMOVE
            case "F": # SAVE LAST OPTION TO CSV
                if selected_list and opt_string:
                    #save_dict_list_as_csv(f"{opt_string}.csv", selected_list)
                    selected_list, opt_string = None, None
                else:
                    print("ERROR! you need to select an option before saving.")
                    pass  
            case 0:
                print("program finished.")
                break
            case _:
                print("incorrect option.")
                pass

########## Files Handling ##########

def read_json_file(filepath: str, list_key) -> list:
    """
    This function reads a JSON file and returns a list of (dicts) from it.
    
    :param filepath: a string that represents the path to a file that contains
    data in JSON format
    :type filepath: str
    :return: a list of dictionaries read from a JSON file specified by the `filepath` parameter.
    """
    dict_lst = list()
    with open(filepath, "r") as file:
        dictionary = json.load(file)
        dict_lst = dictionary[list_key] # CHANGE ACCORDING TO LIST NAME
    return dict_lst


########## Validations / Get Inputs ##########

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def check_int_string(string: str) -> bool:
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


def get_int(input_msg: str, retries: int = 0) -> int:
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

def validate_range(number: int, min, max) -> bool:
    if not isinstance(number, int) or number < min or number > max:
        return False
    else:
        return True

def get_name_data(dictionary: dict, search_key: str) -> str:
    try:
        if search_key in dictionary and isinstance(dictionary, dict):
            return f'Name: {str(dictionary["nombre"]).ljust(15)}' + "\t|\t".center(5) + f'{search_key.capitalize()}:{dictionary[search_key]}'
    except KeyError as err:
        print(f"KeyError: {err} not in dict.")

def get_formatted_key_value(dictionary: dict, search_key: str) -> str:
    if not dictionary or not isinstance(dictionary, dict) or search_key not in dictionary:
        return None
    else:
        return f'{search_key.capitalize()}: {dictionary.get(search_key, "N/A")}'


########## Printing / Listing ##########

#1.
def list_names_data(dict_list: list[dict], search_key: str):
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
    if not dict_list or not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        for index, player in enumerate(dict_list):
            print(f'{index+1}-{get_formatted_key_value(player, search_key)}')

def list_column_key_values(dictionary: dict) -> None:
    if not dictionary or not isinstance(dictionary, dict):
        return None
    else:
        for key, value in dictionary.items():
            print(f'{key.capitalize().replace("_", " ")}: {value}')

def show_player_statistics(dict_list: list[dict]):
    if not dict_list:
        return None
    else:
        list_index_kv_pair(dict_list, "nombre")
        player_index = get_int("Enter the index of the player to show:")
        if validate_range((player_index-1), 0, (len(dict_list)-1)):
            list_column_key_values(dict_list[player_index-1]["estadisticas"])


##########  ##########  ##########  ##########  ##########  ##########


players_list = read_json_file("dt.json", "jugadores")

#list_names_data(players_list, "posicion") # WORKING
show_player_statistics(players_list)


