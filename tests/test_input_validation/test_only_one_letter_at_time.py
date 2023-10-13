import unittest

from src.input_validation import only_one_letter_at_time


class OnlyOneLetterAtTime(unittest.TestCase):
    def test_only_one_letter_at_time_dont_raise_error_on_one_letter(self):
        # Should not produce exception
        self.assertEqual(only_one_letter_at_time("f"), None)

    def test_only_one_letter_at_time_raise_error_on_many_letters(self):
        with self.assertRaises(ValueError):
            only_one_letter_at_time("fd")

    def test_only_one_letter_at_time_raise_exception_on_empty_string(self):
        with self.assertRaises(ValueError):
            only_one_letter_at_time("")


if __name__ == "__main__":
    unittest.main()
