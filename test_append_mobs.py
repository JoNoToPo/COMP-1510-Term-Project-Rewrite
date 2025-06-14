from unittest import TestCase
from unittest.mock import patch

from levels import append_mobs
from text import input_color


class Test(TestCase):
    def test_append_mobs_level_lower_than_zero_greater_than_4(self):
        actual = append_mobs({"level": 0})
        expected = []
        self.assertEqual(actual, expected)

    def test_append_mobs_level_4(self):
        actual = append_mobs({"level": 4})
        expected = [{"name": "GREATEST GRANDFATHER", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "WHITE", "BRIGHT_RED"),
                     "ai": ["move", "rewrite"], "area": 7}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[4])
    @patch('random.choice', side_effect=["stay", "stay", "stay", "stay"])
    def test_append_mobs_level_3_stay_4(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 3}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[5])
    @patch('random.choice', side_effect=["stay", "stay", "stay", "stay", "stay"])
    def test_append_mobs_level_3_stay_5(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 4}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[6])
    @patch('random.choice', side_effect=["stay", "stay", "stay", "stay", "stay", "stay"])
    def test_append_mobs_level_3_stay_6(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 5}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[7])
    @patch('random.choice', side_effect=["stay", "stay", "stay", "stay", "stay", "stay", "stay"])
    def test_append_mobs_level_3_stay_7(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 5},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 6}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[8])
    @patch('random.choice', side_effect=["stay", "stay", "stay", "stay", "stay", "stay", "stay", "stay"])
    def test_append_mobs_level_3_stay_8(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 5},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 6},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 7}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[4])
    @patch('random.choice', side_effect=["move", "move", "move", "move"])
    def test_append_mobs_level_3_move_4(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 3}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[5])
    @patch('random.choice', side_effect=["move", "move", "move", "move", "move"])
    def test_append_mobs_level_3_move_5(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 4}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[6])
    @patch('random.choice', side_effect=["move", "move", "move", "move", "move", "move"])
    def test_append_mobs_level_3_move_6(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 5}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[7])
    @patch('random.choice', side_effect=["move", "move", "move", "move", "move", "move", "move"])
    def test_append_mobs_level_3_move_7(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 5},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 6}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[8])
    @patch('random.choice', side_effect=["move", "move", "move", "move", "move", "move", "move", "move"])
    def test_append_mobs_level_3_move_8(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 5},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 6},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 7}]
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[8])
    @patch('random.choice', side_effect=["move", "stay", "move", "move", "move", "move", "stay", "move"])
    def test_append_mobs_level_3_vary_8(self, _, __):
        actual = append_mobs({"level": 3})
        expected = [{"name": "meteor", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" M ", "RED"),
                     "ai": ["fall", "countdown"], "time left": 25},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 0},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 1},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 2},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 3},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 4},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 5},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["stay"], "id": 6},
                    {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                     "symbol": input_color(" G ", "YELLOW"),
                     "ai": ["move"], "id": 7}]
        self.assertEqual(actual, expected)