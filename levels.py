import random
import map
import player
from text import input_color


def ai_parse(mob, mobs, current_map, current_character, amount_of_bullets, direction):
    """
    Parses between the different actions an ai can take

    :param mob: the mob in the mobs list that is acting
    :param mobs: a list containing dictionaries each containing a key called 'alive' with a boolean value and a
    key called 'name' with a string value
    :param current_map: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param current_character: the player character's dictionary
    :param amount_of_bullets: an integer greater than or equal to zero
    :param direction: one of these four options ("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)
    :precondition: three dictionaries, a list of dictionaries, an integer and a tuple of length three
    :postcondition: one dictionary
    :return: the correct function executed based on the ai of the mob
    """
    if mob["ai"][0] == "move":
        return player.move(direction[0], mob, current_map)
    elif (mob["ai"][0] == "shoot" and authenticate_shot(mob["x_coordinate"] + direction[1],
                                                        mob["y_coordinate"] + direction[2], current_map)):
        return shoot(direction, mobs, mob, amount_of_bullets)
    elif mob["ai"][0] == "shot":
        return shot(mob["direction"], mob, current_map)
    elif mob["ai"][0] == "fall":
        return fall(mob, mobs, current_map)
    elif mob["ai"][0] == "countdown":
        return countdown(mob, current_map, current_character)
    elif mob["ai"][0] == "rewrite":
        return player.player_rewrite(random.choice(["rw", "ra", "rs", "rd"]), mob, current_map)


def append_mobs(character):
    """
    Creates a list of mobs based on what level the player is.

    :param character: the player character dictionary with at least one key named 'level' with an integer value
    :precondition: a dictionary
    :postcondition: one list
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
                 "ai": ["shoot", "move"]},
                {"name": "Great-Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": ["move"], "id": 0},
                {"name": "Great-Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": ["move"], "id": 1}]
    elif character["level"] == 3:
        mob_list = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25}]
        for number in range(random.randrange(4, 8)):
            ai = random.choice(["move", "stay"])
            mob_list.append(
                {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": [ai], "id": number})
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

    :param mobs: a list containing dictionaries each containing a key called 'alive' with a boolean value and a
    key called 'name' with a string value
    :precondition: two dictionaries
    :postconditon: a boolean value
    :return: the correct boolean value pertaining to whether the level goal has been achieved or not

    >>> check_level_goal([{"name": "name"}])
    True
    >>> check_level_goal([{"name": "Hitler"}])
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

    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param mobs: a list of dictionaries containing mob stats which are at minimum, the key strings "alive", "name",
     "y_coordinate", "x_coordinate", and "symbol"
    :param character: a dictionary containing at minimum the key strings "y_coordinate", "x_coordinate" with integer values
    and "symbol" with a string value
    :precondition: two dictionaries and a list of dictionaries
    :postconditon: a list of dictionaries
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
    current_mob = 0
    while current_mob < len(mobs) and (mobs[current_mob]["alive"] == True or mobs[current_mob]["name"] == "bullet"):
        if ((mobs[current_mob]["y_coordinate"], mobs[current_mob]["x_coordinate"]) not in map_key.keys()
                or map_key[(mobs[current_mob]["y_coordinate"], mobs[current_mob]["x_coordinate"])]
                != mobs[current_mob]["symbol"]):
            happens_when_died(map_key, mobs[current_mob], mobs, character)
        else:
            current_mob += 1


def happens_when_died(map_key: dict, mob: dict, mobs: list, character: dict):
    """
    Either kills the player or removes the mob depending on which mob died.

    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param mob: a dictionary within mobs containing mob stats which are at minimum, the key strings "name",
    "y_coordinate", "x_coordinate", and "symbol"
    :param mobs:a list of dictionaries containing mob stats which are at minimum, the key strings "name",
    "y_coordinate", "x_coordinate", and "symbol"
    :param character: a dictionary containing at minimum the key strings "y_coordinate", "x_coordinate" with integer values
    and "symbol" with a string value
    :precondition: the dictionary for the map, the current mob dictionary, a list of mob dictionaries, and
    the player dictionary
    :postcondition: either the position or character overwritten with the name of the mob or the mob being removed from
    the mob list
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
    mob["alive"] = False
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
            map_key[(mob["y_coordinate"], mob["x_coordinate"])] = mob["symbol"]


