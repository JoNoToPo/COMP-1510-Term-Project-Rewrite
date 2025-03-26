import random
import initialize
import map
import player
from text import input_color


def check_level_goal(character, mobs):
    for mob in mobs:
        if mob["name"] == "meteor":
            return False
    if character["level"] <= 2 and mobs[0]["alive"] == False:
        return True
    if character["level"] == 3:
        return True
    if character["level"] == 4 and mobs[0]["alive"] == False:
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
    elif character["level"] == 2:
        return [{"name": "Hitler", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" H ", "RED"),
                 "ai": ["move", "shoot"]},
                {"name": "Great-Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": "stay"},
                {"name": "Great-Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": "stay"}
                ]
    elif character["level"] == 3:
        return [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" M ", "RED"),
                 "ai": ["fall", "countdown"], "time left": 50},
                {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": "stay"},
                {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": "stay"},
                {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "YELLOW"),
                 "ai": "stay"}]
    elif character["level"] == 4:
        return [{"name": "GREATEST GRANDFATHER", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                 "symbol": input_color(" G ", "BRIGHT_RED", "WHITE"),
                 "ai": ["move", "rewrite"], "level": 4}]
    else:
        return []


def overwritten(map_key, mobs, character):
    for mob in mobs:
        if map_key[(mob["y_coordinate"], mob["x_coordinate"])] != mob["symbol"]:
            mob["alive"] = False
            if mob["name"] == "bullet" or mob["name"] == "meteor":
                mobs.remove(mob)
            elif (mob["name"] == "Great-Grandfather"
                  or mob["name"] == "Great-Grandfather"
                  or mob["name"] == "Professor"
                  or mob["name"] == "Time Machine"
                  or mob["name"] == f"{"Great-" * 500}Grandfather"):
                if map_key[(mob["y_coordinate"], mob["x_coordinate"])] == 3:
                    map_key[(character["y_coordinate"], character["x_coordinate"])] = mob["name"]
                else:
                    mobs.remove(mob)


def mob_ai(mobs, map_key, character):
    overwritten(map_key, mobs, character)
    for mob in mobs:
        if mob["alive"]:
            for ai in mob["ai"]:
                if ai == "move":
                    player.move(random.choices(["w", "a", "s", "d"]), mob, map_key)
                    map.rewrite(map_key, mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
                if ai == "shoot" and random.random() > .5:
                    direction = random.choices([("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)])
                    mobs.append({"name": "bullet", "x_coordinate": mob["x_coordinate"] + direction[0][1],
                                 "y_coordinate": mob["y_coordinate"] + direction[0][2], "alive": True,
                                 "symbol": input_color(" • ", "BRIGHT_RED"),
                                 "ai": ["shot"], "direction": direction[0][0]})
                if ai == "shot":
                    shot(mob["direction"], mob, map_key)

                if (ai == "fall" and mob["time left"] == 48) or (ai == "fall" and mob["time left"] == 50):
                    direction = random.choice([random.choices([0, 1], k=2), random.choices([0, -1], k=2)])
                    try:
                        if (map_key[(mob["y_coordinate"] + direction[1], mob["x_coordinate"] + direction[0])] !=
                                input_color(" • ", "BRIGHT_RED")):
                            mobs.append({"name": "meteor", "x_coordinate": mob["x_coordinate"] + direction[0],
                                         "y_coordinate": mob["y_coordinate"] + direction[1], "alive": True,
                                         "symbol": input_color(" M ", "RED"),
                                         "ai": ["fall", "countdown"], "time left": 49})
                    except KeyError:
                        mobs.append({"name": "meteor", "x_coordinate": mob["x_coordinate"] + direction[0],
                                     "y_coordinate": mob["y_coordinate"] + direction[1], "alive": True,
                                     "symbol": input_color(" M ", "RED"),
                                     "ai": ["fall", "countdown"], "time left": 49})
                    for mob2 in mobs:
                        if mob2["alive"]:
                            map.rewrite(map_key, mob2["x_coordinate"], mob2["y_coordinate"],
                                        mob2["symbol"])
                if ai == "countdown":
                    mob["time left"] -= 1
                    if mob["time left"] == 0:
                        map_key[(character["y_coordinate"], character["x_coordinate"])] = "demolished by a meteor"
                if ai == "rewrite" and random.random() > .5:
                    player.player_rewrite(random.choice(["rw", "ra", "rs", "rd"]), mob, map_key)


def shot(direction: str, character: dict, map_key: dict):
    map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"], "   ")
    if (direction[0] == "a"
            and player.authenticate_place(character["x_coordinate"] - 1, character["y_coordinate"], map_key)):
        character["x_coordinate"] -= 1
    elif (direction[0] == "d"
          and player.authenticate_place(character["x_coordinate"] + 1, character["y_coordinate"], map_key)):
        character["x_coordinate"] += 1
    elif (direction[0] == "s"
          and player.authenticate_place(character["x_coordinate"], character["y_coordinate"] + 1, map_key)):
        character["y_coordinate"] += 1
    elif (direction[0] == "w"
          and player.authenticate_place(character["x_coordinate"], character["y_coordinate"] - 1, map_key)):
        character["y_coordinate"] -= 1
        map.rewrite(map_key, character["x_coordinate"], character["y_coordinate"], character["symbol"])

    return character


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