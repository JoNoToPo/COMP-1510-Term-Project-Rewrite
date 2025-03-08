import player


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
    :return: a dictionary containing the
    """
    output = {}
    for row in range(y_offset, y_length + y_offset):
        output[row] = {}
        for column in range(x_offset + 1, x_length + x_offset + 1):
            output[row][column] = 1
    return output


def room_combiner(first_room, second_room):
    output = {}
    for row in set(first_room.keys()).union(set(second_room.keys())):
        if type(row) == type(""):
            continue
        output[row] = {}
        for column in range(30):
            if row in first_room.keys():
                if column in first_room[row].keys():
                    output[row][column] = 1
            if row in second_room.keys():
                if column in second_room[row].keys():
                    output[row][column] = 1
    return output


def rewrite_spot(map_key, x_coordinate, y_coordinate, content):
    map_key[y_coordinate][x_coordinate] = content
    return map_key


def display_text_next_to_map(map_key, input_text, rows_down):
    line = ""
    for letter in input_text:
        if rows_down not in set(map_key.keys()):
            map_key[rows_down] = {30: ""}
        if letter != "/":
            line += letter
        else:
            map_key[rows_down][30] = line
            rows_down += 1
            line = ""
    map_key[rows_down][30] = line
    return map_key


def map_art(map_key):
    output = "|/|" * 31 + "\n"
    for row in range(30):
        if row not in map_key.keys():
            output += "|/|" * 31
        else:
            for column in range(31):
                if column not in map_key[row].keys():
                    output += "|/|"
                elif map_key[row][column] == 1:
                    output += " . "
                elif map_key[row][column] == 2:
                    output += " @ "
                elif type(map_key[row][column]) == type(""):
                    output += "|/|   " + map_key[row][column]
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
    rewrite_spot(combined_rooms, 3, 5, 2)
    display_text_next_to_map(combined_rooms, "This is neat!", 10)
    print(map_art(combined_rooms))


if __name__ == "__main__":
    main()