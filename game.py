import map
import initialize
import player


def game():
    start_room = initialize.room_radomizer(8, 4)
    current_character = initialize.initialize_mob(initialize.new_character(), start_room)
    start_map = initialize.starting_map(start_room, 8, 4)
    test_text = "-" * 30 + "/Your name is " + current_character["name"] + " /and you are going to rewrite History/" + "-" * 30 + "/JONTOTO//GODO"
    print(map.map_art(map.display_text_next_to_map(
        map.rewrite_spot(start_map, current_character["x_coordinate"], current_character["y_coordinate"], 2), test_text,
        2)))
    while True:
        player_input = str(input()).strip().lower()
        if player_input:
            player.parse(player_input, current_character, start_map)
            print(map.map_art(map.display_text_next_to_map(
                map.rewrite_spot(start_map, current_character["x_coordinate"], current_character["y_coordinate"], 2),
                test_text,
                2)))
        else:
            continue


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()