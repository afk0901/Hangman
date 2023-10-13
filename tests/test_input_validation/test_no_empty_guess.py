import unittest

from src.input_validation import no_empty_guess


class NoEmptyGuess(unittest.TestCase):
    def test_no_empty_guess_empty_guess(self):
        with self.assertRaises(ValueError):
            no_empty_guess("")

    def test_no_empty_guess_no_empty_guess(self):
        self.assertEqual(no_empty_guess("n"), None)

    def test_no_empty_guess_empty_guess_space(self):
        with self.assertRaises(ValueError):
            no_empty_guess(" ")


if __name__ == "__main__":
    unittest.main()
