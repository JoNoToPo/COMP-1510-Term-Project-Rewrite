def room(y_length, x_length, x_offset, y_offset):
    output = {}
    for row in range(y_offset, y_length + y_offset):
        output[row] = {}
        for column in range(x_offset, x_length + x_offset):
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


def player_location(map_key, x_coordinate, y_coordinate):
    map_key[y_coordinate][x_coordinate] = 2
    return map_key


def map_art(map_key):
    output = ""
    for row in range(30):
        if row not in map_key.keys():
            output += "|/|" * 30
        else:
            for column in range(30):
                if column not in map_key[row].keys():
                    output += "|/|"
                elif map_key[row][column] == 1:
                    output += " . "
                elif map_key[row][column] == 2:
                    output += " @ "
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
    player_location(combined_rooms, 3, 5)
    print(map_art(combined_rooms))


if __name__ == "__main__":
    main()