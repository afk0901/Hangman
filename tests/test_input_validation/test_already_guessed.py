import unittest

from src.input_validation import _already_guessed


class AlreadyGuessed(unittest.TestCase):
    def test_already_guessed_already_guessed(self):
        with self.assertRaises(ValueError):
            _already_guessed("a", {"a", "c", "d"})

    def test_not_already_guessed_already_guessed(self):
        self.assertEqual(_already_guessed("o", {"a", "c", "d"}), None)


if __name__ == "__main__":
    unittest.main()
