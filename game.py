import map
import initialize as i
import player
import text
import text as t
import levels
from text import input_color
import random


def game():
    """
    Drive the game
    """
    achieved_goal = True
    current_character = player.new_character()
    time_machine = {"name": "Time Machine", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                    "symbol": input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}
    time_in_level = 0
    current_map = {}
    mobs = []
    level_text = ""
    amount_of_bullets = 0
    while True:
        if achieved_goal:
            print(f"to continue to the next level please proceed to the time machine "
                  f"\"{input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}\"")
            if (current_character["y_coordinate"] == time_machine["y_coordinate"] and
                    current_character["x_coordinate"] == time_machine["x_coordinate"]):
                current_character["level"] += 1
                current_character["area"] += 2
                start_room = i.room_randomizer(8 + current_character["level"], 4 + current_character["level"])
                i.initialize_mob(time_machine, start_room, {(0, 0): 1})
                current_character["y_coordinate"] = time_machine["y_coordinate"]
                current_character["x_coordinate"] = time_machine["x_coordinate"]
                if current_character["level"] == 5:
                    print(f"\n\n\n\n\n"
                          f"{f"{input_color(" ", "BRIGHT_BLUE", "BRIGHT_BLUE")}" * 53}"
                          f"\n,--.   ,--.                 ,--.   ,--.,--.         "
                          f"\n \\  `.'  /,---. ,--.,--.    |  |   |  |`--',--,--,  "
                          f"\n  '.    /| .-. ||  ||  |    |  |.'.|  |,--.|      \\ "
                          f"\n    |  | ' '-' ''  ''  '    |   ,'.   ||  ||  ||  | "
                          f"\n    `--'  `---'  `----'     '--'   '--'`--'`--''--' "
                          f"\n{f"{input_color(" ", "BRIGHT_BLUE", "BRIGHT_BLUE")}" * 53}"
                          f"\n\nYou enter the time machine and realize"
                          f"{random.choice(["\n... Now that you think about it, you didn't need to rewrite history at all"
                                            "\nyou thought that you would make your mark on history but it turns out that "
                                            "\nyou just destroyed reality, and that really sucks."
                                            "\n... maybe in another timeline things could have been different..."
                                            "\n [You go the Depressed ending]",
                                            "\nWith this time machine and rewriting device "
                                            "\nyou can now reshape history however you would like"
                                            "\nThis is just the beginning and the world will be written in your image."
                                            "\n[You got the Playing God ending]",
                                            "\n... nothing. You try to think of a satisfying conclusion to all of this madness,"
                                            "\nbut nothing comes to mind. a bunch of random stuff happened and you have no clue why."
                                            "\n[You got the Confused ending]"])} "
                          f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThank you Chris for playing the game and making a fun assignment, please give me a good grade lol")
                    break
                current_map = i.starting_map(start_room, 8, 4, current_character["level"] + 1)
                map.rewrite(start_room, current_character["x_coordinate"], current_character["y_coordinate"],
                            current_character["symbol"])
                mobs = levels.append_mobs(current_character)
                for mob in mobs:
                    i.initialize_mob(mob, current_map, start_room)
                    map.rewrite(current_map, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
                level_text = t.level_text(current_character)
                print(map.level_start_display(level_text))
                input("To play, please make any input:")
                time_in_level = 0
                achieved_goal = False
                print(map.map_art(map.display_text_next_to_map(current_map, level_text, 0), current_character))
        player_input = str(
            input(f"{time_in_level} seconds spent in level.\nMove with 'w', 'a', 's', or 'd'")).strip().lower()
        time_in_level += 1
        try:
            action = player.player_parse(player_input, current_character, current_map, achieved_goal)
        except IndexError:
            action = ("///////////"
                      "Invalid Input,"
                      "//To move type 'w', 'a', 's', or 'd' then press enter"
                      "//To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                      "//to get help type 'help' then press enter"
                      "///////////")
        if type(action) != type("string"):
            levels.overwritten(current_map, mobs, current_character)
            for mob in mobs:
                levels.ai_parse(mob, mobs, current_map, current_character, amount_of_bullets,
                                random.choice([("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)]))
                if len(mob["ai"]) == 2:
                    mob["ai"] = [mob["ai"][1], mob["ai"][0]]
            achieved_goal = levels.check_level_goal(mobs)
            if achieved_goal:
                level_text = text.end_txt(current_character)
            levels.overwritten(current_map, [time_machine, current_character], current_character)
            time_machine["alive"] = True
            if current_character["alive"]:
                print(map.map_art(map.display_text_next_to_map(
                    current_map, level_text, 0), current_character))
            else:
                print(player.how_died(current_map, current_character))
                break
        else:
            print(map.map_art(map.display_text_next_to_map(
                current_map, action, 0), current_character))


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()