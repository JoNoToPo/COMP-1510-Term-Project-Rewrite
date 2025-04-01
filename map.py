from itertools import permutations, cycle

import player
import random
from text import input_color
import text


def room(y_length, x_length, x_offset, y_offset):
    """
    Defines the location of a room as a dictionary for the map.

    :precondition: four positive integers
    :postcondition: a dictionary with keys representing rows the content of which are dictionaries the keys
    being the column and the content being 1
    :param y_length: an integer defining the length of the room in the y-axis
    :param x_length: an integer defining the length of the room in the x-axis
    :param x_offset: an integer defining how far offset the room is from the left in the x-axis
    :param y_offset: an integer defining how far offset the room is from the top in the y-axis
    :return: a dictionary containing the coordinates the room contains

    >>> room(1, 1, 1, 1)
    {(2, 2): '   '}

    """
    output = {}
    for row in range(y_offset + 1, y_length + y_offset + 1):
        for column in range(x_offset + 1, x_length + x_offset + 1):
            output[(row, column)] = "   "
    return output


def room_combiner(first_room, second_room):
    """
    Combines the two rooms into a single dictionary even if they overlap

    :precondition: two dictionaries
    :postcondition: one dictionary
    :param first_room: a dictionary containing a tuple with two integers as the keys and a homogeneous value
    :param second_room: a dictionary containing a tuple with two integers as the keys and a homogeneous value
    :return: a dictionary containing
    """
    output = {}
    for key in list(first_room.keys()) + list(second_room.keys()):
        if key in first_room.keys():
            output[key] = first_room[key]
        else:
            output[key] = second_room[key]
    return output


def rewrite(map_key, x_coordinate, y_coordinate, content, area=1):
    """
    Rewrites the values of a given dictionary at an (x,y) coordinate

    :precondition: a dictionary, two integers corresponding to the (x,y) coordinates,
     and any type of content as a value
    :postcondition: the values of the corresponding locations replaced by the value of "content"
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple as the key and
    an integer or string as the value
    :param x_coordinate: an integer
    :param y_coordinate: en integer
    :param content: a string or integer
    :param area: a positive integer
    """
    for row in range(area):
        for column in range(area):
            if (player.authenticate_place(x_coordinate - column + int(area / 2), y_coordinate - row + int(area / 2),
                                          map_key) and map_key[
                (y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] == 3):
                map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] = "   "
            else:
                map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] = content
    return map_key


def display_text_next_to_map(map_key, input_text, rows_down=0):
    """
    Breaks up input text for each '/' and places it at the end of each row of the map.

    :precondition: a dictionary a string and an integer
    :postcondition: a dictionary
    :param map_key: a dictionary of non-zero length containing two integer coordinates in a tuple as the key and
    an integer or string as the value
    :param input_text: a string
    :param rows_down: an integer
    :return: the map key dictionary modified to have the input text at the end of each row

    >>> display_text_next_to_map({}, "this/is/a/test")
    {(0, 31): '   this', (1, 31): '   is', (2, 31): '   a', (3, 31): '   test'}
    >>> display_text_next_to_map({}, "basecase")
    {(0, 31): '   basecase'}
    """
    line = "   "
    for letter in input_text:
        if letter != "/":
            line += letter
        else:
            map_key[(rows_down, 31)] = line
            rows_down += 1
            line = "   "
    map_key[(rows_down, 31)] = line
    return map_key


def map_art(map_key, character):
    output = ""
    wall = ["   ", cycle(["/|/", "\\|\\"]), cycle(["_|_", "__|", "___", "|__"]), cycle(["\\\\/", "/\\\\"])]
    for row in range(31):
        for column in range(32):
            if not player.authenticate_place(column, row, map_key):
                if character["level"] == 4:
                    output += input_color(wall[0], "WHITE", "WHITE")
                elif character["level"] == 3:
                    output += input_color(next(wall[1]), "GREEN")
                elif character["level"] == 2:
                    output += input_color(next(wall[2]), "DARK_GRAY", "BLACK")
                elif character["level"] == 1:
                    output += input_color(next(wall[3]), "BLUE", "DARK_GRAY")
                else:
                    output += input_color("000", "WHITE", "WHITE")
            elif map_key[(row, column)] == 3:
                for number in range(3):
                    output += input_color(
                        chr(random.randint(48, 5000)),
                        random.choice(text.colors),
                        random.choice(text.colors))
            elif type(map_key[(row, column)]) == type(""):
                output += map_key[(row, column)]
        output += "\n"
    return output

def level_start_display(input_text):
    output = ""
    map_key = {}
    display_text_next_to_map(map_key, input_text)
    for row in range(len(map_key) - 1):
        output += map_key[(row, 31)]
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
    print(map_art(combined_rooms))


if __name__ == "__main__":
    main()