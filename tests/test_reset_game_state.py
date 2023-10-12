import unittest
from unittest.mock import Mock, patch

from src.main import reset_game_state


class ResetGameState(unittest.TestCase):
    # # As generate_random_word connects to an API, we mock it out to avoid
    # spamming the API and providing more accuracy if something is maybe wrong
    # with the API.
    # Also providing more speed.
    def setUp(self):
        self.unfinished_word = ["_", "_", "_", "_", "_", "_", "_"]
        self.patcher = patch(
            "src.word_generation.generate_random_word",
            return_value="mocked",
        )
        self.mocked_generate_random_word = self.patcher.start()
        self.reset_game = reset_game_state()
        self.new_word = "mocked"

    def test_reset_game_state_unfinished_word(self):
        self.assertEqual(
            len(self.reset_game["unfilled_word"]), len(self.reset_game["new_word"])
        )

    def test_reset_game_state_wrong_letters(self):
        self.assertEqual(self.reset_game["wrong_letters"], set())

    def test_reset_game_state_new_word(self):
        self.assertEqual(self.reset_game["new_word"], self.new_word)

    def tearDown(self):
        # Stop the patcher after the test
        self.patcher.stop()


if __name__ == "__main__":
    unittest.main()
