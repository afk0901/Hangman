import unittest

from src.guess_letter import guess_letter
from src.won_lost import win, lost

# Integration test that tests what happens
# when the user guesses a letter and makes a perfect win.
# Perfect win is when the user guesses no wrong letters.
#
# Does not test user input. Only pre-defined guesses.


class GuessLetterPerfectWin(unittest.TestCase):
    def setUp(self) -> None:
        # Initial state
        self.word = "Mississippi"
        self.unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.wrongly_guessed_letters = set()

    def test_guess_letters_no_errors_perfect_win(self):
        # First guess - guessing i
        guess_letter(self.unfilled_word, self.word, "i", self.wrongly_guessed_letters)

        self.assertEqual(
            self.unfilled_word, ["_", "i", "_", "_", "i", "_", "_", "i", "_", "_", "i"]
        )

        # Did not win yet.
        self.assertEqual(win(self.unfilled_word, self.word), False)

        # Did not lose yet and no wrongly guessed letters.
        self.assertEqual(lost(self.wrongly_guessed_letters), 0)

        # Next guess - guessing M
        guess_letter(self.unfilled_word, self.word, "M", self.wrongly_guessed_letters)

        self.assertEqual(
            self.unfilled_word, ["M", "i", "_", "_", "i", "_", "_", "i", "_", "_", "i"]
        )

        # Did not win yet.
        self.assertEqual(win(self.unfilled_word, self.word), False)

        # Did not lose yet and no wrongly guessed letters.
        self.assertEqual(lost(self.wrongly_guessed_letters), 0)

        # Next guess - guessing p
        guess_letter(self.unfilled_word, self.word, "p", self.wrongly_guessed_letters)

        self.assertEqual(
            self.unfilled_word, ["M", "i", "_", "_", "i", "_", "_", "i", "p", "p", "i"]
        )

        # Did not win yet.
        self.assertEqual(win(self.unfilled_word, self.word), False)

        # Did not lose yet and no wrongly guessed letters.
        self.assertEqual(lost(self.wrongly_guessed_letters), 0)

        # Next guess - guessing s
        guess_letter(self.unfilled_word, self.word, "s", self.wrongly_guessed_letters)

        self.assertEqual(
            self.unfilled_word, ["M", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
        )

        # Did win
        self.assertEqual(win(self.unfilled_word, self.word), True)

        # Did not lose and no wrongly guessed letters.
        self.assertEqual(lost(self.wrongly_guessed_letters), 0)


if __name__ == "__main__":
    unittest.main()
