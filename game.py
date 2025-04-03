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
    current_map = {}
    mobs = []
    level_text = ""
    bullet_generator = levels.bullet
    while True:
        if achieved_goal:
            print(f"to continue to the next level please proceed to the time machine "
                  f"\"{input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}\"")
            if (current_character["y_coordinate"] == time_machine["y_coordinate"] and
                    current_character["x_coordinate"] == time_machine["x_coordinate"]):
                current_character["level"] += 1
                current_character["area"] += 2
                if current_character["level"] == 5:
                    print(f"\n\n\n\n\n\n,--.   ,--.                 ,--.   ,--.,--.         "
                          f"\n \\  `.'  /,---. ,--.,--.    |  |   |  |`--',--,--,  "
                          f"\n  '.    /| .-. ||  ||  |    |  |.'.|  |,--.|      \\ "
                          f"\n    |  | ' '-' ''  ''  '    |   ,'.   ||  ||  ||  | "
                          f"\n    `--'  `---'  `----'     '--'   '--'`--'`--''--' "
                          f"\n\n\n\n\n\n\n\n\n\nYou enter the time machine and realize"
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
                          f"\n\n\n\n\n\nThank you Chris for playing the game and making a fun assignment, please give me a good grade lol")
                    break
                start_room = i.room_randomizer(8 + current_character["level"], 4 + current_character["level"])
                i.initialize_mob(time_machine, start_room, {(0, 0): 1})
                current_character["y_coordinate"] = time_machine["y_coordinate"]
                current_character["x_coordinate"] = time_machine["x_coordinate"]
                current_map = i.starting_map(start_room, 8, 4, current_character["level"] + 1)
                map.rewrite(current_map, current_character["x_coordinate"], current_character["y_coordinate"],
                            current_character["symbol"])
                mobs = levels.append_mobs(current_character)
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
        if not player_input:
            action = ("///////////"
                      "Invalid Input,"
                      "//To move type 'w', 'a', 's', or 'd' then press enter"
                      "//To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                      "//to get help type 'help' then press enter"
                      "///////////")
        elif player_input.split()[0] == "help":
            action = (f"{"-" * 53}"
                      "/             ,--.  ,--.       ,--.           "
                      "/             |  '--'  | ,---. |  | ,---.     "
                      "/             |  .--.  || .-. :|  || .-. |    "
                      "/             |  |  |  |\\   --.|  || '-' '    "
                      "/             `--'  `--' `----'`--'|  |-'     "
                      "/----------------------------------`--'---------------/"
                      "/Welcome to Rewrite!"
                      "/To move use 'w' to move up, 'a' to move left "
                      "/'s' to move down and 'd' to move right then press enter."
                      "//To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                      "/for a more complete guide on rewriting simply type 'r' and enter"
                      "//Once anything is rewritten it will display as a corrupted tile."
                      "/corrupted tiles change your perception of reality, and act as barriers."
                      "/however the space surrounding remains the same even if it looks different."
                      "/if you rewrite a corrupted tile, "
                      "/it is erased from existence leaving "
                      "/nothing but floor behind."
                      "/Be careful what you rewrite. You could end up "
                      "/erasing yourself from existence if you are not careful."
                      "/after you are finished with the goal in a level,"
                      "/move to the time machine ' T ' and you will continue the story.")
        elif player_input[0] in ["w", "a", "s", "d"]:
            player.move(player_input, current_character, current_map, achieved_goal)
        elif player_input[0] == "r":
            action = player.player_rewrite(player_input, current_character, current_map)
        elif player_input == "level text":
            action = text.level_text(current_character)
        else:
            action = ("//////////"
                      "Invalid Input,"
                      "//To move type 'w', 'a', 's', or 'd' then press enter"
                      "//To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                      "//to get help type 'help' then press enter"
                      "//////////")
        if type(action) != type("string"):
            levels.overwritten(current_map, mobs, current_character)
            for mob in mobs:
                for ai in mob["ai"]:
                    direction = random.choice([("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)])
                    if ai == "cycle":
                        mob["ai"] = random.choice([["move", "cycle"], ["shoot", "cycle"]])
                    if ai == "move":
                        player.move(direction[0], mob, current_map)
                    if (ai == "shoot" and random.random() > .3
                            and levels.authenticate_shot(mob["x_coordinate"] + direction[1],
                                                         mob["y_coordinate"] + direction[2], current_map)):
                        mobs.append(next(bullet_generator(mob, direction)))
                    if ai == "shot":
                        levels.shot(mob["direction"], mob, current_map)
                        if (mob["alive"]
                                and levels.authenticate_shot(mob["x_coordinate"] - 1, mob["y_coordinate"],
                                                             current_map)):
                            map.rewrite(current_map, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
                    if ai == "fall":
                        levels.fall(mob, mobs, current_map)
                    if ai == "countdown":
                        levels.countdown(mob, current_map, current_character)
                    if ai == "rewrite" and random.random() > .5:
                        player.player_rewrite(random.choice(["rw", "ra", "rs", "rd"]), mob, current_map)
            achieved_goal = levels.check_level_goal(mobs)
            if achieved_goal:
                level_text = text.end_txt(current_character)
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


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()