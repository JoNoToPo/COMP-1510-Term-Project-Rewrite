import map
import initialize


def game():
    start_map = initialize.initialize()
    print(map.map_art(start_map))


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()