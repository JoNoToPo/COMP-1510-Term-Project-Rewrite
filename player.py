import map


def parse(user_input, character, map_key):
    if user_input in ["n", "s", "e", "w", "north", "south", "east", "west"]:
        move(user_input, character, map_key)




def move(user_input, character, map_key):
    map.player_move_from(map_key, character["x_coordinate"], character["y_coordinate"])
    if user_input == "w":
        character["x_coordinate"] -= 1
    elif user_input == "e":
        character["x_coordinate"] += 1
    elif user_input == "s":
        character["y_coordinate"] += 1
    else:
        character["y_coordinate"] -= 1
    return character

