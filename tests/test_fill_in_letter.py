import unittest

from src.main import fill_in_letter


class FillInWord(unittest.TestCase):

    # The correct word is Mississippi.

    def test_fill_in_letters_M_and_s(self):
        word_only_m_filled = ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        word_m_and_s_filled = ["M", "_", "s", "s", "_", "s", "s", "_", "_", "_", "_"]

        unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        fill_in_letter(unfilled_word, "M", [0])

        self.assertEqual(unfilled_word, word_only_m_filled)

        fill_in_letter(unfilled_word, "s", [2, 3, 5, 6])

        self.assertEqual(unfilled_word, word_m_and_s_filled)

# TODO: Test for wrong letters and letters that are already there.


if __name__ == '__main__':
    unittest.main()
