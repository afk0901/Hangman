import unittest

from src.main import letter_positions


class LetterPositions(unittest.TestCase):

    def test_word_does_not_contain_the_letter(self):
        word_not_contains_o = letter_positions('test', 'o')
        self.assertEqual(word_not_contains_o, [])

    def test_word_does_contain_the_letter(self):
        word_contains_e = letter_positions('tester', 'e')
        self.assertEqual(word_contains_e, [1, 4])


if __name__ == '__main__':
    unittest.main()
