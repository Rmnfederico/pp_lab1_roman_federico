from menu_functions import main_app 
from files_handling_functions import read_json_file

#### PROGAM START ####

players_list = read_json_file("dt.json", "jugadores")

main_app(players_list)


