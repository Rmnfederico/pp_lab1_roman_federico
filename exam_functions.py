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

def parse_dict_values(dictionary: dict):
    if not dictionary or not isinstance(dictionary, dict):
        return None
    else:
        dictionary_string = ""
        for index, value in enumerate(dictionary.values()):
            if value and value != "":
                if index < (len(dictionary.values())-1):
                    dictionary_string += f'{value},'
                else:
                    dictionary_string += f'{value}\n'
        return dictionary_string

def parse_dict_keys(dictionary: dict):
    if not dictionary or not isinstance(dictionary, dict):
        return None
    else:
        dictionary_string = ""
        for index, key in enumerate(dictionary.keys()):
            if key:
                if index < (len(dictionary.keys())-1):
                    dictionary_string += f'{key},'
                else:
                    dictionary_string += f'{key}\n'
        return dictionary_string

def save_dict_as_csv(csv_filepath, dictionary: dict) -> bool:
    if not dictionary or not isinstance(dictionary, dict):
        print("Invalid input. The parameter must be a dictionary.")
        return False

    try:
        with open(csv_filepath, "w+") as file:
            written_bytes = file.write(parse_dict_keys(dictionary))
            written_bytes += file.write(parse_dict_values(dictionary))

        if written_bytes != 0:
            print(f'{written_bytes} bytes successfully written at "{csv_filepath}"')
            return True
        else:
            print(f'Error trying to write "{csv_filepath}" file.')
            return False

    except (FileNotFoundError, PermissionError, IOError) as err:
        print(f'An error occurred while saving the file: {err}')
        return False

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
    
def get_string(input_msg: str,retries: int = 0) -> str:
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
            selected_player = dict_list[player_index-1]
            list_column_key_values(selected_player["estadisticas"])
            save_player_statistics_as_csv(selected_player)
        else:
            print("index not found in list.")

#3. Save name, position, player statistics

def extract_statistics_dict(dictionary: dict) -> dict:
    if dictionary and isinstance(dictionary, dict):
        player_statistics_dict = dict()
        player_statistics_dict["nombre"] = dictionary.get("nombre")
        player_statistics_dict["posicion"] = dictionary.get("posicion")
        for key, value in dictionary["estadisticas"].items():
            player_statistics_dict[key] = value
        return player_statistics_dict
    else:
        return None

def save_player_statistics_as_csv(dictionary: dict) -> bool:
    option = get_string("Do you want to save player's statistics? (y/n)")
    if re.match(r"^[y]$", option, re.I):
        player_statistics_dict = extract_statistics_dict(dictionary)
        if save_dict_as_csv(f'{player_statistics_dict.get("nombre")}.csv'.replace(" ", "_"), player_statistics_dict):
            return True
    
    else:
        print("player's statistics not saved.")
        return False
    
#4. let user select a player by name, then list achievements for that player/s

def find_name_by_string_comp(dict_list: list[dict]):
    if not dict_list:
        return None
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
        print(f'{len(filtered_list)} players matched search parameter:')
        list_index_kv_pair(filtered_list, "nombre")
        return filtered_list
    else:
        print(f"no matches found for '{search_name}' in the list.")
        return None

def show_player_achievements_by_name(dict_list: list[dict]):
    if not dict_list or not all((d, dict) for d in dict_list):
        return None
    else:
        filtered_list = find_name_by_string_comp(dict_list)
        if not filtered_list:
            return None
        elif len(filtered_list) == 1:
            for achievement in filtered_list[0]["logros"]:
                print(achievement) 
        else:
            sub_option = get_int("\nselect index from found players:")
            if sub_option > 0 and sub_option <= len(filtered_list):
                print(f'\nAchievements for {filtered_list[sub_option-1].get("nombre")}:\n')
                for achievement in filtered_list[sub_option-1]["logros"]:
                    print(achievement)
            else:
                print(f"index {sub_option} not found.")
                return None


##########  ##########  ##########  ##########  ##########  ##########


players_list = read_json_file("dt.json", "jugadores")

#list_names_data(players_list, "posicion") # WORKING
#show_player_statistics(players_list) # WORKING
#show_player_achievements_by_name()

#show_player_achievements_by_name(players_list) # WORKING

