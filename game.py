import map
import initialize as i
import player
import text as t
import levels
from text import input_color


def game():
    """
    Drive the game
    """
    achieved_goal = True
    current_character = player.new_character()
    time_machine = {"name": "Time Machine", "x_coordinate": 0, "y_coordinate": 0, "alive": True, "symbol": input_color(" T ", "BLUE")}
    while True:
        if achieved_goal:
            if (current_character["y_coordinate"] == time_machine["y_coordinate"] and
                    current_character["x_coordinate"] == time_machine["x_coordinate"]):
                current_character["level"] += 1
                mobs = levels.append_mobs(current_character)
                start_room = i.room_radomizer(8 + current_character["level"], 4 + current_character["level"])
                i.initialize_mob(current_character, start_room)
                time_machine = i.initialize_mob(time_machine, start_room)
                current_map = i.starting_map(start_room, 8, 4, 1 + current_character["level"])
                map.rewrite(current_map, time_machine["x_coordinate"], time_machine["y_coordinate"],
                            time_machine["symbol"])
                map.rewrite(current_map, current_character["x_coordinate"], current_character["y_coordinate"],
                            current_character["symbol"])
                for mob in mobs:
                    i.initialize_mob(mob, current_map)
                    map.rewrite(current_map, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
                level_text = t.level_text(current_character)
                print(map.level_start_display(map.display_text_next_to_map({(0, 0): ""}, level_text, 0)))
                map.map_art(map.display_text_next_to_map(current_map, level_text, 0))
        achieved_goal = levels.check_level_goal(current_character, mobs)
        player_input = str(input("To play, please make any input:")).strip().lower()
        if player_input:
            action = player.parse(player_input, current_character, current_map, achieved_goal)
            if type(action) == type("string"):
                print(map.map_art(map.display_text_next_to_map(
                    current_map, action, 0)))
            else:
                levels.mob_ai(mobs, current_map)
                levels.overwritten(current_map, [time_machine, current_character])
                if current_character["alive"]:
                    print(map.map_art(map.display_text_next_to_map(
                        current_map, level_text, 0)))
                else:
                    print(player.how_died(current_map, current_character))
        else:
            print("Please make an Input")


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()