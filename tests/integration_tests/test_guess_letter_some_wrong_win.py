import unittest

from tests.helpers.guess_letter_assertions import GuessLetterAssertions


# Integration test that tests when a user guesses the wrong letter
# but does win the game.

# Does not test user input. Only pre-defined guesses.


class SomeLettersWrongWin(unittest.TestCase):
    word = "MISSISSIPPI"
    unfilled_word = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    wrong_letters = set()
    guess_letterAssertions = GuessLetterAssertions()

    def test_guess_letter_some_letters_wrong_win(self):
        # User guesses some letters wrong but still wins the game.

        # Correct letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            self.wrong_letters,
            "M",
        )

        # Wrong latter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"Z"},
            "Z",
        )

        # Wrong letter again, same letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"Z"},
            "Z",
        )

        # Wrong letter again, different letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"D", "Z"},
            "D",
        )

        # Wrong letter again, different letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            self.wrong_letters,
            {"D", "E", "Z"},
            "E",
        )

        # Correct letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "S", "S", "_", "S", "S", "_", "_", "_", "_"],
            self.wrong_letters,
            {"D", "E", "Z"},
            "S",
        )

        # Correct letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "S", "S", "_", "S", "S", "_", "P", "P", "_"],
            self.wrong_letters,
            {"D", "E", "Z"},
            "P",
        )

        # Wrong letter

        self.guess_letterAssertions.assert_guess_letter_neither_won(
            self.word,
            self.unfilled_word,
            ["M", "_", "S", "S", "_", "S", "S", "_", "P", "P", "_"],
            self.wrong_letters,
            {"D", "E", "K", "Z"},
            "K",
        )

        # Correct letter

        self.guess_letterAssertions.assert_guess_letter_user_won(
            self.unfilled_word,
            self.word,
            "I",
            self.wrong_letters,
            ["M", "I", "S", "S", "I", "S", "S", "I", "P", "P", "I"],
            {"D", "E", "K", "Z"},
        )


if __name__ == "__main__":
    unittest.main()
