import re
import json
import os

########## Menu Funcs. ##########

def print_menu() -> None:
    print("\n┌-------------------------------------------------------------------------┐")
    print("|\t\tMain Menu (first exam - Dream Team):".ljust(61)+"|")
    print("├-------------------------------------------------------------------------┤")
    print("|\t".ljust(68)+"|")
    print("|\t0. Exit program".ljust(68)+"|")
    print("|\t".ljust(68)+"|")
    print("|\t1. List Dream Team players & positions".ljust(68)+"|")
    print("|\t2. Show a player's stats by index & save to csv".ljust(68)+"|")
    print("|\t3. Show a player's stats by index & save to csv".ljust(68)+"|")
    print("|\t4. Search player by name and show achievements".ljust(68)+"|")
    print("|\t5. List points per game average, sorted by ascending names".ljust(68)+"|")
    print("|\t6. Search player by name and show if they belong to hall of fame".ljust(68)+"|")
    print("|\t7. Show highest total rebounds player/s".ljust(68)+"|")
    print("|\t8. Show highest field shots average player/s".ljust(68)+"|")
    print("|\t9. Show highest total assists player/s".ljust(68)+"|")
    print("|\t10. Enter a value and filter higher points per game avg. list".ljust(68)+"|")
    print("|\t11. Enter a value and filter higher rebounds per game avg. list".ljust(68)+"|")
    print("|\t12. Enter a value and filter higher assists per game avg. list".ljust(68)+"|")
    print("|\t13. Show highest total steals player/s".ljust(68)+"|")
    print("|\t14. Show highest total blocks player/s".ljust(68)+"|")
    print("|\t15. Enter a value and filter higher free throws percentage list".ljust(68)+"|")
    print("|\t16. Show team's points per game average w/o lowest points player".ljust(68)+"|")
    print("|\t17. Show highest number of achiements player/s".ljust(68)+"|")
    print("|\t18. Enter a value and filter higher three-pointers percentage list".ljust(68)+"|")
    print("|\t19. Show highest number of seasons played player/s".ljust(68)+"|")
    print("|\t20. Enter a value and filter higher field shots percentage list".ljust(68)+"|")
    print("|\t23. Rank players by a given stat.".ljust(68)+"|")
    print("└-------------------------------------------------------------------------┘\n")

def main_menu() -> int:
    print_menu()
    option: str = input("enter your option:")
    if re.match(r'^(?:[0-9]|1[0-9]|20|23)$', option):
        return int(option)
    else:
        return -1

def main_app(dict_list: list[dict]) -> None:

    while True:
        
        match main_menu():
            case 1:
                list_names_data(dict_list, "posicion")
            case 2:
                show_player_statistics(dict_list)
            case 3:
                show_player_statistics(dict_list)
            case 4:
                show_player_achievements_by_name(dict_list)
            case 5:
                calc_avg_points_list_players(dict_list)
            case 6:
                show_player_hall_of_fame(dict_list)
            case 7:
                show_highest_stat_player(dict_list, "estadisticas", "rebotes_totales", "rebounds")
            case 8:
                show_highest_stat_player(dict_list, "estadisticas", "porcentaje_tiros_de_campo", "field shots percentage")
            case 9:
                show_highest_stat_player(dict_list, "estadisticas", "asistencias_totales", "total assists")
            case 10:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "promedio_puntos_por_partido")
            case 11:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "promedio_rebotes_por_partido")
            case 12:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "promedio_asistencias_por_partido")
            case 13:
                show_highest_stat_player(dict_list, "estadisticas", "robos_totales", "total steals")
            case 14:
                show_highest_stat_player(dict_list, "estadisticas", "bloqueos_totales", "total blocks")
            case 15:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "porcentaje_tiros_libres")
            case 16:
                show_points_per_game_avg_less_lower(dict_list)
            case 17:
                show_highest_achievements_player(dict_list)
            case 18:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "porcentaje_tiros_triples")
            case 19:
                show_highest_stat_player(dict_list, "estadisticas", "temporadas", "amount of played seasons")
            case 20:
                list_by_position_higher_stats(dict_list)
            case 23:
                rank_by_stat_export_csv(dict_list)
            case 0:
                print("\nSee you space cowboy.\n")
                break
            case _:
                print("incorrect option.")
                pass
        clear_console()

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
    with open(filepath, "r", encoding= "utf-8") as file:
        dictionary = json.load(file)
        dict_lst = dictionary[list_key] # CHANGE ACCORDING TO LIST NAME
    return dict_lst

