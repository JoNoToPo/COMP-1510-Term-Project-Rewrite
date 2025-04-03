import map
import random
import text
from text import input_color


def new_character():
    """
    Initializes the player character and gives a random name.

    :precondition: none
    :postcondition: a dictionary
    :return: a dictionary containing the player's stats and a randomized name
    """
    first_name = random.choice(["Chris", "Derek", "Peter", "Johnny", "Thomas"])
    last_name = random.choice(["Thompson", "\"The Axe\" Morgan", "The Wise", "Jefferson"])
    character_spread = {"name": first_name + " " + last_name, "level": 0, "area": -1, "x_coordinate": 0,
                        "y_coordinate": 0, "alive": True, "symbol": input_color(" @ ", "GREEN", )}
    return character_spread


def move(user_input: str, character: dict, map_key: dict, goal_achieved=True):
    """

    """
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
            if map_key[(y_coordinate, x_coordinate)] == input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE"):
                return True
    return False


def player_rewrite(user_input: str, character: dict, map_key: dict):
    direction = None
    if len(user_input) > 1:
        direction = user_input[1]
    if len(user_input.split()) > 1:
        direction = user_input.split()[1][0]
    if direction == "a":
        map.rewrite(map_key, character["x_coordinate"] - (int(character["area"] / 2) + 1),
                    character["y_coordinate"], 3, character["area"])
    elif direction == "d":
        map.rewrite(map_key, character["x_coordinate"] + (int(character["area"] / 2) + 1),
                    character["y_coordinate"], 3, character["area"])
    elif direction == "s":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] + (int(character["area"] / 2) + 1),
                    3, character["area"])
    elif direction == "w":
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"] - (int(character["area"] / 2) + 1),
                    3, character["area"])
    else:
        return ("/////////////to rewrite, After typing 'r' please specify the "
                "/direction you want to rewrite, 'w', 'a', 's', or 'd'"
                "//Examples:/to rewrite up type 'rw' then press enter/to rewrite left type 'ra' then press enter/"
                "to rewrite down type 'rs' then press enter/to rewrite left type 'rd' then press enter//////////////////")


def how_died(map_key: dict, character: dict):
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
    you_died = (f",--.   ,--.                 ,------.  ,--.          ,--. "
                f"\n \\  `.'  /,---. ,--.,--.    |  .-.  \\ `--' ,---.  ,-|  | "
                f"\n  '.    /| .-. ||  ||  |    |  |  \\  :,--.| .-. :' .-. | "
                f"\n    |  | ' '-' ''  ''  '    |  '--'  /|  |\\   --.\\ `-' | "
                f"\n    `--'  `---'  `----'     `-------' `--' `----' `---'  ")
    killed_friendly = "You look at your hand as it becomes transparent. \nThe rewrite device in your hand clatters to the ground."
    if not place:
        return (f"\n{you_died}"
                "\nYou somehow became a wall."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "   " or place == " . ":
        return (f"\n{you_died}"
                "\nYou are the floor now?"
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == input_color(" • ", "BRIGHT_RED"):
        return (f"\n{you_died}"
                "\nWhether by a bullet or a shard of rock, the result is the same."
                "\nYou got shot."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == input_color(" H ", "RED"):
        return ("Hitler pulls out a knife and stabs you."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == 3:
        return (f"\n{you_died}"
                "\n\nThrough the distortions and tears in reality, "
                "\nyou see The man point his device at you and pulls the trigger"
                "\n"
                "\nYour consciousness fragments over different parts of history "
                "\nand for a brief moment you feel like you understand everything. "
                "\n\nBut just as quickly as that understanding comes, "
                "\nYour mind breaks from the information overload and you drift into unconsciousness."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "demolished by a meteor":
        return (f"\n{you_died}"
                "\n\nThe last thing you see is the meteor crashing down onto the planet right above your head."
                "\nYou don't even feel the impact, as you are blotted out by a fireball that outshines the sun."
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "Great-Grandfather":
        return (f"\n{you_died}"
                f"\n\nUnderestimating the power of the rewrite device"
                f"\nyou accidentally rewrite a random student"
                f"\n{text.with_a_random_thing_from_history}"
                f"\n{killed_friendly}"
                f"\noops you killed one of your Great-Grandfathers."
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "Time Machine":
        return (f"\n{you_died}"
                f"\n\nThrough the power of the rewrite device"
                f"\nyour time machine is rewritten"
                f"\n{text.with_a_random_thing_from_history}"
                f"\n{killed_friendly}"
                f"\n\noops your time machine was destroyed."
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == f"{"Great-" * 500}Grandfather":
        return (f"\n{you_died}"
                f"\n\nUnderestimating the power of the rewrite device"
                f"\nyou accidentally rewrite a caveman"
                f"\n{text.with_a_random_thing_from_history}"
                f"\n{killed_friendly}"
                f"\nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooops "
                f"\nyou killed one of your \n{"Great-" * 500}Grandfathers."
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
    elif place == "Professor":
        return (f"\n{you_died}"
                f"\n\nUsing the device that HE GAVE YOU, you replace him"
                f"\n{text.with_a_random_thing_from_history}"
                f"\n{killed_friendly}"
                f"\nWoah maybe this professor is more than he seems?"
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over")
