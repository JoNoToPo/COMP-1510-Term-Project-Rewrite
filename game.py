import map
import initialize as i
import player
import text
import text as t
import levels
from text import input_color


def game():
    """
    Drive the game
    """
    achieved_goal = True
    current_character = player.new_character()
    time_machine = {"name": "Time Machine", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                    "symbol": input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}
    current_map = {}
    mobs = []
    level_text = ""
    while True:
        if achieved_goal:
            print(f"to continue to the next level please proceed to the time machine "
                  f"\"{input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}\"")
            if (current_character["y_coordinate"] == time_machine["y_coordinate"] and
                    current_character["x_coordinate"] == time_machine["x_coordinate"]):
                current_character["level"] += 1
                current_character["area"] += 2
                if current_character["level"] == 5:
                    print(text.win)
                    break
                mobs = levels.append_mobs(current_character)
                start_room = i.room_radomizer(8 + current_character["level"], 4 + current_character["level"])
                time_machine = i.initialize_mob(time_machine, start_room, {(0, 0): 1})
                i.initialize_mob(current_character, start_room, {(0, 0): 1})
                current_map = i.starting_map(start_room, 8, 4, current_character["level"] + 1)
                map.rewrite(current_map, time_machine["x_coordinate"], time_machine["y_coordinate"],
                            time_machine["symbol"])
                map.rewrite(current_map, current_character["x_coordinate"], current_character["y_coordinate"],
                            current_character["symbol"])
                for mob in mobs:
                    i.initialize_mob(mob, current_map, start_room)
                    map.rewrite(current_map, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
                level_text = t.level_text(current_character)
                print(map.level_start_display(level_text))
                input("To play, please make any input:")
                achieved_goal = False
                print(map.map_art(map.display_text_next_to_map(current_map, level_text, 0), current_character))
        player_input = str(input("move with 'w', 'a', 's', or 'd'")).strip().lower()
        action = 0
        if player_input[0] in ["w", "a", "s", "d"]:
            player.move(player_input, current_character, current_map, achieved_goal)
        elif player_input.split()[0] == "help":
            action = player.player_help(player_input)
        elif player_input[0] == "r":
            action = player.player_rewrite(player_input, current_character, current_map)
        elif player_input == "level text":
            action = text.level_text(current_character)
        else:
            action = ("////////////////////"
                      "Invalid Input,"
                      "/To move type 'w', 'a', 's', or 'd' then press enter"
                      "/To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                      "/to get help type 'help' then press enter"
                      "////////////////////")
        if type(action) != type("string"):
            levels.overwritten(current_map, mobs, current_character)
            for mob in mobs:
                if mob["alive"]:
                    for ai in mob["ai"]:
                        levels.ai_parse(mob, mobs, ai, current_map, current_character)
            for mob in mobs:
                if mob["alive"]:
                    if not (mob["name"] == "bullet" and
                            current_map[(mob["y_coordinate"], mob["x_coordinate"])] == input_color(" M ", "RED")):
                        map.rewrite(current_map, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
            levels.overwritten(current_map, [time_machine, current_character], current_character)
            if current_character["alive"]:
                print(map.map_art(map.display_text_next_to_map(
                    current_map, level_text, 0), current_character))
            else:
                print(player.how_died(current_map, current_character))
                break
        else:
            print(map.map_art(map.display_text_next_to_map(
                current_map, action, 0), current_character))
        achieved_goal = levels.check_level_goal(current_character, mobs)
        if achieved_goal:
            level_text = text.end_txt[current_character["level"] - 1]


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()