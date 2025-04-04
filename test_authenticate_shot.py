from unittest import TestCase

from levels import authenticate_shot
from text import input_color


class Test(TestCase):
    def test_authenticate_shot_floor(self):
        actual = authenticate_shot(1, 1, {(1, 1): "   "})
        expected = True
        self.assertEqual(actual, expected)

    def test_authenticate_shot_wall(self):
        actual = authenticate_shot(1, 1, {})
        expected = False
        self.assertEqual(actual, expected)

    def test_authenticate_shot_rewritten_space(self):
        actual = authenticate_shot(1, 1, {(1, 1): 3})
        expected = False
        self.assertEqual(actual, expected)

    def test_authenticate_shot_hitler(self):
        actual = authenticate_shot(1, 1, {(1, 1): input_color(" H ", "RED")})
        expected = False
        self.assertEqual(actual, expected)

    def test_authenticate_shot_meteor(self):
        actual = authenticate_shot(1, 1, {(1, 1): input_color(" M ", "RED")})
        expected = False
        self.assertEqual(actual, expected)

    def test_authenticate_shot_anything_else(self):
        actual = authenticate_shot(1, 1, {(1, 1): "anything else"})
        expected = True
        self.assertEqual(actual, expected)
