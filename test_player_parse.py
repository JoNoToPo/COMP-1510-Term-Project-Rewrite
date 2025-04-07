from unittest import TestCase
from unittest.mock import patch

from player import player_parse


class Test(TestCase):
    @patch("player.move", side_effect=["you walk up"])
    def test_player_parse_move_up(self, _):
        actual = player_parse("w", {},
                              {}, True)
        expected = "you walk up"
        self.assertEqual(actual, expected)

    @patch("player.move", side_effect=["you walk"])
    def test_player_parse_move_left(self, _):
        actual = player_parse("a", {},
                              {}, True)
        expected = "you walk"
        self.assertEqual(actual, expected)

    @patch("player.move", side_effect=["you walk"])
    def test_player_parse_move_down(self, _):
        actual = player_parse("s", {},
                              {}, True)
        expected = "you walk"
        self.assertEqual(actual, expected)

    @patch("player.move", side_effect=["you walk"])
    def test_player_parse_move_right(self, _):
        actual = player_parse("d", {},
                              {}, True)
        expected = "you walk"
        self.assertEqual(actual, expected)

    @patch("player.player_rewrite", side_effect=["you rewrite"])
    def test_player_parse_rewrite_up(self, _):
        actual = player_parse("rw", {},
                              {}, True)
        expected = "you rewrite"
        self.assertEqual(actual, expected)

    @patch("player.player_rewrite", side_effect=["you rewrite"])
    def test_player_parse_rewrite_left(self, _):
        actual = player_parse("ra", {},
                              {}, True)
        expected = "you rewrite"
        self.assertEqual(actual, expected)

    @patch("player.player_rewrite", side_effect=["you rewrite"])
    def test_player_parse_rewrite_down(self, _):
        actual = player_parse("rs", {},
                              {}, True)
        expected = "you rewrite"
        self.assertEqual(actual, expected)

    @patch("player.player_rewrite", side_effect=["you rewrite"])
    def test_player_parse_rewrite_right(self, _):
        actual = player_parse("rd", {},
                              {}, True)
        expected = "you rewrite"
        self.assertEqual(actual, expected)

    def test_player_parse_help(self):
        actual = player_parse("help", {},
                              {}, True)
        expected = (f"{"-" * 53}"
                    "/             ,--.  ,--.       ,--.           "
                    "/             |  '--'  | ,---. |  | ,---.     "
                    "/             |  .--.  || .-. :|  || .-. |    "
                    "/             |  |  |  |\\   --.|  || '-' '    "
                    "/             `--'  `--' `----'`--'|  |-'     "
                    "/----------------------------------`--'---------------/"
                    "/Welcome to Rewrite!"
                    "/To move use 'w' to move up, 'a' to move left "
                    "/'s' to move down and 'd' to move right then press enter."
                    "//To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                    "/for a more complete guide on rewriting simply type 'r' and enter"
                    "//Once anything is rewritten it will display as a corrupted tile."
                    "/corrupted tiles change your perception of reality, and act as barriers."
                    "/however the space surrounding remains the same even if it looks different."
                    "/if you rewrite a corrupted tile, "
                    "/it is erased from existence leaving "
                    "/nothing but floor behind."
                    "/Be careful what you rewrite. You could end up "
                    "/erasing yourself from existence if you are not careful."
                    "/after you are finished with the goal in a level,"
                    "/move to the time machine ' T ' and you will continue the story.")
        self.assertEqual(actual, expected)

    def test_player_parse_(self):
        actual = player_parse("other input", {},
                              {}, True)
        expected = ("///////////"
                    "Invalid Input,"
                    "//To move type 'w', 'a', 's', or 'd' then press enter"
                    "//To rewrite type 'rw', 'ra', 'rs', or 'rd then press enter'"
                    "//to get help type 'help' then press enter"
                    "///////////")
        self.assertEqual(actual, expected)

