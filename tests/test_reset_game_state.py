import unittest
from unittest.mock import patch

from src.reset_game_state import reset_game_state


class ResetGameState(unittest.TestCase):
    # As generate_random_word connects to an API, we mock it out to avoid
    # spamming the API and providing more accuracy if something is maybe wrong
    # with the API.
    # Also providing more speed.
    def setUp(self):
        self.unfinished_word = ["_", "_", "_", "_", "_", "_", "_"]

        # Start the patcher for the generate_random_word function call
        self.mock_generate_random_word = patch(
            "src.reset_game_state.generate_random_word"
        ).start()
        # Set the return value of the mocked function call (generate_random_word)
        self.mock_generate_random_word.return_value = "hardcoded"

        self.reset_game = reset_game_state()
        self.new_word = "hardcoded"

    def test_reset_game_state_unfinished_word(self):
        self.assertEqual(
            len(self.reset_game["unfilled_word"]), len(self.reset_game["new_word"])
        )

    def test_reset_game_state_wrong_letters(self):
        self.assertEqual(self.reset_game["wrong_letters"], set())

    def test_reset_game_state_new_word(self):
        reset_game = reset_game_state()
        self.assertEqual(reset_game["new_word"], self.new_word)

    def tearDown(self):
        patch.stopall()


if __name__ == "__main__":
    unittest.main()
