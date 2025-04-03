from unittest import TestCase
from unittest.mock import patch
from levels import greater_grandfather
from text import input_color


class Test(TestCase):
    @patch('random.choice', side_effect=["move"])
    def test_greater_grandfather_one_move(self, _):
        actual = next(greater_grandfather())
        expected = {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                    "symbol": input_color(" G ", "YELLOW"),
                    "ai": ["move"], "id": 0}
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=["stay"])
    def test_greater_grandfather_one_stay(self, _):
        actual = next(greater_grandfather())
        expected = {"name": f"{"Great-" * 500}Grandfather", "x_coordinate": 0, "y_coordinate": 0, "alive": True,
                    "symbol": input_color(" G ", "YELLOW"),
                    "ai": ["stay"], "id": 0}
        self.assertEqual(actual, expected)
