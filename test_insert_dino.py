from unittest import TestCase
from unittest.mock import patch
from player import insert_dino


class Test(TestCase):
    @patch("random.randint", side_effect=[1])
    def test_insert_dino_after_first_letter(self, _):
        actual = insert_dino("Jefferson")
        expected = "Jdinoefferson"
        self.assertEqual(actual, expected)

    @patch("random.randint", side_effect=[8])
    def test_insert_dino_before_last_letter(self, _):
        actual = insert_dino("Jefferson")
        expected = "Jeffersodinon"
        self.assertEqual(actual, expected)

    @patch("random.randint", side_effect=[3])
    def test_insert_dino_only_changes_last_word(self, _):
        actual = insert_dino("\"The Axe\" Morgan")
        expected = "\"The Axe\" Mordinogan"
        self.assertEqual(actual, expected)
