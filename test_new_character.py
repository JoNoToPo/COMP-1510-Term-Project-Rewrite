from unittest import TestCase
from unittest.mock import patch

from player import new_character
from text import input_color


class Test(TestCase):
    @patch("random.choice", side_effect=["Chris", "Thompson"])
    def test_new_character_actual(self, _):
        actual = new_character()
        expected = {"name": "Chris Thompson", "level": 0, "area": -1, "x_coordinate": 0,
                    "y_coordinate": 0, "alive": True, "symbol": input_color(" @ ", "GREEN", )}
        self.assertEqual(actual, expected)

    @patch("random.choice", side_effect=["random first name", "random last name"])
    def test_new_character_joke(self, _):
        actual = new_character()
        expected = {"name": "random first name random last name", "level": 0, "area": -1, "x_coordinate": 0,
                    "y_coordinate": 0, "alive": True, "symbol": input_color(" @ ", "GREEN", )}
        self.assertEqual(actual, expected)
