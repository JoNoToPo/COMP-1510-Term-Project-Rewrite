from unittest import TestCase
from levels import happens_when_died


class Test(TestCase):
    def test_happens_when_died_dummy(self):
        mob ={"alive": True, "name": "Dummy", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_hitler(self):
        mob = {"alive": True, "name": "Hitler", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_meteor(self):
        mob = {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_meteor_many(self):
        mob = {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 1}
        mobs = [mob,
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 2},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 3},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 4},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 5},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 6},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 7},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 8},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 9},
                {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 10}]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = [{"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 2},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 3},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 4},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 5},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 6},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 7},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 8},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 9},
                    {"alive": True, "name": "meteor", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D ", "id": 10}]
        self.assertEqual(mobs, expected)

    def test_happens_when_died_bullet(self):
        mob = {"alive": True, "name": "bullet", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_GREATEST_GRANDFATHER(self):
        mob = {"alive": True, "name": "GREATEST GRANDFATHER", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "something"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_great_grandfather_not_murdered(self):
        mob = {"alive": True, "name": "Great-Grandfather", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_greater_grandfather_not_murdered(self):
        mob = {"alive": True, "name": f"{"Great-" * 500}Grandfather", "y_coordinate": 0, "x_coordinate": 0,
               "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_Professor_not_murdered(self):
        mob = {"alive": True, "name": "Professor", "y_coordinate": 0, "x_coordinate": 0,
               "symbol": " D "}
        mobs = [mob]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          mob,
                          mobs,
                          character)
        expected = []
        self.assertEqual(mobs, expected)

    def test_happens_when_died_great_grandfather_murdered(self):
        mobs = [{"alive": True, "name": "Great-Grandfather", "y_coordinate": 0, "x_coordinate": 0, "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          {"alive": True, "name": "Great-Grandfather", "y_coordinate": 0, "x_coordinate": 0,
                           "symbol": " D "},
                          mobs,
                          character)
        expected = {(0, 0): "Great-Grandfather"}
        self.assertEqual(map_key, expected)

    def test_happens_when_died_greater_grandfather_murdered(self):
        mobs = [{"alive": True, "name": f"{"Great-" * 500}Grandfather", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          {"alive": True, "name": f"{"Great-" * 500}Grandfather", "y_coordinate": 0, "x_coordinate": 0,
                           "symbol": " D "},
                          mobs,
                          character)
        expected = {(0, 0): f"{"Great-" * 500}Grandfather"}
        self.assertEqual(map_key, expected)

    def test_happens_when_died_Professor_murdered(self):
        mobs = [{"alive": True, "name": "Professor", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0}
        happens_when_died(map_key,
                          {"alive": True, "name": "Professor", "y_coordinate": 0, "x_coordinate": 0,
                           "symbol": " D "},
                          mobs,
                          character)
        expected = {(0, 0): "Professor"}
        self.assertEqual(map_key, expected)

    def test_happens_when_died_Time_Machine_murdered(self):
        mobs = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): 3}
        character = {"y_coordinate": 0, "x_coordinate": 0, "symbol": "whatever"}
        happens_when_died(map_key,
                          {"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                           "symbol": " D "},
                          mobs,
                          character)
        expected = {(0, 0): "Time Machine"}
        self.assertEqual(map_key, expected)

    def test_happens_when_died_Time_Machine_revive(self):
        mobs = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                 "symbol": " D "}]
        map_key = {(0, 0): "anything other than 3"}
        character = {"y_coordinate": 0, "x_coordinate": 0, "symbol": "whatever"}
        happens_when_died(map_key,
                          {"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                           "symbol": " D "},
                          mobs,
                          character)
        expected = [{"alive": True, "name": "Time Machine", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}]
        self.assertEqual(mobs, expected)

    def test_happens_when_died_character(self):
        map_key = {(0, 0): "character symbol"}
        character = {"alive": True, "name": "player", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}
        mobs = [character]
        happens_when_died(map_key,
                          {"alive": True, "name": "player", "y_coordinate": 0, "x_coordinate": 0,
                           "symbol": " D "},
                          mobs,
                          character)
        expected = [{"alive": True, "name": "player", "y_coordinate": 0, "x_coordinate": 0,
                     "symbol": " D "}]
        self.assertEqual(mobs, expected)
