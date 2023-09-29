import unittest

from tests.helpers.lost_won_assertions import LostWonAssertions
from tests.helpers.guess_letter_assertions import GuessLetterAssertions


class SomeLettersWrongLost(unittest.TestCase):
    word = "MISSISSIPPI"
    unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    wrong_letters = set()
    lost_won_assertions = LostWonAssertions()
    guess_letter_assertions = GuessLetterAssertions()

    def test_guess_letter_some_letters_wrong_lost(self):
        # User guesses some letters wrong and loses the game

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"U"},
            "U",
        )

        # Correct letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"U"},
            "M",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"C", "U"},
            "C",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"C", "U", "D"},
            "D",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"C", "D", "U", "V"},
            "V",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"C", "D", "F", "U", "V"},
            "F",
        )

        # Correct letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "_", "_", "I", "_", "_", "I", "_", "_", "I"],
            self.wrong_letters,
            {"C", "D", "F", "U", "V"},
            "I",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "_", "_", "I", "_", "_", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "C", "D", "F", "U", "V"},
            "A",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "_", "_", "I", "_", "_", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "B", "C", "D", "F", "U", "V"},
            "B",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "_", "_", "I", "_", "_", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "B", "C", "D", "F", "N", "U", "V"},
            "N",
        )

        # Correct letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "S", "S", "I", "S", "S", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "B", "C", "D", "F", "N", "U", "V"},
            "S",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "S", "S", "I", "S", "S", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "B", "C", "D", "E", "F", "N", "U", "V"},
            "E",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "I", "S", "S", "I", "S", "S", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "B", "C", "D", "E", "F", "N", "U", "V", "Z"},
            "Z",
        )

        # Wrong letter
        self.guess_letter_assertions.assert_guess_letter_user_lost(
            self.word,
            self.unfilled_word,
            ["M", "I", "S", "S", "I", "S", "S", "I", "_", "_", "I"],
            self.wrong_letters,
            {"A", "B", "C", "D", "E", "F", "N", "U", "W", "V", "Z"},
            "W",
        )


if __name__ == "__main__":
    unittest.main()
