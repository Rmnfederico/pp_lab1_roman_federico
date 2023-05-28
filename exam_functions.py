import re
import os
from files_handling_functions import *

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

#3. Save name, position & player statistics
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

        for player in positions_list:
            print(f'{get_formatted_key_value(player, "nombre")} | {get_formatted_key_value(player["estadisticas"], "porcentaje_tiros_de_campo")} | {get_formatted_key_value(player, "posicion")}')

#23.

def create_sub_list_stats_rankings(dict_list: list[dict]) -> list:
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
                
        
        #print(rankings_dict_list)

##########  ##########  ##########  ##########  ##########  ##########

players_list = read_json_file("dt.json", "jugadores")

#save_dict_list_as_csv("stats_ranking.csv",create_sub_list_stats_rankings(players_list), ",")