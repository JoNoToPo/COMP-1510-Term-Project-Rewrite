from unittest import TestCase

from player import move
from text import input_color


class Test(TestCase):
    def test_move_d_wall(self):
        test_map2 = {(1, 1): ' D '}
        action = move('d', {'x_coordinate': 1, 'y_coordinate': 1, 'symbol': ' D '}, test_map2)
        expected_action = ("/////////////You walk into the wall"
                           "/and feel quite silly."
                           "//to move up type w and enter"
                           "/to move left type a and enter"
                           "/to move down type s and enter"
                           "/to move right type d and enter"
                           "//////////////////")
        expected_map = {(1, 1): ' D '}
        self.assertEqual(action, expected_action)
        self.assertEqual(test_map2, expected_map)

    def test_move_d_time_machine(self):
        test_map3 = {(1, 1): ' D ', (1, 2): input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}
        action = move('d', {'x_coordinate': 1, 'y_coordinate': 1, 'symbol': ' D '}, test_map3)
        expected_action = {'x_coordinate': 2, 'y_coordinate': 1, 'symbol': ' D '}
        expected_map = {(1, 1): '   ', (1, 2): ' D '}
        self.assertEqual(action, expected_action)
        self.assertEqual(test_map3, expected_map)

    def test_move_w_wall(self):
        test_map = {(2, 1): ' D '}
        action = move('w', {'x_coordinate': 1, 'y_coordinate': 2, 'symbol': ' D '}, test_map)
        expected_action = ("/////////////You walk into the wall"
                           "/and feel quite silly."
                           "//to move up type w and enter"
                           "/to move left type a and enter"
                           "/to move down type s and enter"
                           "/to move right type d and enter"
                           "//////////////////")
        expected_map = {(2, 1): ' D '}
        self.assertEqual(action, expected_action)
        self.assertEqual(test_map, expected_map)

    def test_move_w_time_machine(self):
        test_map = {(2, 1): ' D ', (1, 1): input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}
        action = move('w', {'x_coordinate': 1, 'y_coordinate': 2, 'symbol': ' D '}, test_map)
        expected_action = {'x_coordinate': 1, 'y_coordinate': 1, 'symbol': ' D '}
        expected_map = {(2, 1): '   ', (1, 1): ' D '}
        self.assertEqual(action, expected_action)
        self.assertEqual(test_map, expected_map)

    def test_move_time_machine_false(self):
        test_map = {(1, 1): ' D ', (1, 2): input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}
        action = move('d', {'x_coordinate': 1, 'y_coordinate': 1, 'symbol': ' D '}, test_map, False)
        expected_action = ("/////////////You walk into the wall"
                           "/and feel quite silly."
                           "//to move up type w and enter"
                           "/to move left type a and enter"
                           "/to move down type s and enter"
                           "/to move right type d and enter"
                           "//////////////////")
        expected_map = {(1, 1): ' D ', (1, 2): input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}
        self.assertEqual(action, expected_action)
        self.assertEqual(test_map, expected_map)
