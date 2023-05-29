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
    """
    The function takes a dictionary and a delimiter as input, and returns a string of non-empty values
    from the dictionary separated by the delimiter.
    
    :param dictionary: A dictionary object that contains key-value pairs
    :type dictionary: dict
    :param delimiter: The delimiter parameter is a string that specifies the character(s) to be used to
    separate the values in the output string. By default, it is set to ",", defaults to ,
    :type delimiter: str (optional)
    :return: a string that contains the non-empty values of the input dictionary separated by the
    specified delimiter. If the input is not a dictionary or is empty, the function returns None.
    """
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
    """
    The function takes a dictionary and a delimiter as input, and returns a string of the dictionary
    keys separated by the delimiter.
    
    :param dictionary: A dictionary object that you want to parse the keys of
    :type dictionary: dict
    :param delimiter: The delimiter parameter is a string that specifies the character(s) to be used to
    separate the keys in the output string. By default, it is set to ",", defaults to ,
    :type delimiter: str (optional)
    :return: a string that contains all the keys of the input dictionary separated by a delimiter
    (default is comma) and a newline character at the end. If the input is not a dictionary or is empty,
    the function returns None.
    """
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
    """
    This function saves a dictionary as a CSV file with a specified delimiter.
    
    :param csv_filepath: The file path and name where the CSV file will be saved
    :param dictionary: The dictionary parameter is a dictionary object that contains key-value pairs to
    be saved as a CSV file
    :type dictionary: dict
    :param delimiter: The delimiter parameter is a string that specifies the character used to separate
    values in the CSV file. By default, it is set to "," (comma), defaults to ,
    :type delimiter: str (optional)
    :return: a boolean value indicating whether the dictionary was successfully saved as a CSV file or
    not.
    """
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
    """
    This function saves a list of dictionaries as a CSV file.
    
    :param csv_filepath: The file path where the CSV file will be saved
    :param dict_list: A list of dictionaries that will be saved as a CSV file
    :type dict_list: list[dict]
    :param delimiter: The delimiter parameter is a string that specifies the character used to separate
    values in the CSV file. By default, it is set to "," (comma), but it can be changed to any other
    character such as ";" (semicolon) or "\t" (tab), defaults to ,
    :type delimiter: str (optional)
    :return: a boolean value indicating whether the operation was successful or not.
    """
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