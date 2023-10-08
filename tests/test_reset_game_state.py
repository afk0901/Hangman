import unittest

from src.main import reset_game_state


class ResetGameState(unittest.TestCase):
    def test_reset_game_state(self):
        ...
        # word = "Chicken"
        # wrong_letters = {"a", "t", "z"}
        # unfilled_word = ["m", "i", "s", "s", "i", "n", "g", "c", "h", "i", "c", "k"]
        # game_state = reset_game_state()
        # # The word should be Chicken now, so unfilled word needs to change.
        # self.assertEqual(unfilled_word, ["_", "_", "_", "_", "_", "_", "_"])
        # # And of course no wrong letters
        # # self.assertEqual(wrong_letters, {})


if __name__ == "__main__":
    unittest.main()
