import unittest

from tests.helpers.assert_wrong_10_times import (
    AssertNeitherWonOrLost10Times,
)
from tests.helpers.guess_letter_assertions import GuessLetterAssertions


class PerfectLoss(unittest.TestCase):
    # User needs 11 wrong guesses to lose the game
    # so ensuring that's the case.
    # This is the case when the user only makes wrong guesses.

    AssertNeitherWonOrLost10Times()

    def test_perfect_loss_neither_won_eleven_incorrect(self):
        word = "MISSISSIPPI"
        unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

        previous_wrong_letters = {"A", "R", "N", "L", "B", "C", "D", "E", "F", "G"}
        GuessLetterAssertions().assert_guess_letter_user_lost(
            word,
            unfilled_word,
            unfilled_word,
            previous_wrong_letters,
            {"A", "R", "N", "L", "B", "C", "D", "E", "F", "G", "H"},
            "H",
        )


if __name__ == "__main__":
    unittest.main()
