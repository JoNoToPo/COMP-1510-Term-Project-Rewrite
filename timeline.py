"""
Keeps track of how history has been rewritten between playthroughs.
"""

import json

TIMELINE_FILE = "timeline.json"
ORIGINAL_HISTORY = {"hitler_killed": False, "dinosaurs": False, "boss_name": ""}


def load_timeline(file_name=TIMELINE_FILE):
    """
    Loads the version of history left behind by previous playthroughs.

    :param file_name: a string naming the json file history is saved in
    :precondition: a string
    :postcondition: a dictionary
    :return: a dictionary with the keys 'hitler_killed', 'dinosaurs', and 'boss_name', holding the original history
    for anything that has not been saved yet

    >>> load_timeline("a file that does not exist.json")
    {'hitler_killed': False, 'dinosaurs': False, 'boss_name': ''}
    """
    history = dict(ORIGINAL_HISTORY)
    try:
        with open(file_name) as file_object:
            saved = json.load(file_object)
    except (OSError, ValueError):
        return history
    if isinstance(saved, dict):
        history.update({key: saved[key] for key in ORIGINAL_HISTORY if key in saved})
    return history


def save_timeline(history: dict, file_name=TIMELINE_FILE):
    """
    Saves a version of history for future playthroughs.

    :param history: a dictionary with the keys 'hitler_killed', 'dinosaurs', and 'boss_name'
    :param file_name: a string naming the json file history is saved in
    :precondition: a dictionary and a string
    :postcondition: the history written to the file
    """
    with open(file_name, "w") as file_object:
        json.dump(history, file_object)


def rewrite_history(character: dict, file_name=TIMELINE_FILE):
    """
    Changes history for future playthroughs based on the level the character just completed.

    Killing Hitler means the next run hunts Meinard Goudier and killing Goudier brings Hitler back. Stopping the
    meteor leaves the dinosaurs alive and making the meteor fall brings the humans back. Beating the final boss makes
    the character the next final boss.

    :param character: the player dictionary with at minimum the keys 'level', 'name', and 'timeline'
    :param file_name: a string naming the json file history is saved in
    :precondition: a dictionary of a character standing on the time machine after finishing their level
    :postcondition: the saved history changed according to the level the character finished
    :return: the saved history
    """
    history = load_timeline(file_name)
    if character["level"] == 2:
        history["hitler_killed"] = not character["timeline"]["hitler_killed"]
    elif character["level"] == 3:
        history["dinosaurs"] = not character["timeline"]["dinosaurs"]
    elif character["level"] == 4:
        history["boss_name"] = character["name"]
    else:
        return history
    save_timeline(history, file_name)
    return history
