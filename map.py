from itertools import cycle
import random
from text import input_color


def room(y_length: int, x_length: int, x_offset: int, y_offset: int):
    """
    Defines the location of a room as a dictionary for the map.

    :param y_length: 0 < y_length < 30
    :param x_length: 0 < x_length < 30
    :param x_offset: 0 < x_offset < 29
    :param y_offset: 0 < y_offset < 29
    :precondition: four positive integers
    :postcondition: a dictionary with keys representing rows the content of which are dictionaries the keys
    being the column and the content being 1
    :return: a dictionary containing the coordinates the room contains

    >>> room(1, 1, 0, 0)
    {(1, 1): '   '}
    >>> room(0, 0, 0, 0)
    {}

    """
    output = {}
    for row in range(y_offset + 1, y_length + y_offset + 1):
        for column in range(x_offset + 1, x_length + x_offset + 1):
            output[row, column] = "   "
    return output


def room_combiner(first_room: dict, second_room: dict):
    """
    Combines the two rooms into a single dictionary even if they overlap

    :param first_room: a dictionary containing a tuple with two integers as the keys and a homogeneous value
    :param second_room: a dictionary containing a tuple with two integers as the keys and a homogeneous value
    :precondition: two dictionaries
    :postcondition: one dictionary
    :return: a dictionary containing

    >>> room_combiner({(1, 1): '   '}, {(1, 2): '   '})
    {(1, 1): '   ', (1, 2): '   '}
    >>> room_combiner({(1, 1): '   '}, {(1, 1): '   '})
    {(1, 1): '   '}
    """
    return {key: "   " for key in list(first_room.keys()) + list(second_room.keys())}


def rewrite(map_key: dict, x_coordinate: int, y_coordinate: int, content, area=1):
    """
    Rewrites the values of a given dictionary at an (x,y) coordinate

    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param x_coordinate: an integer
    :param y_coordinate: en integer
    :param content: a string or integer
    :param area: a positive integer
    :precondition: a dictionary, two integers corresponding to the (x,y) coordinates,
     and any type of content as a value
    :postcondition: a dictioanry
    :return: the values of the corresponding locations replaced by the value of "content"

    >>> test_map = {}
    >>> print(rewrite(test_map, 1, 1, 3))
    {(1, 1): 3}
    >>> test_map = {(1, 1): 3}
    >>> print(rewrite(test_map, 1, 1, 3))
    {(1, 1): '   '}
    """
    for row in range(area):
        for column in range(area):
            if ((y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2)) in map_key.keys()
                    and content == 3
                    and map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] == 3
                    and 30 > y_coordinate > 0 and 30 > x_coordinate > 0):
                map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] = "   "
            elif 30 > y_coordinate > 0 and 30 > x_coordinate > 0:
                map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] = content
    return map_key


def display_text_next_to_map(map_key: dict, input_text: str, rows_down=0):
    """
    Breaks up input text for each '/' and places it at the end of each row of the map.

    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param input_text: a string
    :param rows_down: an integer
    :precondition: a dictionary a string and an integer
    :postcondition: a dictionary
    :return: the map key dictionary modified to have the input text broken up by every '/' at the end of each row

    >>> display_text_next_to_map({}, "this/is/a/test")
    {(0, 31): '  this', (1, 31): '  is', (2, 31): '  a', (3, 31): '  test'}
    >>> display_text_next_to_map({}, "basecase")
    {(0, 31): '  basecase'}
    """
    line = "  "
    for letter in input_text:
        if letter != "/":
            line += letter
        else:
            map_key[(rows_down, 31)] = line
            rows_down += 1
            line = "  "
    map_key[(rows_down, 31)] = line
    return map_key


def level_start_display(input_text: str):
    """
    Displays level text without the map

    :param input_text: a string
    :precondtion: a non-empty string
    :postcondition: a string
    :return: the string modified to have a new line and two spaces after each /

    >>> print(level_start_display("this/is/a/test"))
      this
      is
      a
      test
    <BLANKLINE>
    >>> print(level_start_display("m"))
      m
    <BLANKLINE>
    """
    output = ""
    map_key = {}
    display_text_next_to_map(map_key, input_text)
    for row in range(len(map_key)):
        output += map_key[(row, 31)]
        output += "\n"
    return output


def map_art(map_key: dict, character: dict):
    """
    Produces ascii art of the map based on the value of each position in the map dictionary

    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    an integer or string as the value
    :param character: the dictionary containing the player character's stats
    :precondition: two dictionaries
    :postcondition: a string
    :return: ascii art contained in a string with everything in the map and the level text displayed in the
    correct places
    """
    output = ""
    wall = ["   ", cycle(["/|/", "\\|\\"]), cycle(["_|_", "__|", "___", "|__"]), "   "]
    colors = ["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "BRIGHT_RED",
              "BRIGHT_GREEN", "BRIGHT_YELLOW", "BRIGHT_BLUE", "BRIGHT_MAGENTA", "BRIGHT_CYAN"]
    for row in range(31):
        for column in range(32):
            if not (row, column) in map_key.keys():
                if character["level"] == 4:
                    output += input_color(wall[0], "WHITE", "WHITE")
                elif character["level"] == 3:
                    output += input_color(next(wall[1]), "GREEN", "BLACK")
                elif character["level"] == 2:
                    output += input_color(next(wall[2]), "DARK_GRAY", "BLACK")
                elif character["level"] == 1:
                    output += input_color(wall[3], "BLUE", "DARK_GRAY")
                else:
                    output += input_color("000", "WHITE", "WHITE")
            elif map_key[(row, column)] == 3:
                for number in range(3):
                    output += input_color(
                        chr(random.randint(48, 5000)),
                        random.choice(colors),
                        random.choice(colors))
            elif type(map_key[(row, column)]) == type(""):
                output += map_key[(row, column)]
        output += "\n"
    return output


def main():
    """
    Drive the program
    """
    room1 = room(5, 6, 3, 1)
    room2 = room(20, 1, 2, 1)
    room3 = room(1, 20, 2, 20)
    room4 = room(10, 10, 19, 19)
    combined_rooms = room_combiner(room1, room_combiner(room2, room_combiner(room3, room4)))
    rewrite(combined_rooms, 3, 5, 2, 1)
    display_text_next_to_map(combined_rooms, "This is neat!", 10)
    print(map_art(combined_rooms, {"level": 1}))


if __name__ == "__main__":
    main()
