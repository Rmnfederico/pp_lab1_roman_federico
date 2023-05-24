import re
import json


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

def read_json_file(filepath: str, list_key):
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

##########  ##########  ##########  ##########  ##########  ##########

#1.
def get_name_data(dictionary: dict, search_key: str) -> str:
    try:
        if search_key in dictionary and isinstance(dictionary, dict):
            return f'Name: {dictionary["nombre"]} | {search_key.capitalize()}: {dictionary[search_key]}'
    except KeyError as err:
        print(f"KeyError: {err} not in dict.")

def list_names_data(dict_list: list[dict], search_key: str):
    if not dict_list or not isinstance(dict_list, list):
        return None
    else:
        for index, dictionary in enumerate(dict_list):
            if search_key in dictionary:
                print(f'{index+1}-{get_name_data(dictionary, search_key)}')

#2. 

###############

players_list = read_json_file("dt.json", "jugadores")

list_names_data(players_list, "posicion") # WORKING
