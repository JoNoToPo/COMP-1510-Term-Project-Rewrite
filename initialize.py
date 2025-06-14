import random
import map
import player


def room_randomizer(max_size: int, min_size: int):
    """
    Randomizes the size and placement of a room.

    :param max_size: an integer indicating the maximum size the room can be 1 < max_size < 29
    :param min_size: an integer indicating the minimum size the room can be 1 < min_size < 29
    :precondition: two integers
    :postcondition: one dictionary
    :return: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    '   ' as the value
    """
    y_length = min_size + int(random.random() * (max_size - min_size + 1))
    x_length = min_size + int(random.random() * (max_size - min_size + 1))
    x_offset = int(random.random() * (29 - x_length))
    y_offset = int(random.random() * (29 - y_length))
    return map.room(y_length, x_length,
                    x_offset, y_offset)


def room_connector(first_room: dict, second_room: dict):
    """
    Connects two rooms with a hallway

    :param first_room: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    '   ' as the value
    :param second_room: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    '   ' as the value
    :precondition: two dictionaries of non-zero length containing two integer coordinates in a tuple for each key and
    '   ' as the value
    :postcondition: one dictionary
    :return: a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    '   ' as the value

    >>> room_connector({(1, 1): "   "}, {(3, 3): "   "})
    {(1, 1): '   ', (3, 3): '   ', (2, 1): '   ', (3, 1): '   ', (3, 2): '   '}

    >>> room_connector({(1, 3): "   "}, {(3, 1): "   "})
    {(1, 3): '   ', (3, 1): '   ', (2, 3): '   ', (3, 2): '   ', (3, 3): '   '}
    """
    random_place_first_room = random.choice(list(first_room.keys()))
    y_start = random_place_first_room[0] - 1
    x_start = random_place_first_room[1] - 1
    random_place_second_room = random.choice(list(second_room.keys()))
    y_end = random_place_second_room[0] - 1
    x_end = random_place_second_room[1] - 1
    if y_start < y_end:
        if x_start < x_end:
            first_hall = map.room(y_end - y_start, 1, x_start, y_start)
            second_hall = map.room(1, x_end - x_start, x_start, y_end)
        else:
            first_hall = map.room(y_end - y_start, 1, x_start, y_start)
            second_hall = map.room(1, x_start - x_end + 1, x_end, y_end)
    else:
        if x_start > x_end:
            first_hall = map.room(y_start - y_end, 1, x_start, y_end)
            second_hall = map.room(1, x_start - x_end, x_end, y_end)
        else:
            first_hall = map.room(y_start - y_end, 1, x_start, y_end)
            second_hall = map.room(1, x_end - x_start, x_start, y_end)
    return map.room_combiner(first_room, map.room_combiner(second_room, map.room_combiner(first_hall, second_hall)))


def starting_map(starting_room: dict, max_room_size: int, min_room_size: int, number_of_rooms: int):
    """
    Randomizes the initial ascii map for a floor

    :param starting_room: a dictionary containing the coordinates of one rectangular room
    :param max_room_size: an integer indicating the maximum size the room can be 1 < max_size < 29
    :param min_room_size: an integer indicating the minimum size the room can be 1 < min_size < 29
    :param number_of_rooms: a positive non-zero integer indicating the amount of rooms that will be generated
    :precondition: a dictionary and three integers
    :postcondition: a dictionary
    :return: the starting map a dictionary of non-zero length containing two integer coordinates in a tuple for each key and
    '   ' for each value
    """
    while number_of_rooms != 1:
        starting_room = room_connector(starting_room, room_randomizer(max_room_size, min_room_size))
        number_of_rooms -= 1
    return starting_room


def initialize_mob(mob: dict, map_key: dict, start_room: dict):
    """
    Places a mob where there are no other mobs.

    :param mob: the mob dictionary with at minimum the keys y_coordinate and x_coordinate
    :param map_key: the map within which the mob is being placed
    :param start_room: the coordinates within which the mob is not allowed to be placed
    :precondition: three dictionaries
    :postcondition: a dictionary
    :return: the mob dictionary with the coordinates randomized to be within the given map and outside the start room

    >>> initialize_mob({"y_coordinate": 0, "x_coordinate": 0}, {(0, 0): "   ", (3,3): "   "}, {(0, 0): "   "})
    {'y_coordinate': 3, 'x_coordinate': 3}
    >>> initialize_mob({"y_coordinate": 0, "x_coordinate": 0}, {(3,3): "   "}, {(0, 0): ""})
    {'y_coordinate': 3, 'x_coordinate': 3}
    """
    placed = False
    while not placed:
        place = random.choice(list(map_key.keys()))
        mob["y_coordinate"] = place[0]
        mob["x_coordinate"] = place[1]
        if (player.authenticate_move(mob["x_coordinate"], mob["y_coordinate"], map_key, False)
                and place not in start_room.keys()):
            placed = True
    return mob


def initialize_player(player_character: dict, time_machine: dict):
    """
    Levels up the player and places the player on the time machine

    :param player_character: the player dictionary
    :param time_machine: the time machine dictionary
    :precondition: two dictionaries
    :postcondition: one dictionary
    :return: the player dictionary modified with "level" incremented by one, "area" incremented by two, and the player's
    coordinates the same as the time machine

    >>> test_player = {"level": 0, "area": -1, "x_coordinate": 0, "y_coordinate": 0}
    >>> test_time_machine = {"x_coordinate": 1, "y_coordinate": 1}
    >>> initialize_player(test_player, test_time_machine)
    {'level': 1, 'area': 1, 'x_coordinate': 1, 'y_coordinate': 1}
    """
    player_character["level"] += 1
    player_character["area"] += 2
    player_character["y_coordinate"] = time_machine["y_coordinate"]
    player_character["x_coordinate"] = time_machine["x_coordinate"]
    return player_character


def main():
    """
    Drive the program
    """
    # starting_room = room_randomizer(1, 1)
    # room2 = room_randomizer(1, 1)
    # room3 = room_randomizer(1, 1)
    # room4 = room_randomizer(1, 1)
    starting_room = map.room(2, 2, 5, 20)
    room2 = map.room(2, 2, 1, 25)
    start_map = room_connector(starting_room, room2)
    print(map.map_art(start_map, {"level": 1}))


if __name__ == "__main__":
    main()