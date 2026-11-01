"""
Browser version of Rewrite.

Runs inside Pyodide (see index.html). Instead of waiting for input() the page calls tick() three times a second with
the direction key being held (or tapped since the last tick), or None. Time only passes while a direction is held:
standing still freezes the world.
"""

import io
import random
from contextlib import redirect_stdout

import map
import initialize as i
import player
import text as t
import levels
import timeline
from text import input_color

TICKS_PER_SECOND = 3

HELP_TEXT = ("///////////HELP"
             "//Hold 'w', 'a', 's', or 'd' to move."
             "/Time only moves while you hold a direction."
             "//Press 'r' then 'w', 'a', 's', or 'd'"
             "/to rewrite once in that direction."
             "/Press 'r' again to cancel the rewrite."
             "//Rewriting a floor makes a corrupted wall,"
             "/rewriting a corrupted wall turns it back into floor."
             "//Press 'h' to close this help."
             "///////////")


def new_game():
    """
    Creates the state of a fresh game.

    :precondition: none
    :postcondition: a dictionary
    :return: a dictionary holding everything the game loop needs between ticks
    """
    return {"phase": "travel", "character": player.new_character(timeline.load_timeline()),
            "time_machine": {"name": "Time Machine", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                             "symbol": input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")},
            "map": {}, "mobs": [], "level_text": "", "achieved_goal": True, "ticks": 0,
            "rewrite_mode": False, "help": False, "screen": ""}


def start_level(state: dict):
    """
    Levels up the player and builds the next level.

    :param state: the game state dictionary
    :precondition: a game state dictionary with the player standing on the time machine
    :postcondition: the game state modified to be at the start of the next level
    """
    character = state["character"]
    time_machine = state["time_machine"]
    timeline.rewrite_history(character)
    start_room = i.room_randomizer(8 + character["level"] + 1, 4 + character["level"])
    i.initialize_mob(time_machine, start_room, {(0, 0): 1})
    i.initialize_player(character, time_machine)
    if character["level"] == 5:
        output = io.StringIO()
        with redirect_stdout(output):
            t.you_win()
        state["phase"] = "over"
        state["screen"] = output.getvalue() + "\n\n  Press space to play again."
        return
    state["map"] = i.starting_map(start_room, 8, 4, character["level"] + 1)
    map.rewrite(state["map"], character["x_coordinate"], character["y_coordinate"], character["symbol"])
    state["mobs"] = levels.append_mobs(character)
    for mob in state["mobs"]:
        i.initialize_mob(mob, state["map"], start_room)
        map.rewrite(state["map"], mob["x_coordinate"], mob["y_coordinate"], mob["symbol"])
    if character["level"] == 1:
        dummy, professor = state["mobs"]
        i.block_corridor(professor, state["map"], start_room, (character["y_coordinate"], character["x_coordinate"]),
                         (dummy["y_coordinate"], dummy["x_coordinate"]))
    state["level_text"] = t.level_text(character)
    state["achieved_goal"] = False
    state["rewrite_mode"] = False
    state["ticks"] = 0
    state["phase"] = "intro"
    state["screen"] = map.level_start_display(state["level_text"]) + "\n  Press space to play."


def player_action(state: dict, key: str):
    """
    Moves or rewrites in the direction the player is holding.

    :param state: the game state dictionary
    :param key: one of 'w', 'a', 's', or 'd'
    :precondition: a game state dictionary in the playing phase
    :postcondition: the player moved or rewrote next to themselves, and rewrite mode is off after a rewrite
    """
    if state["rewrite_mode"]:
        player.player_rewrite(f"r{key}", state["character"], state["map"])
        state["rewrite_mode"] = False
    else:
        player.move(key, state["character"], state["map"], state["achieved_goal"])


def world_step(state: dict):
    """
    Advances every mob by one tick and checks whether the player died or finished the level.

    :param state: the game state dictionary
    :precondition: a game state dictionary in the playing phase
    :postcondition: the game state advanced by one tick
    """
    current_map = state["map"]
    mobs = state["mobs"]
    character = state["character"]
    time_machine = state["time_machine"]
    levels.overwritten(current_map, mobs, character)
    for mob in mobs:
        levels.ai_parse(mob, mobs, current_map, character, 0,
                        random.choice([("w", 0, -1), ("a", -1, 0), ("s", 0, 1), ("d", 1, 0)]))
        if len(mob["ai"]) == 2:
            mob["ai"] = [mob["ai"][1], mob["ai"][0]]
    levels.meteor_impact(character, mobs, current_map, time_machine)
    state["achieved_goal"] = levels.check_level_goal(mobs)
    if state["achieved_goal"]:
        state["level_text"] = t.end_txt(character)
    levels.overwritten(current_map, [time_machine, character], character)
    time_machine["alive"] = True
    if not character["alive"]:
        state["phase"] = "over"
        state["screen"] = player.how_died(current_map, character) + "\n\n  Press space to play again."


def draw(state: dict):
    """
    Renders the map with the side text.

    :param state: the game state dictionary
    :precondition: a game state dictionary in the playing phase
    :postcondition: the screen of the game state replaced with the current map
    """
    side_text = HELP_TEXT if state["help"] else state["level_text"]
    state["screen"] = map.map_art(map.display_text_next_to_map(state["map"], side_text, 0), state["character"])


def tick(state: dict, key=None):
    """
    Runs one tick of the game.

    :param state: the game state dictionary
    :param key: a single character string held or pressed since the last tick, or None if nothing was pressed
    :precondition: a game state dictionary
    :postcondition: the game state advanced by one tick if a direction was held, otherwise only redrawn
    :return: the game state
    """
    key = key.lower() if key else None
    if state["phase"] in ["intro", "over"]:
        if key == " ":
            if state["phase"] == "over":
                state.clear()
                state.update(new_game())
                start_level(state)
            else:
                state["phase"] = "playing"
                draw(state)
        return state
    if state["phase"] == "travel":
        start_level(state)
        return state
    if key == "h":
        state["help"] = not state["help"]
    elif key == "r":
        state["rewrite_mode"] = not state["rewrite_mode"]
    if key not in ["w", "a", "s", "d"]:
        draw(state)
        return state
    player_action(state, key)
    world_step(state)
    if state["phase"] != "playing":
        return state
    character = state["character"]
    time_machine = state["time_machine"]
    if (state["achieved_goal"] and character["y_coordinate"] == time_machine["y_coordinate"]
            and character["x_coordinate"] == time_machine["x_coordinate"]):
        start_level(state)
        return state
    state["ticks"] += 1
    draw(state)
    return state


def status(state: dict) -> dict:
    """
    Summarizes the game state for the page's status bar.

    :param state: the game state dictionary
    :precondition: a game state dictionary
    :postcondition: a dictionary
    :return: a dictionary of the values the page shows next to the game screen
    """
    return {"phase": state["phase"], "rewrite_mode": state["rewrite_mode"], "help": state["help"],
            "seconds": state["ticks"] // TICKS_PER_SECOND, "level": state["character"]["level"],
            "goal": state["achieved_goal"], "name": state["character"]["name"]}
