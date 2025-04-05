from unittest import TestCase

from map import display_text_next_to_map


class Test(TestCase):
    def test_display_text_next_to_map_test(self):
        actual = display_text_next_to_map({}, "this/is/a/test")
        expected = {(0, 31): '  this', (1, 31): '  is', (2, 31): '  a', (3, 31): '  test'}
        self.assertEqual(actual, expected)

    def test_display_text_next_to_map_basecase(self):
        actual = display_text_next_to_map({}, "basecase")
        expected = {(0, 31): '  basecase'}
        self.assertEqual(actual, expected)

    def test_display_text_next_to_map_2_rows_down(self):
        actual = display_text_next_to_map({}, "basecase", 2)
        expected = {(2, 31): '  basecase'}
        self.assertEqual(actual, expected)

    def test_display_text_next_to_map_many_slashes(self):
        actual = display_text_next_to_map({}, "/////")
        expected = {(0, 31): '  ', (1, 31): '  ', (2, 31): '  ', (3, 31): '  ', (4, 31): '  ', (5, 31): '  '}
        self.assertEqual(actual, expected)