def parse_dict_values(dictionary: dict, delimiter:str = ",") -> str:
    if not dictionary or not isinstance(dictionary, dict):
        return None
    else:
        dictionary_string = ""
        for index, value in enumerate(dictionary.values()):
            if value and value != "":
                if index < (len(dictionary.values())-1):
                    dictionary_string += f'{value}{delimiter}'
                else:
                    dictionary_string += f'{value}\n'
        return dictionary_string

def parse_dict_keys(dictionary: dict, delimiter:str = ",") -> str:
    if not dictionary or not isinstance(dictionary, dict):
        return None
    else:
        dictionary_string = ""
        for index, key in enumerate(dictionary.keys()):
            if key:
                if index < (len(dictionary.keys())-1):
                    dictionary_string += f'{key}{delimiter}'
                else:
                    dictionary_string += f'{key}\n'
        return dictionary_string

def save_dict_as_csv(csv_filepath, dictionary: dict, delimiter:str = ",") -> bool:
    if not dictionary or not isinstance(dictionary, dict):
        print("Invalid input. The parameter must be a dictionary.")
        return False

    try:
        with open(csv_filepath, "w+", encoding="utf-8") as file:
            written_bytes = file.write(parse_dict_keys(dictionary, delimiter))
            written_bytes += file.write(parse_dict_values(dictionary, delimiter))

        if written_bytes != 0:
            print(f'{written_bytes} bytes successfully written at "{csv_filepath}"')
            return True
        else:
            print(f'Error trying to write "{csv_filepath}" file.')
            return False

    except (FileNotFoundError, PermissionError, IOError) as err:
        print(f'An error occurred while saving the file: {err}')
        return False
    
def save_dict_list_as_csv(csv_filepath, dict_list: list[dict], delimiter: str = ",") -> bool:
    if not dict_list or not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
        print("empty list / not all elements in list are dicts.")
        return False
    else:
        try:
            could_write = False
            with open(csv_filepath, "w+", encoding="utf-8") as file:
                written_bytes = file.write(parse_dict_keys(dict_list[0], delimiter))
                for dictionary in dict_list:
                    written_bytes += file.write(parse_dict_values(dictionary, delimiter))
            if written_bytes != 0:
                print(f'{written_bytes} bytes successfully written at "{csv_filepath}"')
                could_write = True
                return could_write
            else:
                print(f'error trying to write "{csv_filepath}" file.')
                could_write = False
                return could_write
        except (FileNotFoundError, PermissionError, IOError) as err:
            print(f'An error occurred while saving the file: {err}')
            return could_write

########## Validations / Get Inputs ##########

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('\nPress a key to continue...')
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

def check_float_string(string: str) -> bool:
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
    if not dict_list:
        return None
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

#1.
def list_names_data(dict_list: list[dict], search_key: str) -> None:
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

def show_player_statistics(dict_list: list[dict]) -> None:
    if not dict_list:
        return None
    else:
        list_index_kv_pair(dict_list, "nombre")
        player_index = get_int("Enter the index of the player to show:")
        if validate_range((player_index-1), 0, (len(dict_list)-1)):
            selected_player = dict_list[player_index-1]
            print(f'\nShowing statistics for {selected_player["nombre"]}:\n')
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
    option = get_string("\nDo you want to save player's statistics as csv? (y/n)")
    if re.match(r"^[y]$", option, re.I):
        player_statistics_dict = extract_statistics_dict(dictionary)
        if save_dict_as_csv(f'{player_statistics_dict.get("nombre")}.csv'.replace(" ", "_"), player_statistics_dict):
            return True
    
    else:
        print("player's statistics not saved.")
        return False
    
#4. let user select a player by name, then list achievements for that player/s

def find_name_by_string_comp(dict_list: list[dict]) -> list:
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
        print(f'{len(filtered_list)} player/s matched search parameter:\n')
        list_index_kv_pair(filtered_list, "nombre")
        return filtered_list
    else:
        print(f"no matches found for '{search_name}' in the list.")
        return None

