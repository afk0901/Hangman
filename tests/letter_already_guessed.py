import unittest

from src.guess_letter import letter_already_guessed


class LetterAlreadyGuessed(unittest.TestCase):
    def setUp(self) -> None:
        # WATCH OUT! can't contain o as it's used to check for a non-existing letter!
        self.partially_filled_word = [
            "_",
            "_",
            "a",
            "_",
            "b",
            "_",
            "_",
            "c",
            "_",
            "_",
            "_",
        ]

    def test_letter_already_guessed_already_guessed(self):
        already_guessed = letter_already_guessed(self.partially_filled_word, "b")
        self.assertTrue(already_guessed)

    def test_letter_already_guessed_not_already_guessed(self):
        already_guessed = letter_already_guessed(self.partially_filled_word, "o")
        self.assertFalse(already_guessed)


if __name__ == "__main__":
    unittest.main()
