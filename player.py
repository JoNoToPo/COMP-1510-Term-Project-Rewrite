import map
import random


def new_character():
    first_name = random.choice(["Chris", "Derek", "Peter", "Johnny", "Thomas"])
    last_name = random.choice(["Thompson", "The Axe Morgan", "The Wise", "Jefferson"])
    character_spread = {"name": first_name + " " + last_name, "level": 2, "x_coordinate": 0, "y_coordinate": 0}
    return character_spread


def parse(user_input, character, map_key):
    if user_input in ["n", "s", "e", "w", "north", "south", "east", "west"]:
        move(user_input, character, map_key)
    elif user_input == "help":
        return player_help(user_input)
    elif user_input[0] == "r":
        player_rewrite(user_input, character, map_key)


def move(user_input, character, map_key):
    map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"],
                random.choices(["   ", " . "], [0.9, 0.1])[0], 1)
    if user_input[0] == "w":
        if authenticate_move(character["x_coordinate"] - 1, character["y_coordinate"], map_key):
            character["x_coordinate"] -= 1
    elif user_input[0] == "e":
        if authenticate_move(character["x_coordinate"] + 1, character["y_coordinate"], map_key):
            character["x_coordinate"] += 1
    elif user_input[0] == "s":
        if authenticate_move(character["x_coordinate"], character["y_coordinate"] + 1, map_key):
            character["y_coordinate"] += 1
    else:
        if character["y_coordinate"] - 1 in map_key.keys():
            if authenticate_move(character["x_coordinate"], character["y_coordinate"] - 1, map_key):
                character["y_coordinate"] -= 1
    return character

def authenticate_place(x_coordinate, y_coordinate, map_key):
    if (y_coordinate, x_coordinate) in map_key.keys():
        return True
    return False


def authenticate_move(x_coordinate, y_coordinate, map_key):
    if authenticate_place(x_coordinate, y_coordinate, map_key):
        if map_key[(y_coordinate, x_coordinate)] == "   " or " . ":
            return True
    return False


def player_help(user_input):
    if user_input == "help":
        output = ("-" * 53 +
                  "/,--.  ,--.       ,--.           "
                  "/|  '--'  | ,---. |  | ,---.     "
                  "/|  .--.  || .-. :|  || .-. |    "
                  "/|  |  |  |\\   --.|  || '-' '    "
                  "/`--'  `--' `----'`--'|  |-'     "
                  "/---------------------`--'----------------------------/"
                  "//Insert helptext here")
        return output


def player_rewrite(user_input, character, map_key):
    area = character["level"] * 2 - 1
    if user_input.split()[1][0] == "w":
        map.rewrite(map_key, character["x_coordinate"] - (int(area / 2) + 1), character["y_coordinate"], 3, area)
    elif user_input.split()[1][0] == "e":
        map.rewrite(map_key, character["x_coordinate"] + (int(area / 2) + 1), character["y_coordinate"], 3, area)
    elif user_input.split()[1][0] == "s":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] + (int(area / 2) + 1), 3, area)
    else:
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] - (int(area / 2) + 1), 3, area)