def show_player_achievements_by_name(dict_list: list[dict]) -> None:
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
            sub_option = get_int("\nselect index from found players or 0 to print all:")
            if sub_option == 0:
                for player in filtered_list:
                    print(f'\nAchievements for {player["nombre"]}:')
                    for achievements in player["logros"]:
                        print(achievements)
            elif validate_range(sub_option, 1, len(filtered_list)):
                print(f'\nAchievements for {filtered_list[sub_option-1].get("nombre")}:\n')
                for achievement in filtered_list[sub_option-1]["logros"]:
                    print(achievement)
            else:
                print(f"index {sub_option} not found.")
                return None

#5. calc. & show avg. points per game (per dream team player) sorted by name (asc)
def calc_avg_points_list_players(dict_list: list[dict]) -> None:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        sorted_list = quicksort_for_dicts(dict_list, "nombre", True)
        points_avg = calculate_avg(sorted_list, "estadisticas", "promedio_puntos_por_partido")
        print(f'\nThe average points per game for the whole team is {points_avg}\n')
        for player in sorted_list:
             print(f'Name: {str(player["nombre"]).ljust(15)}' + "\t|\t".center(5) + f'Promedio puntos por partido: {player["estadisticas"]["promedio_puntos_por_partido"]}')

#6. let user select a player by name and show if he belongs to hall of fame
def filter_values_from_dict_list(dict_list: list[dict], search_key, filter_string: str) -> list:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        pattern = fr'({filter_string})$'
        return [d for d in dict_list if any(re.search(pattern, item, re.I) for item in d.get(search_key, []))]

def show_player_hall_of_fame(dict_list: list[dict]) -> None:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
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
def show_highest_stat_player(dict_list: list[dict], search_key: str, search_sub_key: str, stat) -> dict:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        max_stat_players = calculate_max_min_data_dicts(players_list, search_key, search_sub_key, True)
        if not max_stat_players:
            return None
        else:
            print(f"\nMax. {stat} player/s:")
            for player in max_stat_players:
                print(f'{get_formatted_key_value(player, "nombre")} | {get_formatted_key_value(player[search_key], search_sub_key)}')

def filter_greater_or_lesser(dict_list: list[dict], search_key, search_sub_key, greater: bool = True) -> list:
    if not dict_list:
        return None
    else:
        value = get_float("Enter a points per game value (can be float):")
        lesser_list = list()
        greater_list = list()
        for dictionary in dict_list:
            #REFACTOR VALIDATION SO FUNC. INSTANTLY BREAKS WHEN INVALID PARAM. KEYS
            if search_key in dictionary and search_sub_key in dictionary[search_key]:
                if dictionary[search_key][search_sub_key] < value:
                    lesser_list.append(dictionary)
                else:
                    greater_list.append(dictionary)
        
        if not lesser_list and not greater_list:
            print("search key / search sub key not found in any dict.")
            return None
        else:
            if greater: #IMPLEMENT TERNARY OPERATOR?
                return greater_list
            else:
                return lesser_list

def show_higher_stats_per_game_list(dict_list: list[dict], search_key: str, sub_search_key: str) -> None:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        filtered_list = filter_greater_or_lesser(dict_list, search_key, sub_search_key, True)
        if not filtered_list:
            print("no matches found for the value entered.")
            return None
        else:
            print(f'\nHigher {sub_search_key.replace("_", " ")} list:\n')
            for player in filtered_list:
                print(f'{get_formatted_key_value(player, "nombre")} | {get_formatted_key_value(player[search_key], sub_search_key)}')

#16.
def show_points_per_game_avg_less_lower(dict_list: list[dict]) -> None:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        return None
    else:
        sorted_list = quicksort_for_dicts([extract_statistics_dict(d) for d in dict_list], "promedio_puntos_por_partido", True)
        lowest_name, lowest_score = sorted_list[0]['nombre'], sorted_list[0]['promedio_puntos_por_partido']
        print(f"\nAvg w/o {lowest_name}'s score ({lowest_score}):\n{calculate_avg(sorted_list[1:], 'promedio_puntos_por_partido', '', False)}")


#17. REFACTOR

