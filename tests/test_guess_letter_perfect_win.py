import unittest

from tests.helpers.guess_letter_assertions import GuessLetterAssertions


# What happens when the user wins?
class GuessLetterPerfectWin(unittest.TestCase):
    word = "Banana"

    def test_letter_B(self):
        unfilled_word = ["_", "_", "_", "_", "_" "_"]
        previous_wrong_letters = set()
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            ["B", "_", "_", "_", "_" "_"],
            unfilled_word,
            previous_wrong_letters,
            previous_wrong_letters,
            "B",
        )

    def test_letter_a(self):
        unfilled_word = ["B", "_", "_", "_", "_", "_"]
        previous_wrong_letters = set()
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            ["B", "a", "_", "a", "_", "a"],
            unfilled_word,
            previous_wrong_letters,
            previous_wrong_letters,
            "a",
        )

    def test_user_won(self):
        unfilled_word = ["B", "a", "_", "a", "_", "a"]
        previous_wrong_letters = set()
        GuessLetterAssertions().assert_guess_letter_user_won(
            unfilled_word,
            self.word,
            "n",
            previous_wrong_letters,
            ["B", "a", "n", "a", "n", "a"],
            previous_wrong_letters,
        )


if __name__ == "__main__":
    unittest.main()
