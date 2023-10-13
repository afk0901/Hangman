import unittest

from src.input_validation import only_alphabetic


class OnlyAlphabetic(unittest.TestCase):
    def test_only_alphabetic_alphabetic_does_not_raise_exception(self):
        self.assertEqual(only_alphabetic("abcde"), None)

    def test_only_alphabetic_alphabetic_does_not_raise_exception_ð(self):
        self.assertEqual(only_alphabetic("ð"), None)

    def test_only_alphabetic_alphabetic_does_not_raise_exception_ö(self):
        self.assertEqual(only_alphabetic("ö"), None)

    def test_only_alphabetic_alphabetic_does_not_raise_exception_þ(self):
        self.assertEqual(only_alphabetic("þ"), None)

    def test_only_alphabetic_alphabetic_does_not_raise_exception_æ(self):
        self.assertEqual(only_alphabetic("æ"), None)

    def test_only_alphabetic_number_raises_ValueError(self):
        with self.assertRaises(ValueError):
            only_alphabetic("abc123ff")

    def test_only_alphabetic_special_char_raises_ValueError(self):
        with self.assertRaises(ValueError):
            only_alphabetic("abc!#$%&%##%'$$''$'")


if __name__ == "__main__":
    unittest.main()
