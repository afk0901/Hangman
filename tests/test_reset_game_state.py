import unittest
from unittest.mock import Mock, patch

from src.main import reset_game_state


class ResetGameState(unittest.TestCase):
    unfinished_word = ["_", "_", "_", "_", "_", "_", "_"]

    def test_reset_game_state_unfinished_word(self):
        reset_game = reset_game_state("Chicken")
        self.assertEqual(reset_game["unfilled_word"], self.unfinished_word)

    def test_reset_game_state_wrong_letters(self):
        reset_game = reset_game_state("Chicken")
        self.assertEqual(reset_game["wrong_letters"], set())

    # As generate_random_word connects to an API, we mock it out to avoid
    # spamming the API and providing more accuracy if something is maybe wrong
    # with the API.
    # Also providing more speed.

    # TODO: Find out why the mock is not working as expected
    @patch("src.word_generation.generate_random_word", new=Mock(return_value="Mocked"))
    def test_reset_game_state_new_word(self):
        reset_game = reset_game_state("Chicken")
        self.assertNotEqual(reset_game["new_word"], "Chicken")

    # TODO: Mock the API - cant really make this test properly without a mock
    def test_reset_game_state_new_word_length(self):
        reset_game = reset_game_state("Chicken")
        self.assertEqual(len(reset_game["unfilled_word"]), len(reset_game["new_word"]))


if __name__ == "__main__":
    unittest.main()
