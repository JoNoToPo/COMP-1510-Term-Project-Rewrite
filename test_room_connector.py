from unittest import TestCase

from initialize import room_connector


class Test(TestCase):
    def test_room_connector_bottom_left(self):
        actual = room_connector({(1, 1): "   "}, {(3, 3): "   "})
        expected = {(1, 1): '   ', (2, 1): '   ', (3, 1): '   ', (3, 2): '   ', (3, 3): '   '}
        self.assertEqual(actual, expected)

    def test_room_connector_bottom_right(self):
        actual = room_connector({(1, 3): "   "}, {(3, 1): "   "})
        expected = {(1, 3): '   ', (2, 3): '   ', (3, 1): '   ', (3, 2): '   ', (3, 3): '   '}
        self.assertEqual(actual, expected)

    def test_room_connector_top_right(self):
        actual = room_connector({(3, 3): "   "}, {(1, 1): "   "})
        expected = {(1, 1): '   ', (1, 2): '   ', (1, 3): '   ', (2, 3): '   ', (3, 3): '   '}
        self.assertEqual(actual, expected)

    def test_room_connector_top_left(self):
        actual = room_connector({(3, 1): "   "}, {(1, 3): "   "})
        expected = {(1, 1): '   ', (1, 2): '   ', (1, 3): '   ', (2, 1): '   ', (3, 1): '   '}
        self.assertEqual(actual, expected)
