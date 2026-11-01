import os
import tempfile
from unittest import TestCase
from timeline import rewrite_history, load_timeline, save_timeline, ORIGINAL_HISTORY


class Test(TestCase):
    def setUp(self):
        self.file_name = os.path.join(tempfile.mkdtemp(), "timeline.json")

    def character(self, level, **history):
        return {"level": level, "name": "Chris The Wise", "timeline": {**ORIGINAL_HISTORY, **history}}

    def test_rewrite_history_killing_hitler_brings_goudier(self):
        actual = rewrite_history(self.character(2), self.file_name)
        expected = {"hitler_killed": True, "dinosaurs": False, "boss_name": ""}
        self.assertEqual(actual, expected)

    def test_rewrite_history_killing_goudier_brings_hitler_back(self):
        save_timeline({"hitler_killed": True, "dinosaurs": False, "boss_name": ""}, self.file_name)
        actual = rewrite_history(self.character(2, hitler_killed=True), self.file_name)
        expected = {"hitler_killed": False, "dinosaurs": False, "boss_name": ""}
        self.assertEqual(actual, expected)

    def test_rewrite_history_stopping_the_meteor_keeps_dinosaurs(self):
        actual = rewrite_history(self.character(3), self.file_name)
        expected = {"hitler_killed": False, "dinosaurs": True, "boss_name": ""}
        self.assertEqual(actual, expected)

    def test_rewrite_history_meteor_falling_brings_humans_back(self):
        save_timeline({"hitler_killed": False, "dinosaurs": True, "boss_name": ""}, self.file_name)
        actual = rewrite_history(self.character(3, dinosaurs=True), self.file_name)
        expected = {"hitler_killed": False, "dinosaurs": False, "boss_name": ""}
        self.assertEqual(actual, expected)

    def test_rewrite_history_winner_becomes_boss(self):
        actual = rewrite_history(self.character(4), self.file_name)
        expected = {"hitler_killed": False, "dinosaurs": False, "boss_name": "Chris The Wise"}
        self.assertEqual(actual, expected)

    def test_rewrite_history_level_one_changes_nothing(self):
        rewrite_history(self.character(1), self.file_name)
        self.assertFalse(os.path.exists(self.file_name))

    def test_rewrite_history_is_saved(self):
        rewrite_history(self.character(2), self.file_name)
        actual = load_timeline(self.file_name)
        expected = {"hitler_killed": True, "dinosaurs": False, "boss_name": ""}
        self.assertEqual(actual, expected)

    def test_load_timeline_corrupt_file(self):
        with open(self.file_name, "w") as file_object:
            file_object.write("not json")
        actual = load_timeline(self.file_name)
        self.assertEqual(actual, ORIGINAL_HISTORY)
