from unittest import TestCase
from map import rewrite


class Test(TestCase):
    def test_rewrite_wall_with_rewritten_space(self):
        actual = rewrite({}, 1, 1, 3)
        expected = {(1, 1): 3}
        self.assertEqual(actual, expected)

    def test_rewrite_rewrite_rewrite(self):
        actual = rewrite({(1, 1): 3}, 1, 1, 3)
        expected = {(1, 1): "   "}
        self.assertEqual(actual, expected)

    def test_rewrite_anything_else_rewrite(self):
        actual = rewrite({(1, 1): "anything_else"}, 1, 1, 3)
        expected = {(1, 1): 3}
        self.assertEqual(actual, expected)

    def test_rewrite_area_3_and_rewritten_space_rewrite(self):
        actual = rewrite({(1, 1): 3}, 1, 1, 3, 3)
        expected = {(0, 0): 3,
                    (0, 1): 3,
                    (0, 2): 3,
                    (1, 0): 3,
                    (1, 1): '   ',
                    (1, 2): 3,
                    (2, 0): 3,
                    (2, 1): 3,
                    (2, 2): 3}
        self.assertEqual(actual, expected)

    def test_rewrite_rewritten_space_anything_else(self):
        actual = rewrite({(1, 1): 3}, 1, 1, "anything")
        expected = {(1, 1): "anything"}
        self.assertEqual(actual, expected)

    def test_rewrite_wall_anything_else(self):
        actual = rewrite({}, 1, 1, "anything")
        expected = {(1, 1): "anything"}
        self.assertEqual(actual, expected)

    def test_rewrite_floor_anything_else(self):
        actual = rewrite({(1, 1): "   "}, 1, 1, "anything")
        expected = {(1, 1): "anything"}
        self.assertEqual(actual, expected)

    def test_rewrite_out_of_bounds(self):
        actual = rewrite({}, 0, 0, "anything")
        expected = {}
        self.assertEqual(actual, expected)

    def test_rewrite_area_out_of_bounds(self):
        actual = rewrite({}, 0, 0, "anything", 5)
        expected = {}
        self.assertEqual(actual, expected)

    def test_rewrite_area_to_out_of_bounds(self):
        actual = rewrite({}, 1, 1, "anything", 5)
        expected = {(-1, -1): 'anything',
                    (-1, 0): 'anything',
                    (-1, 1): 'anything',
                    (-1, 2): 'anything',
                    (-1, 3): 'anything',
                    (0, -1): 'anything',
                    (0, 0): 'anything',
                    (0, 1): 'anything',
                    (0, 2): 'anything',
                    (0, 3): 'anything',
                    (1, -1): 'anything',
                    (1, 0): 'anything',
                    (1, 1): 'anything',
                    (1, 2): 'anything',
                    (1, 3): 'anything',
                    (2, -1): 'anything',
                    (2, 0): 'anything',
                    (2, 1): 'anything',
                    (2, 2): 'anything',
                    (2, 3): 'anything',
                    (3, -1): 'anything',
                    (3, 0): 'anything',
                    (3, 1): 'anything',
                    (3, 2): 'anything',
                    (3, 3): 'anything'}
        self.assertEqual(actual, expected)