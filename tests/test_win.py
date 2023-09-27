import unittest

from src.won_lost import win


class Win(unittest.TestCase):
    def test_win_won(self):
        did_win = win(["t", "e", "s", "t"], "test")
        self.assertTrue(did_win)

    def test_did_not_win(self):
        did_win = win(["t", "e", "s", "t"], "testing_machine")
        self.assertFalse(did_win)


if __name__ == '__main__':
    unittest.main()
