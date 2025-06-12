from unittest import TestCase

from initialize import initialize_player


class Test(TestCase):
    def test_initialize_player_lvl_1(self):
        test_player = {"level": 0, "area": -1, "x_coordinate": 0, "y_coordinate": 0}
        test_time_machine = {"x_coordinate": 1, "y_coordinate": 1}
        actual = initialize_player(test_player, test_time_machine)
        expected = {'level': 1, 'area': 1, 'x_coordinate': 1, 'y_coordinate': 1}
        self.assertEqual(actual, expected)

    def test_initialize_player_lvl_2(self):
        test_player = {"level": 1, "area": 1, "x_coordinate": 0, "y_coordinate": 0}
        test_time_machine = {"x_coordinate": 1, "y_coordinate": 1}
        actual = initialize_player(test_player, test_time_machine)
        expected = {'level': 2, 'area': 3, 'x_coordinate': 1, 'y_coordinate': 1}
        self.assertEqual(actual, expected)
