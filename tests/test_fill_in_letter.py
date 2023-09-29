import unittest

from src.letter import fill_in_letter


class FillInWord(unittest.TestCase):
    # The correct word is Mississippi.

    unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    def test_fill_in_letters_M_and_s(self):
        word_only_m_filled = ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
        word_m_and_s_filled = ["M", "_", "s", "s", "_", "s", "s", "_", "_", "_", "_"]

        fill_in_letter(self.unfilled_word, "M", [0])

        self.assertEqual(self.unfilled_word, word_only_m_filled)

        fill_in_letter(self.unfilled_word, "s", [2, 3, 5, 6])

        self.assertEqual(self.unfilled_word, word_m_and_s_filled)

    # TODO: Test for wrong letters and letters that are already there.

    # TODO: Ensure that only one letter is allowed, not many

    def test_only_one_letter_allowed(self):
        fill_in_letter(self.unfilled_word, "xx")


if __name__ == "__main__":
    unittest.main()
