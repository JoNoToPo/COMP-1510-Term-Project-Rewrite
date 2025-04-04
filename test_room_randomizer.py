from sys import activate_stack_trampoline
from unittest import TestCase
from unittest.mock import patch

from initialize import room_randomizer


class Test(TestCase):
    @patch('random.random', side_effect=[0.99, 0.99, 1, 1])
    def test_room_randomizer_all_high(self, _):
        actual = room_randomizer(1, 1)
        expected = {(29, 29): '   '}
        self.assertEqual(actual, expected)

    @patch('random.random', side_effect=[0, 0, 0, 0])
    def test_room_randomizer_all_0(self, _):
        actual = room_randomizer(30, 0)
        expected = {}
        self.assertEqual(actual, expected)

    @patch('random.random', side_effect=[0, 0, 1, 0])
    def test_room_randomizer_third_1(self, _):
        actual = room_randomizer(1, 1)
        expected = {(1, 29): '   '}
        self.assertEqual(actual, expected)

    @patch('random.random', side_effect=[0, 0, 0, 1])
    def test_room_randomizer_fourth_1(self, _):
        actual = room_randomizer(1, 1)
        expected = {(29, 1): '   '}
        self.assertEqual(actual, expected)

    @patch('random.random', side_effect=[0.5, 0.5, 0, 0])
    def test_room_randomizer_half(self, _):
        actual = room_randomizer(2, 1)
        expected = {(1, 1): '   ', (1, 2): '   ', (2, 1): '   ', (2, 2): '   '}
        self.assertEqual(actual, expected)