#CALC. AUX FUNC
def calc_max_data_dicts(dict_list: list[dict], search_key: str, comp_len: bool = False) -> list:
    if not dict_list or not all(isinstance(d, dict) for d in dict_list):
        print("empty list / not all elements in list are dicts.")
        return None
    else:
        if not all(search_key in d for d in dict_list):
            print(f"search key '{search_key}' not present in all dicts.")
            return None
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

        #REFACTOR TO RETURN LIST SO MULTIPLE K-V PAIRS CAN BE PRINTED/LISTED
        #TAKE OUT PRINTING RESPONSABILITY TO THESE FUNCS. RETURN LISTS AND PRIN THE SEPARATELY
        #WITH A DECENT PRINTING FUNCTION, C'MON YOU LAZY TRASHCAN
        #show_higher_stats_per_game_list(positions_list, "estadisticas", "porcentaje_tiros_de_campo")

        for player in positions_list:
            print(f'{get_formatted_key_value(player, "nombre")} | {get_formatted_key_value(player["estadisticas"], "porcentaje_tiros_de_campo")} | {get_formatted_key_value(player, "posicion")}')

#23.
def rank_by_stat_export_csv(dict_list:list[dict]) -> bool:
    if not dict_list:
        return False
    else:
        print("Ranky by:\n1.Total Points scored\n2.Total Rebounds")
        print("3.Total assists\n4.Total steals")
        option = get_int("Select an option (number):")
        match option:
            case 1:
                selected_stat = "puntos_totales"
            case 2:
                selected_stat = "rebotes_totales"
            case 3:
                selected_stat = "asistencias_totales"
            case 4:
                selected_stat = "robos_totales"
            case _:
                print("incorrect option.")
                return False
        
        sorted_list = quicksort_for_dicts_double_key(dict_list, "estadisticas", selected_stat, False)
        for index, player in enumerate(sorted_list):
            print(f'Rank {index+1} | {get_formatted_key_value(player, "nombre")} | {get_formatted_key_value(player["estadisticas"], selected_stat)}')
        if save_dict_list_as_csv(f'{selected_stat}_list.csv', sorted_list, ";"):
            return True
        else:
            print("list could not be saved to a csv file.")
            return False


##########  ##########  ##########  ##########  ##########  ##########


players_list = read_json_file("dt.json", "jugadores")

#list_names_data(players_list, "posicion") # WORKING -1
#show_player_statistics(players_list) # WORKING -2/3

#show_player_achievements_by_name(players_list) # WORKING -4

#calc_avg_points_list_players(players_list) # WORKING -5
#show_player_hall_of_fame(players_list) # WORKING -6

#show_highest_stat_player(players_list, "estadisticas", "rebotes_totales", "rebounds") # WORKING -7
#show_highest_stat_player(players_list, "estadisticas", "porcentaje_tiros_de_campo", "field shots percentage") #WORKING -8
#show_highest_stat_player(players_list, "estadisticas", "asistencias_totales", "total assists") # WORKING -9

#show_higher_stats_per_game_list(players_list, "estadisticas", "promedio_puntos_por_partido") # WORKING -10
#show_higher_stats_per_game_list(players_list, "estadisticas", "promedio_rebotes_por_partido") # WORKING -11
#show_higher_stats_per_game_list(players_list, "estadisticas", "promedio_asistencias_por_partido") # WORKING -12

#show_highest_stat_player(players_list, "estadisticas", "robos_totales", "total steals") # WORKING -13
#show_highest_stat_player(players_list, "estadisticas", "bloqueos_totales", "total blocks") # WORKING -14

#show_higher_stats_per_game_list(players_list, "estadisticas", "porcentaje_tiros_libres") # WORKING -15

#show_points_per_game_avg_less_lower(players_list) # WORKING -16

#show_highest_achievements_player(players_list) # WORKING -17 (TO REFACTOR PRINT)

#show_higher_stats_per_game_list(players_list, "estadisticas", "porcentaje_tiros_triples") # WORKING -18

#show_highest_stat_player(players_list, "estadisticas", "temporadas", "amount of played seasons") # WORKING -19

#list_by_position_higher_stats(players_list) # WORKING -20 -> REFACTOR PRINTED LIST

#rank_by_stat_export_csv(players_list) # WORKING -23
