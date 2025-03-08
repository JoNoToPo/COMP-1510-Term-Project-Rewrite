import random
import map


def room_radomizer(max_size, min_size):
    y_length = min_size + int(random.random() * (max_size - min_size + 1))
    x_length = min_size + int(random.random() * (max_size - min_size + 1))
    x_offset = int(random.random() * (30 - x_length))
    y_offset = int(random.random() * (30 - y_length))
    return map.room(y_length, x_length,
                    x_offset, y_offset)


def room_connector(first_room, second_room):
    y_start = random.choice(list(first_room.keys()))
    x_start = random.choice(list(first_room[y_start].keys()))
    y_end = random.choice(list(second_room.keys()))
    x_end = random.choice(list(second_room[y_end].keys()))
    if y_start < y_end:
        if x_start < x_end:
            first_hall = map.room(y_end - y_start, 1, x_start, y_start)
            second_hall = map.room(1, x_end - x_start, x_start, y_end)
        else:
            first_hall = map.room(y_end - y_start, 1, x_start, y_start)
            second_hall = map.room(1, x_start - x_end + 1, x_end, y_end)
    else:
        if x_start < x_end:
            first_hall = map.room(y_start - y_end, 1, x_start, y_end)
            second_hall = map.room(1, x_end - x_start, x_start, y_end)
        else:
            first_hall = map.room(y_start - y_end, 1, x_start, y_end)
            second_hall = map.room(1, x_start - x_end + 1, x_end, y_end)
    return map.room_combiner(first_room, map.room_combiner(second_room, map.room_combiner(first_hall, second_hall)))


def starting_map(starting_room, max_room_size, min_room_size, number_of_rooms):
    while number_of_rooms != 1:
        starting_room = room_connector(starting_room, room_radomizer(max_room_size, min_room_size))
        number_of_rooms -= 1
    return starting_room


def initialize_mob(mob, start_room):
    mob["y_coordinate"] = random.choice(list(start_room.keys()))
    mob["x_coordinate"] = random.choice(list(start_room[mob["y_coordinate"]].keys()))
    return mob


def main():
    """
    Drive the program
    """
    starting_room = room_radomizer(7, 3)
    room2 = room_radomizer(7, 3)
    room3 = room_radomizer(7, 3)
    room4 = room_radomizer(7, 3)
    start_map = room_connector(room_connector(starting_room, room2), room_connector(room3, room4))
    print(map.map_art(start_map))


if __name__ == "__main__":
    main()