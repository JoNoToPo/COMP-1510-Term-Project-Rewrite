from unittest import TestCase
from initialize import find_path


class Test(TestCase):
    def test_find_path_straight_line(self):
        actual = find_path({(1, 1): "@", (1, 2): "   ", (1, 3): "D"}, (1, 1), (1, 3))
        expected = [(1, 1), (1, 2), (1, 3)]
        self.assertEqual(actual, expected)

    def test_find_path_around_corner(self):
        actual = find_path({(1, 1): "@", (2, 1): "   ", (2, 2): "D"}, (1, 1), (2, 2))
        expected = [(1, 1), (2, 1), (2, 2)]
        self.assertEqual(actual, expected)

    def test_find_path_blocked_by_wall(self):
        actual = find_path({(1, 1): "@", (1, 3): "D"}, (1, 1), (1, 3))
        expected = []
        self.assertEqual(actual, expected)

    def test_find_path_blocked_by_rewritten_tile(self):
        actual = find_path({(1, 1): "@", (1, 2): 3, (1, 3): "D"}, (1, 1), (1, 3))
        expected = []
        self.assertEqual(actual, expected)
