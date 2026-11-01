from unittest import TestCase
from initialize import block_corridor


class Test(TestCase):
    def test_block_corridor_first_corridor_tile(self):
        test_map = {(1, 1): "@", (1, 2): "   ", (1, 3): "   ", (1, 4): "D", (5, 5): "P"}
        actual = block_corridor({"y_coordinate": 5, "x_coordinate": 5, "symbol": "P"}, test_map, {(1, 1): "   "},
                                (1, 1), (1, 4))
        expected = {"y_coordinate": 1, "x_coordinate": 2, "symbol": "P"}
        self.assertEqual(actual, expected)

    def test_block_corridor_old_place_cleared(self):
        test_map = {(1, 1): "@", (1, 2): "   ", (1, 3): "D", (5, 5): "P"}
        block_corridor({"y_coordinate": 5, "x_coordinate": 5, "symbol": "P"}, test_map, {(1, 1): "   "},
                       (1, 1), (1, 3))
        expected = {(1, 1): "@", (1, 2): "P", (1, 3): "D", (5, 5): "   "}
        self.assertEqual(test_map, expected)

    def test_block_corridor_skips_start_room_and_wide_area(self):
        test_map = {(1, 1): "@", (1, 2): "   ", (2, 2): "   ", (1, 3): "   ", (2, 3): "   ",
                    (1, 4): "   ", (1, 5): "D", (5, 5): "P"}
        actual = block_corridor({"y_coordinate": 5, "x_coordinate": 5, "symbol": "P"}, test_map,
                                {(1, 1): "   ", (1, 2): "   "}, (1, 1), (1, 5))
        expected = {"y_coordinate": 1, "x_coordinate": 4, "symbol": "P"}
        self.assertEqual(actual, expected)

    def test_block_corridor_no_corridor_uses_first_tile_outside_start_room(self):
        test_map = {(1, 1): "@", (1, 2): "   ", (2, 2): "   ", (1, 3): "D", (2, 3): "   ", (5, 5): "P"}
        actual = block_corridor({"y_coordinate": 5, "x_coordinate": 5, "symbol": "P"}, test_map, {(1, 1): "   "},
                                (1, 1), (1, 3))
        expected = {"y_coordinate": 1, "x_coordinate": 2, "symbol": "P"}
        self.assertEqual(actual, expected)

    def test_block_corridor_goal_unreachable(self):
        test_map = {(1, 1): "@", (1, 3): "D", (5, 5): "P"}
        actual = block_corridor({"y_coordinate": 5, "x_coordinate": 5, "symbol": "P"}, test_map, {(1, 1): "   "},
                                (1, 1), (1, 3))
        expected = {"y_coordinate": 5, "x_coordinate": 5, "symbol": "P"}
        self.assertEqual(actual, expected)
