from unittest import TestCase
from levels import meteor_impact


class Test(TestCase):
    def setUp(self):
        self.time_machine = {"y_coordinate": 1, "x_coordinate": 3}
        self.map = {(1, 1): "@", (1, 2): "   ", (1, 3): "T"}

    def dinosaur(self, **extra):
        return {"level": 3, "timeline": {"dinosaurs": True}, "y_coordinate": 1, "x_coordinate": 1, **extra}

    def test_meteor_impact_human_timeline(self):
        actual = meteor_impact({"level": 3, "timeline": {"dinosaurs": False}}, [], self.map, self.time_machine)
        self.assertIsNone(actual)

    def test_meteor_impact_other_level(self):
        actual = meteor_impact({"level": 2, "timeline": {"dinosaurs": True}}, [], self.map, self.time_machine)
        self.assertIsNone(actual)

    def test_meteor_impact_gunners_still_defending(self):
        character = self.dinosaur()
        actual = meteor_impact(character, [{"name": "Raptor Gunner"}], self.map, self.time_machine)
        self.assertIsNone(actual)
        self.assertNotIn("impact", character)

    def test_meteor_impact_starts_from_path_length(self):
        actual = meteor_impact(self.dinosaur(), [{"name": "Great-Grandfather"}], self.map, self.time_machine)
        expected = 3 + 15 - 1
        self.assertEqual(actual, expected)

    def test_meteor_impact_no_path(self):
        actual = meteor_impact(self.dinosaur(), [], {(1, 1): "@"}, self.time_machine)
        expected = 39
        self.assertEqual(actual, expected)

    def test_meteor_impact_lands_on_character(self):
        character = self.dinosaur(impact=1)
        meteor_impact(character, [], self.map, self.time_machine)
        self.assertEqual(self.map[(1, 1)], "demolished by a meteor")
