import unittest

from tests.helpers.guess_letter_assertions import GuessLetterAssertions


class PerfectLoss(unittest.TestCase):
    word = "MISSISSIPPI"
    unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    wrong_letters = set()

    # Perfect loss means that the user never guess a single letter right.
    def test_perfect_loss(self):
        # Has not won or lost yet, wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"R"},
            "R"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "R"},
            "A"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "R", "N"},
            "N"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "R", "N", "O"},
            "O"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "R", "N", "O", "T"},
            "T"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "J", "R", "N", "O", "T"},
            "J"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "J", "R", "N", "O", "T", "Z"},
            "Z"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "J", "R", "N", "O", "T", "W", "Z"},
            "W"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "J", "R", "V", "N", "O", "T", "W", "Z"},
            "V"
        )

        # Has not won or lost yet, another wrong guess
        GuessLetterAssertions().assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "G", "J", "R", "V", "N", "O", "T", "W", "Z"},
            "G"
        )

        # Finally, user has lost the game.

        GuessLetterAssertions().assert_guess_letter_user_lost(
            self.word,
            self.unfilled_word,
            self.unfilled_word,
            self.wrong_letters,
            {"A", "F", "G", "J", "R", "V", "N", "O", "T", "W", "Z"},
            "F"
        )


if __name__ == '__main__':
    unittest.main()
