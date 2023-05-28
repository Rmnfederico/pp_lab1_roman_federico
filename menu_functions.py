from exam_functions import *

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
    option: str = input("Enter your option:")
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
                save_dict_list_as_csv("stats_ranking.csv",create_sub_list_stats_rankings(dict_list), ",")
            case 0:
                print("\nSee you space cowboy.\n")
                break
            case _:
                print("incorrect option.")
                pass
        clear_console()