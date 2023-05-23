import re
import json

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