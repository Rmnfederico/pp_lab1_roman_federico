import json

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