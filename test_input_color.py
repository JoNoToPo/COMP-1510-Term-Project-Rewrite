from unittest import TestCase

from text import input_color


class Test(TestCase):
    def test_input_color_just_text_color_black(self):
        actual = input_color("string", "RED")
        expected = "\033[31mstring\033[0m"
        self.assertEqual(expected, actual)

    def test_input_color_text_and_background_color(self):
        actual = input_color("string", "YELLOW", "BLACK")
        expected = "\033[33m\033[40mstring\033[0m"
        self.assertEqual(expected, actual)

    def test_input_color_just_text_color_red(self):
        actual = input_color("string", "BLACK")
        expected = "\033[30mstring\033[0m"
        self.assertEqual(expected, actual)
