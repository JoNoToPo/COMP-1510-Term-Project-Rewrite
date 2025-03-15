import random
import map
import mobs
import player


def room_radomizer(max_size, min_size):
    y_length = min_size + int(random.random() * (max_size - min_size + 1))
    x_length = min_size + int(random.random() * (max_size - min_size + 1))
    x_offset = int(random.random() * (30 - x_length))
    y_offset = int(random.random() * (30 - y_length))
    return map.room(y_length, x_length,
                    x_offset, y_offset)


def room_connector(first_room, second_room):
    random_place_first_room = random.choice(list(first_room.keys()))
    y_start = random_place_first_room[0]
    x_start = random_place_first_room[1]
    random_place_second_room = random.choice(list(second_room.keys()))
    y_end = random_place_second_room[0]
    x_end = random_place_second_room[1]
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
    initialize_mob(mobs.time_machine, starting_room)
    map.rewrite(starting_room, mobs.time_machine["x_coordinate"], mobs.time_machine["y_coordinate"], 4, 1)
    while number_of_rooms != 1:
        starting_room = room_connector(starting_room, room_radomizer(max_room_size, min_room_size))
        number_of_rooms -= 1
    return starting_room


def initialize_mob(mob, start_room):
    placed = False
    while not placed:
        place = random.choice(list(start_room.keys()))
        mob["y_coordinate"] = place[0]
        mob["x_coordinate"] = place[1]
        if player.authenticate_place(mob["x_coordinate"], mob["y_coordinate"], start_room):
            placed = True
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