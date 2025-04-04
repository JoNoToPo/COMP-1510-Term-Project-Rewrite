from unittest import TestCase

from map import room_combiner


class Test(TestCase):
    def test_room_combiner_two_spots(self):
        actual = room_combiner({(1, 1): '   '}, {(1, 2): '   '})
        expected = {(1, 1): '   ', (1, 2): '   '}
        self.assertEqual(actual, expected)

    def test_room_combiner_overlap(self):
        actual = room_combiner({(1, 1): '   '}, {(1, 1): '   '})
        expected = {(1, 1): '   '}
        self.assertEqual(actual, expected)

    def test_room_combiner_overlap_one_spot_but_other_spots_from_both_rooms(self):
        actual = room_combiner({(1, 1): '   ', (1, 2): '   '}, {(1, 2): '   ', (2, 2): '   '})
        expected = {(1, 1): '   ', (1, 2): '   ', (2, 2): '   '}
        self.assertEqual(actual, expected)