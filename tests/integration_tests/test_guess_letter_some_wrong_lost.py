import unittest

from src.guess_letter import guess_letter
from src.won_lost import win, lost


class SomeLettersWrongLost(unittest.TestCase):

    def setUp(self) -> None:
        self.word = "MISSISSIPPI"
        self.unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.wrong_letters = set()

    def test_guess_letter_some_letters_wrong_lost(self):
        # User guesses some letters wrong and loses the game

        # Wrong letter
        guess_letter(self.unfilled_word, self.word, "U", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"U"})
        self.assertEqual(self.unfilled_word, ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        #TODO: We use this very often to check for the win and lost status
        # so put this into a helper function.

        did_lost = win(self.unfilled_word, self.word)
        did_win = lost(self.wrong_letters)
        self.assertFalse(did_win)
        self.assertFalse(did_lost)

        # Correct letter
        guess_letter(self.unfilled_word, self.word, "M", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"U"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # assert_win_loss

        # Wrong letter
        guess_letter(self.unfilled_word, self.word, "C", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"C", "U"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # assert_win_loss

        # Wrong letter
        guess_letter(self.unfilled_word, self.word, "D", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"C", "U", "D"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # assert_win_loss

        # Wrong letter
        guess_letter(self.unfilled_word, self.word, "C", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"C", "D", "U"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # assert_win_loss

        guess_letter(self.unfilled_word, self.word, "V", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"C", "D", "U", "V"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # assert_win_loss

        guess_letter(self.unfilled_word, self.word, "F", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"C", "D", "F", "U", "V"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # TODO: CONTINUE

if __name__ == '__main__':
    unittest.main()
