import exam_functions as funcs
from menu_functions import main_app 

#### PROGAM START ####

players_list = funcs.read_json_file("dt.json", "jugadores")

main_app(players_list)


