from exam_functions import *

########## Menu Funcs. ##########

def print_menu() -> None:
    """
    This function prints a menu with various options for a program related to a basketball team.
    """
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
    """
    The function displays a menu, prompts the user for an option, and returns the option as an integer
    if it is a valid input.
    :return: The function `main_menu()` returns an integer value. If the user enters a valid option (a
    number between 0 and 20, or 23), the function returns that integer value. If the user enters an
    invalid option, the function returns -1.
    """
    print_menu()
    option: str = input("Enter your option:")
    if re.match(r'^(?:[0-9]|1[0-9]|20|23)$', option):
        return int(option)
    else:
        return -1

def main_app(dict_list: list[dict]) -> None:
    """
    This is the main function of a Python program that provides various options to display and analyze
    basketball player statistics.
    
    :param dict_list: A list of dictionaries containing basketball player statistics
    :type dict_list: list[dict]
    """

    option_two = False
    stats = "estadisticas"
    points_avg = "promedio_puntos_por_partido"
    total_rebounds = "rebotes_totales"
    field_shots_pctg = "porcentaje_tiros_de_campo"
    total_assists = "asistencias_totales"
    rebounds_avg = "promedio_rebotes_por_partido"
    assists_avg = "promedio_asistencias_por_partido"
    total_steals = "robos_totales"
    total_blocks = "bloqueos_totales"
    free_throw_pctg = "porcentaje_tiros_libres"
    three_pointers_pctg = "porcentaje_tiros_triples"
    seasons = "temporadas"

    while True:
        match main_menu():
            case 1:
                list_names_data(dict_list, "posicion")
            case 2:
                selected_player = get_player_statistics(dict_list)
                print_column_key_values(selected_player[stats], selected_player["nombre"])
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
                list_name_stat(calc_avg_points_list_players(dict_list), points_avg)
            case 6:
                show_player_hall_of_fame(dict_list)
            case 7:
                list_name_stat(get_highest_stat_player(dict_list, stats, total_rebounds), total_rebounds, "\nMax. rebounds player/s:")
            case 8:
                list_name_stat(get_highest_stat_player(dict_list, stats, field_shots_pctg), field_shots_pctg, "Max. field shots percentage player/s")
            case 9:
                list_name_stat(get_highest_stat_player(dict_list, stats, total_assists), total_assists, "Max. total assists player/s")
            case 10:
                list_name_stat(get_higher_stats_per_game_list(dict_list, stats, points_avg), points_avg, f"Higher {points_avg.replace('_', ' ')} list")
            case 11:
                list_name_stat(get_higher_stats_per_game_list(dict_list, stats, rebounds_avg), rebounds_avg, f"Higher {rebounds_avg.replace('_', ' ')} list")
            case 12:
                list_name_stat(get_higher_stats_per_game_list(dict_list, stats, assists_avg), assists_avg, f"Higher {assists_avg.replace('_', ' ')} list")
            case 13:
                list_name_stat(get_highest_stat_player(dict_list, stats, total_steals), total_steals, "Max. total steals player/s")
            case 14:
                list_name_stat(get_highest_stat_player(dict_list, stats, total_blocks), total_blocks, "Max. total blocks player/s")
            case 15:
                list_name_stat(get_higher_stats_per_game_list(dict_list, stats, free_throw_pctg), free_throw_pctg, f"Higher {free_throw_pctg.replace('_', ' ')} list")
            case 16:
                show_points_per_game_avg_less_lower(dict_list)
            case 17:
                show_highest_achievements_player(dict_list)
            case 18:
                list_name_stat(get_higher_stats_per_game_list(dict_list, stats, three_pointers_pctg), three_pointers_pctg, f"Higher {three_pointers_pctg.replace('_', ' ')} list")
            case 19:
                list_name_stat(get_highest_stat_player(dict_list, stats, seasons), seasons, "Max. numb. of played seasons player/s")
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