def shoot(direction, mobs, mob, amount_of_bullets):
    mobs.append({"name": "bullet", "x_coordinate": mob["x_coordinate"] + direction[1],
                 "y_coordinate": mob["y_coordinate"] + direction[2], "alive": True,
                 "symbol": input_color(" • ", "BRIGHT_RED"), "id": amount_of_bullets,
                 "ai": ["shot"], "direction": direction[0], "just_shot": True})
    amount_of_bullets += 1


def countdown(mob, map_key, character):
    mob["time left"] -= 1
    if mob["time left"] < 1:
        map_key[(character["y_coordinate"], character["x_coordinate"])] = "demolished by a meteor"


def fall(mob: dict, mobs: list, map_key: dict):
    """
    Create duplicate meteors in the map

    :param mob: the meteor dictionary
    :param mobs: a list of mob dictionaries
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :precondition: two dictionaries and a list of dictionaries
    :postcondition: a list of dictionaries
    :return: 20 meteors appended to the mob list in locations surrounding the first mob
    """
    if mob["time left"] == 25:
        for meteor_id in range(20):
            place = [random.randrange(-3, 3), random.randrange(-3, 3)]
            if 30 < mob["y_coordinate"] + place[1] < 0 or 30 < mob["x_coordinate"] + place[0] < 0:
                continue
            mobs.append({"name": "meteor", "x_coordinate": mob["x_coordinate"] + place[0],
                         "y_coordinate": mob["y_coordinate"] + place[1], "alive": True,
                         "symbol": input_color(" M ", "RED"), "id": meteor_id,
                         "ai": ["countdown", "shoot"], "time left": 25})
            map.rewrite(map_key, mobs[-1]["x_coordinate"], mobs[-1]["y_coordinate"], mobs[-1]["symbol"])


def shot(direction: str, character: dict, map_key: dict):
    """
    Moves a shot character in a given direction if it wasn't just shot, and it doesn't hit a barrier

    :param direction: a string of either a, d, s, or w
    :param character: the dictionary of the character that was shot
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :precondition: a string and two dictionaries
    :postcondition: character dictionary modified
    :return: True if the bullet can fly to that coordinate False if not

    >>> test_bullet = {"name": "bullet", "x_coordinate": 0, "y_coordinate": 0, "alive": True, "symbol": "B", "just_shot": False}
    >>> test_map = {(0, 0): "B"}
    >>> shot("d", test_bullet, test_map)
    >>> print(test_map)
    {(0, 0): 'B'}
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
    if character["alive"] and authenticate_shot(character["x_coordinate"], character["y_coordinate"], map_key):
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"], character["symbol"])


def authenticate_shot(x_coordinate: int, y_coordinate: int, map_key: dict):
    """
    Checks to see if the place the bullet is flying to is blocked.

    :param x_coordinate: an integer
    :param y_coordinate: another integer
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :precondition: two integers and a dictionary
    :postcondition: a boolean value
    :return: True if the bullet can fly to that coordinate False if not

    >>> authenticate_shot(0, 0, {(0, 0): "anything_else"})
    True
    >>> authenticate_shot(0, 0, {})
    False
    """
    if (y_coordinate, x_coordinate) in map_key.keys():
        if (map_key[(y_coordinate, x_coordinate)] != 3
                and map_key[(y_coordinate, x_coordinate)] != input_color(" M ", "RED")
                and map_key[(y_coordinate, x_coordinate)] != input_color(" H ", "RED")):
            return True
    return False
