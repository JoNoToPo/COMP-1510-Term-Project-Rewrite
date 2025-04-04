from unittest import TestCase

from map import level_start_display


class Test(TestCase):
    def test_level_start_display_this_is_a_test(self):
        actual = level_start_display("this/is/a/test")
        expected = "  this\n  is\n  a\n  test\n"
        self.assertEqual(actual, expected)

    def test_level_start_display_many_slashes(self):
        actual = level_start_display("////")
        expected = "  \n  \n  \n  \n  \n"
        self.assertEqual(actual, expected)

    def test_level_start_display_empty(self):
        actual = level_start_display("")
        expected = "  \n"
        self.assertEqual(actual, expected)

    def test_level_start_display_basecase(self):
        actual = level_start_display("basecase")
        expected = "  basecase\n"
        self.assertEqual(actual, expected)

