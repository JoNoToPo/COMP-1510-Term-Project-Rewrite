import map
import random
import text as t


def new_character():
    first_name = random.choice(["Chris", "Derek", "Peter", "Johnny", "Thomas"])
    last_name = random.choice(["Thompson", "The Axe Morgan", "The Wise", "Jefferson"])
    character_spread = {"name": first_name + " " + last_name, "level": 0, "x_coordinate": 0, "y_coordinate": 0, "alive": True}
    return character_spread


def parse(user_input, character: dict, map_key: dict, goal_achieved: bool):
    if user_input in ["w", "a", "s", "d"]:
        move(user_input, character, map_key, goal_achieved)
    elif user_input.split()[0] == "help":
        return player_help(user_input)
    elif user_input[0] == "r":
        player_rewrite(user_input, character, map_key)


def move(user_input: str, character: dict, map_key: dict, goal_achieved: bool):
    map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"],
                random.choices(["   ", " . "], [0.9, 0.1])[0])
    if user_input[0] == "a" and authenticate_move(character["x_coordinate"] - 1, character["y_coordinate"], map_key,
                                                  goal_achieved):
        character["x_coordinate"] -= 1
    elif user_input[0] == "d" and authenticate_move(character["x_coordinate"] + 1, character["y_coordinate"], map_key,
                                                    goal_achieved):
        character["x_coordinate"] += 1
    elif user_input[0] == "s" and authenticate_move(character["x_coordinate"], character["y_coordinate"] + 1, map_key,
                                                    goal_achieved):
        character["y_coordinate"] += 1
    elif user_input[0] == "w" and authenticate_move(character["x_coordinate"], character["y_coordinate"] - 1, map_key,
                                                    goal_achieved):
        character["y_coordinate"] -= 1
    map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"],
                " @ ")
    return character

def authenticate_place(x_coordinate: int, y_coordinate: int, map_key: dict):
    if (y_coordinate, x_coordinate) in map_key.keys():
        return True
    return False


def authenticate_move(x_coordinate: int, y_coordinate: int, map_key: dict, goal_achieved: bool):
    if authenticate_place(x_coordinate, y_coordinate, map_key):
        if map_key[(y_coordinate, x_coordinate)] == "   " or " . ":
            return True
        if goal_achieved:
            if map_key[(y_coordinate, x_coordinate)] == " T ":
                return True
    return False


def player_help(user_input: str) -> str:
    if user_input == "help":
        output = t.line + t.help
    if user_input == "help" + "w" or "a" or "s" or "d":
        output = t.line + t.help
    return output


def player_rewrite(user_input: str, character: dict, map_key: dict):
    area = character["level"] * 2 - 1
    try:
        direction = user_input.split()[1][0]
    except IndexError:
        direction = user_input[1]
    if direction == "a":
        map.rewrite(map_key, character["x_coordinate"] - (int(area / 2) + 1), character["y_coordinate"], 3, area)
    elif direction == "d":
        map.rewrite(map_key, character["x_coordinate"] + (int(area / 2) + 1), character["y_coordinate"], 3, area)
    elif direction == "s":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] + (int(area / 2) + 1), 3, area)
    elif direction == "w":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] - (int(area / 2) + 1), 3, area)
    else:
        print("invalid input")