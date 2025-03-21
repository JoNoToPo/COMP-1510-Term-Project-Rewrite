def check_level_goal(character, enemies):
    if character["level"] == 1 and enemies == []:
        return True
    else:
        return False


def append_enemies(character):
    if character["level"] == 1:
        return []
    if character["level"] == 2:
        return [{"name": "Hitler", "x_coordinate": 0, "y_coordinate": 0, "content": " H ", "alive": False}]


def overwritten(map_key, *mobs):
    for mob in mobs:
        if map_key[(mob["x_coordinate"], mob["y_coordinate"])] == mob["content"]:
            mob["alive"] = False