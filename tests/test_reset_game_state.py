import unittest

from src.main import reset_game_state


class ResetGameState(unittest.TestCase):
    def test_reset_game_state(self):
        word = "Chicken"
        reset_game_state(word)


if __name__ == "__main__":
    unittest.main()
