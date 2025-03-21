import map
import initialize as i
import player
import text as t
import levels


def game():
    """
    Drive the game
    """
    achieved_goal = True
    current_character = player.new_character()
    time_machine = {"x_coordinate": 0, "y_coordinate": 0, "content": " T ", "alive": True}
    while True:
        if (achieved_goal and current_character["y_coordinate"] == time_machine["y_coordinate"] and
                current_character["x_coordinate"] == time_machine["x_coordinate"]):
            current_character["level"] += 1
            enemies = levels.append_enemies(current_character)
            start_room = i.room_radomizer(8 + current_character["level"], 4 + current_character["level"])
            i.initialize_mob(current_character, start_room)
            time_machine = i.initialize_mob({"x_coordinate": 0, "y_coordinate": 0}, start_room)
            current_map = i.starting_map(start_room, 8, 4, 2 + current_character["level"])
            for enemy in enemies:
                i.initialize_mob(enemy, current_map)
            map.rewrite(current_map, time_machine["x_coordinate"], time_machine["y_coordinate"], " T ")
            map.rewrite(current_map, current_character["x_coordinate"], current_character["y_coordinate"], " @ ")
            level_text = t.line + t.title + t.line + "//Your name is " + current_character["name"] + t.start_text
            print(map.map_art(map.display_text_next_to_map(
                current_map, level_text, 0)))
        achieved_goal = levels.check_level_goal(current_character, enemies)
        player_input = str(input("To play, move to your time machine \"T\":")).strip().lower()
        if player_input:
            action = player.parse(player_input, current_character, current_map, achieved_goal)
            if type(action) == type("string"):
                print(map.map_art(map.display_text_next_to_map(
                    current_map, action, 0)))
            else:
                print(map.map_art(map.display_text_next_to_map(
                    current_map, level_text, 0)))
        else:
            print("Please make an Input")



def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()