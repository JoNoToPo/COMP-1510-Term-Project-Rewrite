from unittest import TestCase

from levels import shot
from text import input_color


class Test(TestCase):
    def test_shot_just_shot(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "w", "just_shot": True}
        map_key = {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                   (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        shot(character, map_key)
        expected_character = {"name": "bullet", "x_coordinate": 2,
                              "y_coordinate": 2, "alive": True,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": character["direction"], "just_shot": False}
        self.assertEqual(character, expected_character)

    def test_shot_correctly_shot_w(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "w", "just_shot": False}
        map_key = {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                   (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        shot(character, map_key)
        expected_map = {(1, 2): input_color(" • ", "BRIGHT_RED"), (2, 2): "   ",
                        (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        self.assertEqual(map_key, expected_map)

    def test_shot_correctly_shot_a(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "a", "just_shot": False}
        map_key = {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                   (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        shot(character, map_key)
        expected_map = {(1, 2): "   ", (2, 2): "   ",
                        (2, 1): input_color(" • ", "BRIGHT_RED"), (3, 2): "   ", (2, 3): "   "}
        self.assertEqual(map_key, expected_map)

    def test_shot_correctly_shot_s(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "s", "just_shot": False}
        map_key = {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                   (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        shot(character, map_key)
        expected_map = {(1, 2): "   ", (2, 2): "   ",
                        (2, 1): "   ", (3, 2): input_color(" • ", "BRIGHT_RED"), (2, 3): "   "}
        self.assertEqual(map_key, expected_map)

    def test_shot_correctly_shot_d(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "d", "just_shot": False}
        map_key = {(1, 2): "   ", (2, 2): input_color(" • ", "BRIGHT_RED"),
                   (2, 1): "   ", (3, 2): "   ", (2, 3): "   "}
        shot(character, map_key)
        expected_map = {(1, 2): "   ", (2, 2): "   ",
                        (2, 1): "   ", (3, 2): "   ", (2, 3): input_color(" • ", "BRIGHT_RED")}
        self.assertEqual(map_key, expected_map)

    def test_shot_blocked(self):
        character = {"name": "bullet", "x_coordinate": 2,
                     "y_coordinate": 2, "alive": True,
                     "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                     "ai": ["shot"], "direction": "d", "just_shot": False}
        map_key = {(2, 2): input_color(" • ", "BRIGHT_RED")}
        shot(character, map_key)
        expected_map = {(2, 2): "   "}
        expected_character = {"name": "bullet", "x_coordinate": 2,
                              "y_coordinate": 2, "alive": False,
                              "symbol": input_color(" • ", "BRIGHT_RED"), "id": 0,
                              "ai": ["shot"], "direction": "d", "just_shot": False}
        self.assertEqual(map_key, expected_map)
        self.assertEqual(character, expected_character)
