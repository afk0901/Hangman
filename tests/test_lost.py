import unittest

from src.won_lost import lost


class Lost(unittest.TestCase):
    # If user has guessed 11 times wrong then the user lost the game.
    def test_lost_game_lost(self):
        did_lost = lost({"a", "b", "c", "d", "e", "f", "g", "l", "w", "v", "m"})
        self.assertTrue(did_lost)

    def test_lost_game_not_lost(self):
        did_lost = lost({"a", "b", "c", "d", "e", "f", "g", "x", "z", "o"})
        self.assertFalse(did_lost)


if __name__ == "__main__":
    unittest.main()
