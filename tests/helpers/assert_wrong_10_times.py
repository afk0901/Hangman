import unittest

from tests.helpers.guess_letter_assertions import GuessLetterAssertions


class AssertNeitherWonOrLost10Times(unittest.TestCase):

    """
    Tests if user neither won nor lost, 10 times to check on the
    wrong letters.
    """

    word = "MISSISSIPPI"
    unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    def test_perfect_loss_neither_won_one_incorrect(self):
        previous_wrong_letters = set()
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"R"},
            "R",
        )

    def test_perfect_loss_neither_won_two_incorrect(self):
        previous_wrong_letters = {"R"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R"},
            "A",
        )

    def test_perfect_loss_neither_won_three_incorrect(self):
        previous_wrong_letters = {"A", "R"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N"},
            "N",
        )

    def test_perfect_loss_neither_won_four_incorrect(self):
        previous_wrong_letters = {"A", "R", "N"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L"},
            "L",
        )

    def test_perfect_loss_neither_won_five_incorrect(self):
        previous_wrong_letters = {"A", "R", "N", "L"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B"},
            "B",
        )

    def test_perfect_loss_neither_won_six_incorrect(self):
        previous_wrong_letters = {"A", "R", "N", "L", "B"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B", "C"},
            "C",
        )

    def test_perfect_loss_neither_won_seven_incorrect(self):
        previous_wrong_letters = {"A", "R", "N", "L", "B", "C"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B", "C", "D"},
            "D",
        )

    def test_perfect_loss_neither_won_eight_incorrect(self):
        previous_wrong_letters = {"A", "R", "N", "L", "B", "C", "D"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B", "C", "D", "E"},
            "E",
        )

    def test_perfect_loss_neither_won_nine_incorrect(self):
        previous_wrong_letters = {"A", "R", "N", "L", "B", "C", "D", "E"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B", "C", "D", "E", "F"},
            "F",
        )

    def test_perfect_loss_neither_won_ten_incorrect(self):
        previous_wrong_letters = {"A", "R", "N", "L", "B", "C", "D", "E", "F"}
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B", "C", "D", "E", "F", "G"},
            "G",
        )


if __name__ == "__main__":
    unittest.main()
