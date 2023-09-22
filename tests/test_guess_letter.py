import unittest

from src.main import guess_letter, win


# Let's play Hangman! Tests the whole functionality.

class GuessLetter(unittest.TestCase):

    def setUp(self) -> None:
        # Initial state
        self.word = "Mississippi"
        self.unfilled_word = ["", "", "", "", "", "", "", "", "", "", ""]
        self.guessed_letters = []

    def test_guess_letters_no_errors_perfect_win(self):

        # First guess - guessing i
        guess_letter(self.unfilled_word, self.word, "i",
                     self.guessed_letters)

        self.assertEqual(self.unfilled_word,
                         ["", "i", "", "", "i", "", "", "i", "", "", "i"])

        # Did not win yet.
        self.assertEqual(win(self.unfilled_word, self.word), False)

        # Next guess - guessing M
        guess_letter(self.unfilled_word, self.word, "M",
                     self.guessed_letters)

        self.assertEqual(self.unfilled_word,
                         ["M", "i", "", "", "i", "", "", "i", "", "", "i"])

        # Did not win yet.
        self.assertEqual(win(self.unfilled_word, self.word), False)

        # Next guess - guessing p
        guess_letter(self.unfilled_word, self.word, "p",
                     self.guessed_letters)

        self.assertEqual(self.unfilled_word,
                         ["M", "i", "", "", "i", "", "", "i", "p", "p", "i"])

        # Did not win yet.
        self.assertEqual(win(self.unfilled_word, self.word), False)

        # Next guess - guessing s
        guess_letter(self.unfilled_word, self.word, "s",
                     self.guessed_letters)

        self.assertEqual(self.unfilled_word,
                         ["M", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"])

        # Did win
        self.assertEqual(win(self.unfilled_word, self.word), True)

    def test_guess_letters_lost_the_game(self):
        ...

    def test_guess_letters_wrong_letter(self):
        ...

    def test_guess_letters_letter_already_guessed(self):
        ...








if __name__ == '__main__':
    unittest.main()
