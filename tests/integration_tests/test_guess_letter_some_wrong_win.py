import unittest

from src.guess_letter import guess_letter
from src.won_lost import win


# Integration test that tests when a user guesses the wrong letter
# but does win the game.

# Does not test user input. Only pre-defined guesses.


class SomeLettersWrongWin(unittest.TestCase):

    def setUp(self) -> None:
        self.word = "MISSISSIPPI"
        self.unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.wrong_letters = set()

    def test_guess_letter_some_letters_wrong_win(self):
        # User guesses some letters wrong but still wins the game.

        # Correct latter
        guess_letter(self.unfilled_word, self.word, "M", self.wrong_letters)
        self.assertEqual(self.wrong_letters, set())

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Wrong latter
        guess_letter(self.unfilled_word, self.word, "Z", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Wrong letter again, same letter
        guess_letter(self.unfilled_word, self.word, "Z", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Wrong letter again, different letter
        guess_letter(self.unfilled_word, self.word, "D", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"D", "Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Wrong letter again, different letter
        guess_letter(self.unfilled_word, self.word, "E", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"D", "E", "Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Correct letter
        guess_letter(self.unfilled_word, self.word, "S", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"D", "E", "Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "S", "S", "_", "S", "S", "_", "_", "_", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Correct letter
        guess_letter(self.unfilled_word, self.word, "P", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"D", "E", "Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "S", "S", "_", "S", "S", "_", "P", "P", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Wrong letter
        guess_letter(self.unfilled_word, self.word, "K", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"D", "E", "K", "Z"})
        self.assertEqual(self.unfilled_word, ["M", "_", "S", "S", "_", "S", "S", "_", "P", "P", "_"])

        # Did not win yet
        did_win = win(self.unfilled_word, self.word)
        self.assertFalse(did_win)

        # Correct letter
        guess_letter(self.unfilled_word, self.word, "I", self.wrong_letters)
        self.assertEqual(self.wrong_letters, {"D", "E", "K", "Z"})
        self.assertEqual(self.unfilled_word, ["M", "I", "S", "S", "I", "S", "S", "I", "P", "P", "I"])

        # Did win
        did_win = win(self.unfilled_word, self.word)
        self.assertTrue(did_win)


if __name__ == '__main__':
    unittest.main()
