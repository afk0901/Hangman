import unittest

from src.input_validation import _no_empty_guess


class NoEmptyGuess(unittest.TestCase):
    def test__no_empty_guess_empty_guess(self):
        with self.assertRaises(ValueError):
            _no_empty_guess("")

    def test__no_empty_guess__no_empty_guess(self):
        self.assertEqual(_no_empty_guess("n"), None)

    def test__no_empty_guess_empty_guess_space(self):
        with self.assertRaises(ValueError):
            _no_empty_guess(" ")


if __name__ == "__main__":
    unittest.main()
