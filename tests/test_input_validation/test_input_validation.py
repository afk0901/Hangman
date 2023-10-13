import unittest

from src.input_validation import input_validation


class InputValidation(unittest.TestCase):
    def test_test_input_validation_one_many_letters(self):
        self.assertEqual(input_validation("afdasdasd", set()), True)

    def test_input_validation_one_legit_letter(self):
        self.assertEqual(input_validation("a", set()), False)

    def test_input_validation_already_guessed(self):
        self.assertEqual(input_validation("B", {"a", "b", "c"}), True)

    def test_input_validation_special_characters(self):
        self.assertEqual(input_validation("!", {"a", "b", "c"}), True)

    def test_input_validation_number(self):
        self.assertEqual(input_validation("4", {"a", "b", "c"}), True)

    def test_input_validation_empty(self):
        self.assertEqual(input_validation("", {"a", "b", "c"}), True)

    def test_input_validation_space(self):
        self.assertEqual(input_validation(" ", {"a", "b", "c"}), True)


if __name__ == "__main__":
    unittest.main()
