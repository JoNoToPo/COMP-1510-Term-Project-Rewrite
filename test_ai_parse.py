from unittest import TestCase
from unittest.mock import patch
from levels import ai_parse


class Test(TestCase):
    @patch("player.move", side_effect=["ai_moves"])
    def test_ai_parse_move(self, _):
        actual = ai_parse({"ai": ["move"]},
                          [], {}, {}, 0,
                          ("w", 0, -1))
        expected = "ai_moves"
        self.assertEqual(actual, expected)

    @patch("levels.shoot", side_effect=["ai_shoot"])
    def test_ai_parse_shoot(self, _):
        actual = ai_parse({"x_coordinate": 2, "y_coordinate": 2, "ai": ["shoot"]},
                          [], {(1, 2): "   "}, {}, 0,
                          ("w", 0, -1))
        expected = "ai_shoot"
        self.assertEqual(actual, expected)

    @patch("levels.shot", side_effect=["ai_shot"])
    def test_ai_parse_shot(self, _):
        actual = ai_parse({"ai": ["shot"], "direction": ("w", 0, -1)},
                          [], {}, {}, 0,
                          ("w", 0, -1))
        expected = "ai_shot"
        self.assertEqual(actual, expected)

    @patch("levels.fall", side_effect=["ai_fall"])
    def test_ai_parse_fall(self, _):
        actual = ai_parse({"ai": ["fall"]},
                          [], {}, {}, 0,
                          ("w", 0, -1))
        expected = "ai_fall"
        self.assertEqual(actual, expected)

    @patch("levels.countdown", side_effect=["ai_countdown"])
    def test_ai_parse_countdown(self, _):
        actual = ai_parse({"ai": ["countdown"]},
                          [], {}, {}, 0,
                          ("w", 0, -1))
        expected = "ai_countdown"
        self.assertEqual(actual, expected)

    @patch("player.player_rewrite", side_effect=["ai_rewrite"])
    def test_ai_parse_rewrite(self, _):
        actual = ai_parse({"ai": ["rewrite"]},
                          [], {}, {}, 0,
                          ("w", 0, -1))
        expected = "ai_rewrite"
        self.assertEqual(actual, expected)


