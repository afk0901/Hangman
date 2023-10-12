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
        self.reset_game = reset_game_state()
        self.new_word = "mocked"

    def test_reset_game_state_unfinished_word(self):
        self.assertEqual(
            len(self.reset_game["unfilled_word"]), len(self.reset_game["new_word"])
        )

    def test_reset_game_state_wrong_letters(self):
        self.assertEqual(self.reset_game["wrong_letters"], set())

    def test_reset_game_state_new_word(self):
        reset_game = reset_game_state()
        self.assertEqual(reset_game["new_word"], "mocked")

    @patch("src.main.generate_random_word")
    def test_reset_game_state(self, mock_generate_random_word):
        # Set the return value of the mocked function
        mock_generate_random_word.return_value = "hardcoded"

        game_state = reset_game_state()

        # Now, whenever reset_game_state is called within this test, generate_random_word will return 'hardcoded'
        self.assertEqual(game_state["new_word"], "hardcoded")


if __name__ == "__main__":
    unittest.main()
