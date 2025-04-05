from unittest import TestCase

from player import authenticate_move
from text import input_color


class Test(TestCase):
    def test_authenticate_move_wall(self):
        actual = authenticate_move(1, 1, {}, True)
        expected = False
        self.assertEqual(expected, actual)

    def test_authenticate_move_floor(self):
        actual = authenticate_move(1, 1, {(1, 1): "   "}, True)
        expected = True
        self.assertEqual(expected, actual)

    def test_authenticate_move_time_machine_true(self):
        actual = authenticate_move(1, 1,
                                   {(1, 1): input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")},
                                   True)
        expected = True
        self.assertEqual(expected, actual)

    def test_authenticate_move_time_machine_false(self):
        actual = authenticate_move(1, 1,
                                   {(1, 1): input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")},
                                   False)
        expected = False
        self.assertEqual(expected, actual)

