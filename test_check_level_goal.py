from tabnanny import check
from unittest import TestCase

from levels import check_level_goal


class Test(TestCase):
    def test_check_level_goal_(self):
        actual = check_level_goal([{"name": "anything else"}])
        expected = True
        self.assertEqual(actual, expected)

    def test_check_level_goal_hitler(self):
        actual = check_level_goal([{"name": "Hitler"}])
        expected = False
        self.assertEqual(actual, expected)

    def test_check_level_goal_meteor(self):
        actual = check_level_goal([{"name": "meteor"}])
        expected = False
        self.assertEqual(actual, expected)

    def test_check_level_goal_dummy(self):
        actual = check_level_goal([{"name": "Dummy"}])
        expected = False
        self.assertEqual(actual, expected)

    def test_check_level_goal_GREATEST_GRANDFATHER(self):
        actual = check_level_goal([{"name": "GREATEST GRANDFATHER"}])
        expected = False
        self.assertEqual(actual, expected)

    def test_check_level_goal_empty(self):
        actual = check_level_goal([])
        expected = True
        self.assertEqual(actual, expected)

