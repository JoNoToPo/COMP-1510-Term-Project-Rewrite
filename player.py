import map
import random

import text
import text as t
from text import input_color


def new_character():
    first_name = random.choice(["Chris", "Derek", "Peter", "Johnny", "Thomas"])
    last_name = random.choice(["Thompson", "The Axe Morgan", "The Wise", "Jefferson"])
    character_spread = {"name": first_name + " " + last_name, "level": 3, "x_coordinate": 0, "y_coordinate": 0,
                        "alive": True, "symbol": input_color(" @ ", "GREEN")}
    return character_spread


def parse(user_input, character: dict, map_key: dict, goal_achieved: bool):
    if user_input in ["w", "a", "s", "d"]:
        move(user_input, character, map_key, goal_achieved)
    elif user_input.split()[0] == "help":
        return player_help(user_input)
    elif user_input[0] == "r":
        player_rewrite(user_input, character, map_key)
    elif user_input.lower().strip() == "level text":
        return text.level_text(character)


def move(user_input: str, character: dict, map_key: dict, goal_achieved=True):
    map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"],
                "   ")
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
        if map_key[(y_coordinate, x_coordinate)] == "   ":
            return True
        if goal_achieved:
            if map_key[(y_coordinate, x_coordinate)] == input_color(" T ", "BRIGHT_BLUE", "DARK_GRAY"):
                return True
    return False


def player_help(user_input: str) -> str:
    output = ""
    if user_input == "help":
        output = t.line + t.help_text
    if user_input == "help" + "w" or "a" or "s" or "d":
        output = t.line + t.help_text
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

    >>> print(how_died({(0, 0): input_color(' • ', 'BRIGHT_RED')}, {"x_coordinate": 0, "y_coordinate": 0}))
    Whether by a bullet or a shard of rock, the result is the same.
    You got shot.
    Game Over
    """
    place = map_key[(character["y_coordinate"], character["x_coordinate"])]
    if not place:
        return (f"\n{you_died}"
                "\nYou somehow became a wall."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "   " or place == " . ":
        return (f"\n{you_died}"
                "\nYou are the floor now?"
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == input_color(" • ", "BRIGHT_RED"):
        return (f"\n{you_died}"
                "\nWhether by a bullet or a shard of rock, the result is the same."
                "\nYou got shot."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == input_color(" H ", "RED"):
        return ("Hitler pulls out a knife and stabs you."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == 3:
        return (f"\n{you_died}"
                "\nYour consciousness fragments over different parts of history "
                "\nand for a brief moment you feel like you understand everything. "
                "\nBut just as quickly as that understanding comes, "
                "\nYour mind breaks from the information overload and you drift into unconsciousness."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "demolished by a meteor":
        return (f"\n{you_died}"
                "\nThe last thing you see is the meteor crashing down onto the planet right above your head."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "Great-Grandfather":
        return (f"\n{you_died}"
                f"\n\n{killed_freindly}"
                "\noops you killed one of your Great-Grandfathers."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "Time Machine":
        return (f"\n{you_died}"
                f"\n\n{killed_freindly}"
                f"\noops you destroyed your time machine."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == f"{"Great-" * 500}Grandfather":
        return (f"\n{you_died}"
                f"\n\n{killed_freindly}"
                f"\nooops you killed one of your {"Great-" * 500}Grandfather."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")

killed_freindly = "You look at your hand as it becomes transparent. \nThe rewrite device in your hand clatters to the ground."
you_died = (f",--.   ,--.                 ,------.  ,--.          ,--. "
            f"\n \  `.'  /,---. ,--.,--.    |  .-.  \ `--' ,---.  ,-|  | "
            f"\n  '.    /| .-. ||  ||  |    |  |  \  :,--.| .-. :' .-. | "
            f"\n    |  | ' '-' ''  ''  '    |  '--'  /|  |\   --.\ `-' | "
            f"\n    `--'  `---'  `----'     `-------' `--' `----' `---'  ")