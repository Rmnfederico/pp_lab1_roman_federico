import exam_functions as funcs

#### PROGAM START ####

players_list = funcs.read_json_file("dt.json", "jugadores")

funcs.main_app(players_list)

