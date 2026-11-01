from unittest import TestCase
from unittest.mock import patch

from player import new_character
from text import input_color
from timeline import ORIGINAL_HISTORY


class Test(TestCase):
    @patch("random.choice", side_effect=["Chris", "Thompson"])
    def test_new_character_actual(self, _):
        actual = new_character()
        expected = {"name": "Chris Thompson", "level": 0, "area": -1, "x_coordinate": 0,
                    "y_coordinate": 0, "alive": True, "symbol": input_color(" @ ", "GREEN", ),
                    "timeline": ORIGINAL_HISTORY}
        self.assertEqual(actual, expected)

    @patch("random.choice", side_effect=["random first name", "random last name"])
    def test_new_character_joke(self, _):
        actual = new_character()
        expected = {"name": "random first name random last name", "level": 0, "area": -1, "x_coordinate": 0,
                    "y_coordinate": 0, "alive": True, "symbol": input_color(" @ ", "GREEN", ),
                    "timeline": ORIGINAL_HISTORY}
        self.assertEqual(actual, expected)

    @patch("random.randint", side_effect=[5])
    @patch("random.choice", side_effect=["Chris", "Thompson"])
    def test_new_character_dinosaur(self, _, __):
        history = {"hitler_killed": False, "dinosaurs": True, "boss_name": ""}
        actual = new_character(history)
        expected = {"name": "Chris Thompdinoson", "level": 0, "area": -1, "x_coordinate": 0,
                    "y_coordinate": 0, "alive": True, "symbol": input_color(" & ", "GREEN", ), "timeline": history}
        self.assertEqual(actual, expected)
