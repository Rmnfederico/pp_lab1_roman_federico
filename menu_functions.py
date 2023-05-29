from exam_functions import *

########## Menu Funcs. ##########

def print_menu() -> None:
    justification = 68
    print("\n┌-------------------------------------------------------------------------┐")
    print("|\t\tMain Menu (first exam - Dream Team):".ljust(61)+"|")
    print("├-------------------------------------------------------------------------┤")
    print("|\t".ljust(justification)+"|")
    print("|\t0. Exit program".ljust(justification)+"|")
    print("|\t".ljust(justification)+"|")
    print("|\t1. List Dream Team players & positions".ljust(justification)+"|")
    print("|\t2. Show a player's stats by index & save to csv".ljust(justification)+"|")
    print("|\t3. Save option 3 as csv".ljust(justification)+"|")
    print("|\t4. Search player by name and show achievements".ljust(justification)+"|")
    print("|\t5. List points per game average, sorted by ascending names".ljust(justification)+"|")
    print("|\t6. Search player by name and show if they belong to hall of fame".ljust(justification)+"|")
    print("|\t7. Show highest total rebounds player/s".ljust(justification)+"|")
    print("|\t8. Show highest field shots average player/s".ljust(justification)+"|")
    print("|\t9. Show highest total assists player/s".ljust(justification)+"|")
    print("|\t10. Enter a value and filter higher points per game avg. list".ljust(justification)+"|")
    print("|\t11. Enter a value and filter higher rebounds per game avg. list".ljust(justification)+"|")
    print("|\t12. Enter a value and filter higher assists per game avg. list".ljust(justification)+"|")
    print("|\t13. Show highest total steals player/s".ljust(justification)+"|")
    print("|\t14. Show highest total blocks player/s".ljust(justification)+"|")
    print("|\t15. Enter a value and filter higher free throws percentage list".ljust(justification)+"|")
    print("|\t16. Show team's points per game average w/o lowest points player".ljust(justification)+"|")
    print("|\t17. Show highest number of achiements player/s".ljust(justification)+"|")
    print("|\t18. Enter a value and filter higher three-pointers percentage list".ljust(justification)+"|")
    print("|\t19. Show highest number of seasons played player/s".ljust(justification)+"|")
    print("|\t20. Enter a value and filter higher field shots percentage list".ljust(justification)+"|")
    print("|\t23. Rank players by stats and save as csv.".ljust(justification)+"|")
    print("└-------------------------------------------------------------------------┘\n")

def main_menu() -> int:
    print_menu()
    option: str = input("Enter your option:")
    if re.match(r'^(?:[0-9]|1[0-9]|20|23)$', option):
        return int(option)
    else:
        return -1

def main_app(dict_list: list[dict]) -> None:
    
    option_two = False
    while True:
        match main_menu():
            case 1:
                list_names_data(dict_list, "posicion")
            case 2:
                selected_player = get_player_statistics(dict_list)
                print_column_key_values(selected_player["estadisticas"], selected_player["nombre"])
                option_two = True
            case 3:
                if option_two:
                    save_player_statistics_as_csv(selected_player)
                    selected_player, option_two = None, False
                else:
                    print("No player selected in option 2 to save.")
            case 4:
                show_player_achievements_by_name(dict_list)
            case 5:
                list_name_stat(calc_avg_points_list_players(dict_list), "promedio_puntos_por_partido")
            case 6:
                show_player_hall_of_fame(dict_list)
            case 7:
                list_name_stat(get_highest_stat_player(dict_list, "estadisticas", "rebotes_totales"), "rebotes_totales", "\nMax. rebounds player/s:")
            case 8:
                list_name_stat(get_highest_stat_player(dict_list, "estadisticas", "porcentaje_tiros_de_campo"),"porcentaje_tiros_de_campo","Max. field shots percentage player/s")
            case 9:
                list_name_stat(get_highest_stat_player(dict_list, "estadisticas", "asistencias_totales"),"asistencias_totales","Max. total assists player/s")
            case 10:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "promedio_puntos_por_partido")
            case 11:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "promedio_rebotes_por_partido")
            case 12:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "promedio_asistencias_por_partido")
            case 13:
                #show_highest_stat_player(dict_list, "estadisticas", "robos_totales", "total steals")
                pass
            case 14:
                #show_highest_stat_player(dict_list, "estadisticas", "bloqueos_totales", "total blocks")
                pass
            case 15:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "porcentaje_tiros_libres")
            case 16:
                show_points_per_game_avg_less_lower(dict_list)
            case 17:
                show_highest_achievements_player(dict_list)
            case 18:
                show_higher_stats_per_game_list(dict_list, "estadisticas", "porcentaje_tiros_triples")
            case 19:
                #show_highest_stat_player(dict_list, "estadisticas", "temporadas", "amount of played seasons")
                pass
            case 20:
                list_by_position_higher_stats(dict_list)
            case 23:
                save_dict_list_as_csv("stats_ranking.csv",create_sub_list_stats_rankings(dict_list), ",")
            case 0:
                print("\nSee you space cowboy.\n")
                break
            case _:
                print("incorrect option.")
                pass
        clear_console()