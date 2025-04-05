from unittest import TestCase
from unittest.mock import patch
from initialize import initialize_mob


class Test(TestCase):
    def test_initialize_mob_single_space(self):
        actual = initialize_mob({"y_coordinate": 0, "x_coordinate": 0},
                                {(3, 3): "   "}, {(0, 0): "   "})
        expected = {"y_coordinate": 3, "x_coordinate": 3}
        self.assertEqual(actual, expected)

    def test_initialize_mob_blocked_space(self):
        actual = initialize_mob({"y_coordinate": 0, "x_coordinate": 0},
                                {(0, 0): "   ", (3, 3): "   "}, {(0, 0): "   "})
        expected = {"y_coordinate": 3, "x_coordinate": 3}
        self.assertEqual(actual, expected)

    @patch("random.choice", side_effect=[(1, 1)])
    def test_initialize_mob_random_choice(self, _):
        actual = initialize_mob({"y_coordinate": 0, "x_coordinate": 0},
                                {(0, 0): "   ", (3, 3): "   ", (1, 1): "   "}, {(0, 0): "   "})
        expected = {"y_coordinate": 1, "x_coordinate": 1}
        self.assertEqual(actual, expected)

