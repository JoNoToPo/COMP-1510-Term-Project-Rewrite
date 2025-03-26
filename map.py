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
    """
    output = {}
    for row in range(y_offset, y_length + y_offset):
        for column in range(x_offset + 1, x_length + x_offset + 1):
            output[(row, column)] = "   "
    return output


def room_combiner(first_room, second_room):
    output = {}
    for key in list(first_room.keys()) + list(second_room.keys()):
        if key in first_room.keys():
            output[key] = first_room[key]
        else:
            output[key] = second_room[key]
    return output


def rewrite(map_key, x_coordinate, y_coordinate, content, area=1):
    for row in range(area):
        for column in range(area):
            if (player.authenticate_place(x_coordinate - column + int(area / 2), y_coordinate - row + int(area / 2),
                                          map_key) and map_key[
                (y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] == 3):
                map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] = "   "
            else:
                map_key[(y_coordinate - row + int(area / 2), x_coordinate - column + int(area / 2))] = content
    return map_key


def display_text_next_to_map(map_key, input_text, rows_down):
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
    output = "|/|" * 31 + "\n"
    for row in range(30):
        for column in range(32):
            if not player.authenticate_place(column, row, map_key):
                if character["level"] == 4:
                    output += input_color(random.choices(["|/|", "000"], [0.95, 0.05])[0], "WHITE", "WHITE")
                elif character["level"] == 3:
                    output += input_color(random.choices(["|/|", "|||"], [0.95, 0.05])[0], "GREEN")
                elif character["level"] == 2:
                    output += input_color(random.choices(["]]]", "[[["], [0.95, 0.05])[0], "DARK_GRAY", "BLACK")
                elif character["level"] == 1:
                    output += input_color(random.choices(["0|0", "0|0"], [0.95, 0.05])[0], "BLUE", "DARK_GRAY")
                else:
                    output += random.choices(["000", "0|0"], [0.95, 0.05])[0]
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

def level_start_display(map_key):
    output = ""
    for row in range(30):
        for column in range(31, 32):
            if not player.authenticate_place(column, row, map_key):
                output += ""
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
    print(map_art(combined_rooms))


if __name__ == "__main__":
    main()