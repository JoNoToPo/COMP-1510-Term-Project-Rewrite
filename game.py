import map
import initialize
import player


def game():
    start_room = initialize.room_radomizer(8, 4)
    current_character = initialize.initialize_mob(initialize.new_character(), start_room)
    start_map = initialize.starting_map(start_room, 8, 4, 3)
    menu_text = (
            "-" * 53 +
            "/,------.        ,--.   ,--.       ,--.  ,--."
            "/|  .--. ' ,---. |  |   |  |,--.--.`--',-'  '-. ,---.  "
            "/|  '--'.'| .-. :|  |.'.|  ||  .--',--.'-.  .-'| .-. : "
            "/|  |\\  \\ \\   --.|   ,'.   ||  |   |  |  |  |  \\   --. "
            "/`--' '--' `----''--'   '--'`--'   `--'  `--'   `----' /"
            + "-" * 53 +
            "//Your name is " + current_character["name"] + " /and you are going to rewrite History" +
            "//To learn how to play type \"help\" at any time,"
            "/or if you want more details about any action /type \"help (action)\""
            " and it will be explained to you.")
    print(map.map_art(map.display_text_next_to_map(
        map.rewrite_spot(start_map, current_character["x_coordinate"], current_character["y_coordinate"], 2),
        menu_text, 0)))
    while True:
        player_input = str(input("To play, move to your time machine \"T\":")).strip().lower()
        if player_input:
            player.parse(player_input, current_character, start_map)
            print(map.map_art(map.display_text_next_to_map(
                map.rewrite_spot(start_map, current_character["x_coordinate"], current_character["y_coordinate"], 2),
                menu_text, 0)))
        else:
            continue


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()