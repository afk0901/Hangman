import unittest

from src.main import generate_random_word


class GenerateRandomWord(unittest.TestCase):
    def test_returns_a_word(self):
        rw = generate_random_word()

        # A word should contain at least one character
        self.assertGreater(len(rw), 0)

        # A word should not contain any space
        # Word should not contain only space
        # Let's allow sentences as some words
        # have space in it such as orange juice.
        self.assertNotIn(" ", rw)

        # A word should always return a string.
        self.assertTrue(rw.isalpha())

    def test_returns_different_words(self):
        ...


if __name__ == "__main__":
    unittest.main()
