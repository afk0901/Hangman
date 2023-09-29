import unittest

from src.guess_letter import wrong_letter_guessed


class WrongLetter(unittest.TestCase):
    def test_wrong_letter_guessed_wrong_letter_guessed(self):
        # Guessing b that's not in the word.
        wrong_letter = wrong_letter_guessed("tester", "b")
        self.assertTrue(wrong_letter)

    def test_wrong_letter_correct_letter_guessed(self):
        # Guessing e that's in the word.
        wrong_letter = wrong_letter_guessed("tester", "e")
        self.assertFalse(wrong_letter)


if __name__ == "__main__":
    unittest.main()
