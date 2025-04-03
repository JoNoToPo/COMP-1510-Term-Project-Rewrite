import random
import map
import player
from text import input_color


def greater_grandfather():
    """
    Generates a greater grandfather that will either stay in place or move randomly.

    :precondition: none
    :postcondition: a dictionary
    :return: a dictionary with a random AI and unique id
    """
    number = 0
    while True:
        ai = random.choice(["move", "stay"])
        yield {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
               "symbol": input_color(" G ", "YELLOW"),
               "ai": [ai], "id": number}
        number += 1


def append_mobs(character):
    """
    Creates a list of mobs based on what level the player is.

    :precondition: a dictionary
    :postcondition: a list
    :param character: the player character dictionary with at least one key named 'level' with an integer value
    :return: a list containing dictionaries pertaining to the mobs in the level

    >>> append_mobs({"level": 0})
    []
    """
    if character["level"] == 1:
        return [{"name": "Dummy", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" D ", "RED"), "ai": ["stay"]},
                {"name": "Professor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" P ", "YELLOW"),
                 "ai": ["move"]}]
    elif character["level"] == 2:
        return [{"name": "Hitler", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" H ", "RED"),
                 "ai": ["move", "shoot"]},
                {"name": "Great-Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": ["move"], "id": 0},
                {"name": "Great-Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": ["move"], "id": 1}]
    elif character["level"] == 3:
        mob_list = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 50}]
        for _ in range(random.randrange(4, 8)):
            mob_list.append(next(greater_grandfather()))
        return mob_list
    elif character["level"] == 4:
        return [{"name": "GREATEST GRANDFATHER", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "WHITE", "BRIGHT_RED"),
                 "ai": ["move", "rewrite"], "area": 7}]
    else:
        return []


def check_level_goal(mobs: list):
    """
    Finds if the goal of a level has been completed.

    :precondition: two dictionaries
    :postconditon: a boolean value
    :param mobs: a list containing dictionaries each containing a key called 'alive' with a boolean value and a
    key called 'name' with a string value
    :return: the correct boolean value pertaining to whether the level goal has been achieved or not

    >>> check_level_goal({"level": 1}, [{"name": "name", "alive": False}])
    True
    >>> check_level_goal({"level": 5}, [{"name": "name", "alive": False}])
    False
    """
    for mob in mobs:
        if (mob["name"] == "meteor"
                or mob["name"] == "Hitler"
                or mob["name"] == "Dummy"
                or mob["name"] == "GREATEST GRANDFATHER"):
            return False
    return True


def overwritten(map_key: dict, mobs: list, character: dict):
    """
    Checks if a mob has been overwritten.

    :precondition: two dictionaries and a list of dictionaries
    :postconditon: a list of dictionaries
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param mobs: a list of dictionaries containing mob stats which are at minimum, the key strings "alive", "name",
     "y_coordinate", "x_coordinate", and "symbol"
    :param character: the dictionary containing the player character's stats
    :return: each mob dictionary in the mobs list modified correctly to have the value corresponding to whether or not
    they have been overwritten

    >>> map_test = {(0, 0): "anything"}
    >>> mob_list = [{"name": "bullet", "x_coordinate": 0, "y_coordinate": 0, "alive": True, "symbol": "B"}]
    >>> test_character = {"x_coordinate": 0, "y_coordinate": 0, "symbol": "C"}
    >>> overwritten(map_test, mob_list, test_character)
    >>> print(mob_list)
    []
    >>> mob_list = [{"name": "Time Machine", "x_coordinate": 0, "y_coordinate": 0, "alive": True, "symbol": "T"}]
    >>> overwritten(map_test, mob_list, test_character)
    >>> print(map_test)
    {(0, 0): 'T'}
    """
    for mob in mobs:
        if map_key[(mob["y_coordinate"], mob["x_coordinate"])] != mob["symbol"]:
            mob["alive"] = False
            happens_when_died(map_key, mob, mobs, character)


def happens_when_died(map_key: dict, mob: dict, mobs: list, character: dict):
    """
    Either kills the player or removes the mob depending on which mob died.

    :precondition: the dictionary for the map, the current mob dictionary, a list of mob dictionaries, and
    the player dictionary
    :postcondition: either the position or character overwritten with the name of the mob or the mob being removed from
    the mob list
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param mob: a dictionary within mobs containing mob stats which are at minimum, the key strings "name",
    "y_coordinate", "x_coordinate", and "symbol"
    :param mobs:a list of dictionaries containing mob stats which are at minimum, the key strings "name",
    "y_coordinate", "x_coordinate", and "symbol"
    :param character: the dictionary containing the player character's stats
    :return: the mob either being removed from the mobs list or overwrite the character's position in the map

    >>> map_test = {(0, 0): "anything"}
    >>> mob_list = [{"name": "bullet", "x_coordinate": 0, "y_coordinate": 0, "symbol": "B"}]
    >>> test_character = {"x_coordinate": 0, "y_coordinate": 0, "symbol": "C"}
    >>> happens_when_died(map_test, mob_list[0], mob_list, test_character)
    >>> print(mob_list)
    []
    >>> mob_list = [{"name": "Time Machine", "x_coordinate": 0, "y_coordinate": 0, "symbol": "T"}]
    >>> happens_when_died(map_test, mob_list[0], mob_list, test_character)
    >>> print(map_test)
    {(0, 0): 'T'}
    """
    if (mob["name"] == "bullet"
            or mob["name"] == "meteor"
            or mob["name"] == "Hitler"
            or mob["name"] == "Dummy"
            or mob["name"] == "GREATEST GRANDFATHER"):
        mobs.remove(mob)
    elif (mob["name"] == "Great-Grandfather"
          or mob["name"] == "Professor"
          or mob["name"] == f"{"Great-" * 500}Grandfather"):
        if map_key[(mob["y_coordinate"], mob["x_coordinate"])] == 3:
            map_key[(character["y_coordinate"], character["x_coordinate"])] = mob["name"]
        else:
            mobs.remove(mob)
    elif mob["name"] == "Time Machine":
        if map_key[(mob["y_coordinate"], mob["x_coordinate"])] == 3:
            map_key[(character["y_coordinate"], character["x_coordinate"])] = mob["name"]
        elif map_key[(mob["y_coordinate"], mob["x_coordinate"])] != character["symbol"]:
            mob["alive"] = True
            map_key[(mob["y_coordinate"], mob["x_coordinate"])] = mob["symbol"]


