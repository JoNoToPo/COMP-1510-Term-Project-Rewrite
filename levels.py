import random

import initialize
import map
import player
from text import input_color



def check_level_goal(character, mobs):
    if character["level"] == 1 and mobs[0]["alive"] == False:
        return True
    if character["level"] == 2 and mobs[0]["alive"] == False:
        return True
    else:
        return False


def append_mobs(character):
    if character["level"] == 1:
        return [{"name": "Dummy", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" D ", "RED"), "ai": "stay"},
                {"name": "Professor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" P ", "YELLOW"),
                 "ai": "stay"}]
    if character["level"] == 2:
        return [{"name": "Hitler", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" H ", "RED"),
                 "ai": ["move", "shoot"]}]


def overwritten(map_key, mobs):
    for mob in mobs:
        if map_key[(mob["y_coordinate"], mob["x_coordinate"])] != mob["symbol"]:
            mob["alive"] = False
            if mob["name"] == "bullet":
                mobs.remove(mob)


def mob_ai(mobs, map_key):
    overwritten(map_key, mobs)
    for mob in mobs:
        if mob["alive"]:
            for ai in mob["ai"]:
                if ai == "move":
                    player.move(random.choices(["w", "a", "s", "d"]), mob, map_key)
                if ai == "shoot" and random.random() > .5:
                    direction = random.choices([("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)])
                    mobs.append({"name": "bullet", "x_coordinate": mob["x_coordinate"] + direction[0][1],
                                 "y_coordinate": mob["y_coordinate"] + direction[0][2], "alive": True,
                                 "symbol": input_color(" • ", "RED"),
                                 "ai": ["shot"], "direction": direction[0][0]})
                if ai == "shot":
                    mob["direction"]
                    player.move(mob["direction"], mob, map_key)
                    map.rewrite(map_key, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
            map.rewrite(map_key, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])


def main():
    """
    Drive the program
    """
    character = {"level": 2}
    mobs = append_mobs(character)
    maper = {(0, 0): "anything", (0, 1): "anything", (1, 0): "anything", (1, 1): "anything", (1, 2): "anything",
             (2, 1): "anything", }
    initialize.initialize_mob(mobs[0], maper)
    for mob in mobs:
        map.rewrite(maper, mob, mob["x_coordinate"], mob["y_coordinate"])
    mob_ai(mobs, maper)
    print(mobs)

if __name__ == "__main__":
    main()