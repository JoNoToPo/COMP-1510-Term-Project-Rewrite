from unittest import TestCase

from levels import overwritten


class Test(TestCase):
    def test_overwritten_dummy(self):
        mobs = [{"alive": True, "name": "Dummy", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_hitler(self):
        mobs = [{"alive": True, "name": "Hitler", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_meteor(self):
        mobs = [{"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_meteor_many(self):
        mobs = [{"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 1},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 2},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 3},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 4},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 5},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 6},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 7},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 8},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 9},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 10},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 11}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_bullet(self):
        mobs = [{"alive": True, "name": "bullet", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_GREATEST_GRANDFATHER(self):
        mobs = [{"alive": True, "name": "GREATEST GRANDFATHER", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_great_grandfather_not_murdered(self):
        mobs = [{"alive": True, "name": "Great-Grandfather", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_greater_grandfather_not_murdered(self):
        mobs = [{"alive": True, "name": f"{"Great-" * 500}Grandfather", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_Professor_not_murdered(self):
        mobs = [{"alive": True, "name": "Professor", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_overwritten_great_grandfather_murdered(self):
        mobs = [{"alive": True, "name": "Great-Grandfather", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = {(0, 0): "Great-Grandfather"}
        self.assertEqual(map_key, expected)

    def test_overwritten_greater_grandfather_murdered(self):
        mobs = [{"alive": True, "name": f"{"Great-" * 500}Grandfather", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = {(0, 0): f"{"Great-" * 500}Grandfather"}
        self.assertEqual(map_key, expected)

    def test_overwritten_Professor_murdered(self):
        mobs = [{"alive": True, "name": "Professor", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        overwritten(map_key,
                    mobs,
                    character)
        expected = {(0, 0): "Professor"}
        self.assertEqual(map_key, expected)

    def test_overwritten_Time_Machine_murdered(self):
        mobs = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0, "symbol": "whatever"}
        overwritten(map_key,
                    mobs,
                    character)
        expected = {(0, 0): " D "}
        self.assertEqual(map_key, expected)

    def test_overwritten_Time_Machine_revive(self):
        mobs = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0, "symbol": "whatever"}
        overwritten(map_key,
                    mobs,
                    character)
        expected = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}]
        self.assertEqual(mobs, expected)

    def test_overwritten_Time_Machine_overlap(self):
        mobs = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): "character symbol"}
        character = {"y_coordinate": 0, "x_coordinate": 0, "symbol": "character symbol"}
        overwritten(map_key,
                    mobs,
                    character)
        expected = [{"alive": False, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}]
        self.assertEqual(mobs, expected)

    def test_overwritten_character(self):
        map_key = {(0, 0): "character symbol"}
        character = {"alive": True, "name": "player", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}
        mobs = [character]
        overwritten(map_key,
                    mobs,
                    character)
        expected = [{"alive": False, "name": "player", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}]
        self.assertEqual(mobs, expected)