def countdown(mob: dict, map_key: dict, character: dict):
    mob["time left"] -= 1
    if mob["time left"] == 0:
        map_key[(character["y_coordinate"], character["x_coordinate"])] = "demolished by a meteor"


def fall(mob: dict, mobs: list, map_key: dict):
    """
    Create duplicate meteors in the map

    :precondition: two dictionaries and a list of dictionaries
    :postcondition: some number of meteors appended to the mob list in locations surrounding the first mob
    :param mob: the meteor dictionary
    :param mobs: a list of mob dictionaries
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    """
    if mob["time left"] == 50:
        placement_attempt = 0
        while placement_attempt < 20:
            place = [random.choice(range(-3, 3)), random.choice(range(-3, 3))]
            placement_attempt += 1
            if (mob["y_coordinate"] + place[1], mob["x_coordinate"] + place[0]) in map_key.keys():
                if ((map_key[(mob["y_coordinate"] + place[1], mob["x_coordinate"] + place[0])]
                     == input_color(" M ", "BRIGHT_RED")) or
                        map_key[(mob["y_coordinate"] + place[1], mob["x_coordinate"] + place[0])] == 3):
                    continue
            mobs.append({"name": "meteor", "x_coordinate": mob["x_coordinate"] + place[0],
                         "y_coordinate": mob["y_coordinate"] + place[1], "alive": True,
                         "symbol": input_color(" M ", "RED"), "id": placement_attempt,
                         "ai": ["countdown", "shoot"], "time left": 50})
            map.rewrite(map_key, mobs[-1]["x_coordinate"], mobs[-1]["y_coordinate"], mobs[-1]["symbol"])


def bullet(mob: dict, direction: tuple):
    """
    Generates a bullet next to the mob that fired it that will move in one direction

    :precondition: a dictionary and a list
    :postcondition: a dictionary
    :param mob: the mob dictionary that fired the bullet with at minimum the 'x_coordinate' and 'y_coordinate' keys
    :param direction: one of these four tuples ("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)
    """
    number = 0
    while True:
        yield {"name": "bullet", "x_coordinate": mob["x_coordinate"] + direction[0][1],
               "y_coordinate": mob["y_coordinate"] + direction[0][2], "alive": True,
               "symbol": input_color(" • ", "BRIGHT_RED"), "id": number,
               "ai": ["shot"], "direction": direction[0][0], "just_shot": True}
        number += 1


def shot(direction: str, character: dict, map_key: dict):
    """
    Moves a shot character in a given direction if it wasn't just shot, and it doesn't hit a barrier

    :precondition: a string and two dictionaries
    :postcondition: character dictionary modified
    :param direction: a string of either a, d, s, or w
    :param character: the dictionary of the character that was shot
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :return: True if the bullet can fly to that coordinate False if not

    >>> test_bullet = {"name": "bullet", "x_coordinate": 0, "y_coordinate": 0, "alive": True, "symbol": "B", "just_shot": False}
    >>> test_map = {(0, 0): "B"}
    >>> shot("d", test_bullet, test_map)
    >>> print(test_map)
    {(0, 0): '   '}
    >>> print(test_bullet["alive"])
    False
    """
    if not character["just_shot"]:
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"], "   ")
        if (direction[0] == "a"
                and authenticate_shot(character["x_coordinate"] - 1, character["y_coordinate"], map_key)):
            character["x_coordinate"] -= 1
        elif (direction[0] == "d"
              and authenticate_shot(character["x_coordinate"] + 1, character["y_coordinate"], map_key)):
            character["x_coordinate"] += 1
        elif (direction[0] == "s"
              and authenticate_shot(character["x_coordinate"], character["y_coordinate"] + 1, map_key)):
            character["y_coordinate"] += 1
        elif (direction[0] == "w"
              and authenticate_shot(character["x_coordinate"], character["y_coordinate"] - 1, map_key)):
            character["y_coordinate"] -= 1
        else:
            character["alive"] = False
    else:
        character["just_shot"] = False


def authenticate_shot(x_coordinate: int, y_coordinate: int, map_key: dict):
    """
    Checks to see if the place the bullet is flying to is blocked.

    :precondition: two integers and a dictionary
    :postcondition: a boolean value
    :param x_coordinate: an integer
    :param y_coordinate: an integer
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :return: True if the bullet can fly to that coordinate False if not

    >>> authenticate_shot(0, 0, {(0, 0): "anything_else"})
    True
    >>> authenticate_shot(0, 1, {(0, 0): "anything_else"})
    False
    """
    if player.authenticate_place(x_coordinate, y_coordinate, map_key):
        if (map_key[(y_coordinate, x_coordinate)] != 3 and
                map_key[(y_coordinate, x_coordinate)] != input_color(" M ", "RED")):
            return True
    return False
