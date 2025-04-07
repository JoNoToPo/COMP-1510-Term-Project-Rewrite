from unittest import TestCase

from levels import shot_move
from text import input_color


class Test(TestCase):
    def test_shot_move_w_correct(self):
        map_key = {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                   (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "w", "just_shot": False}
        shot_move(character, map_key)
        expected_character = {"name": "bullet", "x_coordinate": 2,
                              "y_coordinate": 1, "alive": True,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": character["direction"], "just_shot": False}
        self.assertEqual(character, expected_character)

    def test_shot_move_a_correct(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "a", "just_shot": False}
        shot_move(character, {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                              (2, 1): "   ", (3, 2): "   ", (2, 3): "   "})
        expected_character = {"name": "bullet", "x_coordinate": 1,
                              "y_coordinate": 2, "alive": True,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": character["direction"], "just_shot": False}
        self.assertEqual(character, expected_character)

    def test_shot_move_s_correct(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "s", "just_shot": False}
        shot_move(character, {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                              (2, 1): "   ", (3, 2): "   ", (2, 3): "   "})
        expected_character = {"name": "bullet", "x_coordinate": 2,
                              "y_coordinate": 3, "alive": True,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": character["direction"], "just_shot": False}
        self.assertEqual(character, expected_character)

    def test_shot_move_d_correct(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "d", "just_shot": False}
        shot_move(character, {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                              (2, 1): "   ", (3, 2): "   ", (2, 3): "   "})
        expected_character = {"name": "bullet", "x_coordinate": 3,
                              "y_coordinate": 2, "alive": True,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": character["direction"], "just_shot": False}
        self.assertEqual(character, expected_character)

    def test_shot_move_wrong(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "d", "just_shot": False}
        shot_move(character, {})
        expected_character = {"name": "bullet", "x_coordinate": 2,
                              "y_coordinate": 2, "alive": False,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": character["direction"], "just_shot": False}
        self.assertEqual(character, expected_character)
