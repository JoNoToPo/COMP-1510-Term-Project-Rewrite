import map
import random
import text as t
from text import input_color


def new_character():
    first_name = random.choice(["Chris", "Derek", "Peter", "Johnny", "Thomas"])
    last_name = random.choice(["Thompson", "The Axe Morgan", "The Wise", "Jefferson"])
    character_spread = {"name": first_name + " " + last_name, "level": 0, "x_coordinate": 0, "y_coordinate": 0,
                        "alive": True, "symbol": input_color(" @ ", "GREEN")}
    return character_spread


def parse(user_input, character: dict, map_key: dict, goal_achieved: bool):
    if user_input in ["w", "a", "s", "d"]:
        move(user_input, character, map_key, goal_achieved)
    elif user_input.split()[0] == "help":
        return player_help(user_input)
    elif user_input[0] == "r":
        player_rewrite(user_input, character, map_key)


def move(user_input: str, character: dict, map_key: dict, goal_achieved=True):
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
                character["symbol"])
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
        direction = user_input[1]
    except IndexError:
        direction = None
    try:
        direction = user_input.split()[1][0]
    except IndexError:
        pass
    if direction == "a":
        map.rewrite(map_key, character["x_coordinate"] - (int(area / 2) + 1), character["y_coordinate"], 3, area)
    elif direction == "d":
        map.rewrite(map_key, character["x_coordinate"] + (int(area / 2) + 1), character["y_coordinate"], 3, area)
    elif direction == "s":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] + (int(area / 2) + 1), 3, area)
    elif direction == "w":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] - (int(area / 2) + 1), 3, area)
    else:
        print("After 'r' please specify the direction you want to rewrite, 'w', 'a', 's', or 'd'")

def how_died(map_key, character):
    """
    Finds how the character.

    :precondition: two dictionaries
    :postcondition: a string
    :param map_key: a dictionary containing tuples of the room coordinates as the keys and a string of the contents
    as the value
    :param character: a dictionary containing at least two keys called Y-coordinate and X-coordinate corresponding to
    the location of the character
    :return: a string corresponding to what killed the chaacter

    >>> print(how_died({(0, 0): input_color(' • ', 'RED')}, {"x_coordinate": 0, "y_coordinate": 0}))
    You got shot
    Game Over
    """
    place = map_key[(character["y_coordinate"], character["x_coordinate"])]
    if place == "   " or place == " . ":
        return "you are the floor now"
    if place == input_color(" • ", "RED"):
        return ("You got shot "
                "\nGame Over")
    if place == input_color(" H ", "RED"):
        return ("Hitler pulls out a knife and stabs you "
                "\nGame Over")
    if place == 3:
        return ("Your conciousness fragments over dfferent parts of history "
                "\nand for a brief moment you feel like you understand everything. "
                "\nBut just as quickly as that understanding comes, "
                "\nYour mind breaks from the information overload and you drift into unconsiousness "
                "\nGame Over")