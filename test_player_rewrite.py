from unittest import TestCase

from player import player_rewrite


class Test(TestCase):
    def test_player_rewrite_wall_with_rewritten_space(self):
        actual = {}
        player_rewrite("w", {'x_coordinate': 1, 'y_coordinate': 2, 'area': 1}, actual)
        expected = {(1, 1): 3}
        self.assertEqual(actual, expected)

    def test_player_rewrite_rewritten_space(self):
        actual = {(1, 1): 3}
        player_rewrite("w", {'x_coordinate': 1, 'y_coordinate': 2, 'area': 1}, actual)
        expected = {(1, 1): "   "}
        self.assertEqual(actual, expected)

    def test_player_rewrite_anything_else_player_rewrite(self):
        actual = {(1, 1): "anything_else"}
        player_rewrite("w", {'x_coordinate': 1, 'y_coordinate': 2, 'area': 1}, actual)
        expected = {(1, 1): 3}
        self.assertEqual(actual, expected)

    def test_player_rewrite_area_3_and_rewritten_space_player_rewrite(self):
        actual = {(1, 2): 3}
        player_rewrite("w", {'x_coordinate': 1, 'y_coordinate': 3, 'area': 3}, actual)
        expected = {(0, 0): 3,
                    (0, 1): 3,
                    (0, 2): 3,
                    (1, 0): 3,
                    (1, 1): 3,
                    (1, 2): '   ',
                    (2, 0): 3,
                    (2, 1): 3,
                    (2, 2): 3}
        self.assertEqual(actual, expected)

    def test_player_rewrite_out_of_bounds(self):
        actual = {}
        player_rewrite("w", {'x_coordinate': 1, 'y_coordinate': 1, 'area': 1}, actual)
        expected = {}
        self.assertEqual(actual, expected)

    def test_player_rewrite_area_out_of_bounds(self):
        actual = {}
        player_rewrite("w", {'x_coordinate': 1, 'y_coordinate': 2, 'area': 3}, actual)
        expected = {}
        self.assertEqual(actual, expected)

    def test_player_rewrite_area_to_out_of_bounds(self):
        actual = {}
        player_rewrite("w", {'x_coordinate': 3, 'y_coordinate': 4, 'area': 5}, actual)
        expected = {(-1, 1): 3,
                    (-1, 2): 3,
                    (-1, 3): 3,
                    (-1, 4): 3,
                    (-1, 5): 3,
                    (0, 1): 3,
                    (0, 2): 3,
                    (0, 3): 3,
                    (0, 4): 3,
                    (0, 5): 3,
                    (1, 1): 3,
                    (1, 2): 3,
                    (1, 3): 3,
                    (1, 4): 3,
                    (1, 5): 3,
                    (2, 1): 3,
                    (2, 2): 3,
                    (2, 3): 3,
                    (2, 4): 3,
                    (2, 5): 3,
                    (3, 1): 3,
                    (3, 2): 3,
                    (3, 3): 3,
                    (3, 4): 3,
                    (3, 5): 3}
        self.assertEqual(actual, expected)
