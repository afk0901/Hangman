import unittest

from src.word_generation import populate_unfilled_word


class UnfilledWord(unittest.TestCase):
    def test_populate_unfilled_word(self):
        unfilled_word = populate_unfilled_word("Mistery")
        self.assertEqual(unfilled_word, ["_", "_", "_", "_", "_", "_", "_"])


if __name__ == "__main__":
    unittest.main()
