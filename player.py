import map
import random

def new_character():
    first_name = random.choice(["Chris", "Derek", "Peter", "Johnny", "Thomas"])
    last_name = random.choice(["Thompson", "The Axe Morgan", "The Wise", "Jefferson"])
    character_spread = {"name": first_name + " " + last_name, "health": 3, "x_coordinate": 0, "y_coordinate": 0}
    return character_spread


def parse(user_input, character, map_key):
    if user_input in ["n", "s", "e", "w", "north", "south", "east", "west"]:
        move(user_input, character, map_key)


def move(user_input, character, map_key):
    map.rewrite_spot(map_key, character["x_coordinate"], character["y_coordinate"], 1)
    if user_input[0] == "w":
        if character["x_coordinate"] - 1 in map_key[character["y_coordinate"]].keys():
            character["x_coordinate"] -= 1
    elif user_input[0] == "e":
        if character["x_coordinate"] + 1 in map_key[character["y_coordinate"]].keys():
            character["x_coordinate"] += 1
    elif user_input[0] == "s":
        if character["y_coordinate"] + 1 in map_key.keys():
            if character["x_coordinate"] in map_key[character["y_coordinate"] + 1].keys():
                character["y_coordinate"] += 1
    else:
        if character["y_coordinate"] - 1 in map_key.keys():
            if character["x_coordinate"] in map_key[character["y_coordinate"] - 1].keys():
                character["y_coordinate"] -= 1
    return character

