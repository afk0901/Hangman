import unittest

from src.guess_letter import guess_letter
from tests.helpers.lost_won_assertions import LostWonAssertions


class GuessLetterAssertions(unittest.TestCase):
    def assert_guess_letter(
        self,
        word: str,
        unfilled_word: list[str],
        expected_unfilled_word: list[str],
        wrong_letters: set[str],
        expected_wrong_letters: set[str],
        guessed_letter,
    ):
        """
        Asserts if the unfilled word is in the correct state after a wrong guess
        and the letter is in the wrong_letters set.

        :param word: The actual word
        :param unfilled_word: Unfilled word list such as ["_","_","_"]
        :param expected_unfilled_word: Unfilled word list such as ["_","_","_"], the test should expect this list
        :param wrong_letters: Set of wrongly guessed letters from software under test.
        :param expected_wrong_letters: Set of wrongly guessed letters, the test should expect this set.
        :param guessed_letter: Letter that has been guessed
        """
        guess_letter(unfilled_word, word, guessed_letter, wrong_letters)
        self.assertEqual(wrong_letters, expected_wrong_letters)
        self.assertEqual(unfilled_word, expected_unfilled_word)

    def assert_guess_letter_neither_won(
        self,
        word: str,
        unfilled_word: list[str],
        expected_unfilled_word: list[str],
        wrong_letters: set[str],
        expected_wrong_letters: set[str],
        guessed_letter: str,
    ):
        self.assert_guess_letter(
            word,
            unfilled_word,
            expected_unfilled_word,
            wrong_letters,
            expected_wrong_letters,
            guessed_letter,
        )

        # Did not lose, neither did the user win.
        LostWonAssertions().assert_not_lost_not_won(unfilled_word, word, wrong_letters)

    def assert_guess_letter_user_lost(
        self,
        word: str,
        unfilled_word: list[str],
        expected_unfilled_word: list[str],
        wrong_letters: set[str],
        expected_wrong_letters: set[str],
        guessed_letter,
    ):
        self.assert_guess_letter(
            word,
            unfilled_word,
            expected_unfilled_word,
            wrong_letters,
            expected_wrong_letters,
            guessed_letter,
        )

        LostWonAssertions().assert_lost(wrong_letters)

    def assert_guess_letter_user_won(
        self,
        unfilled_word: list[str],
        word: str,
        guessed_letter: str,
        wrong_letters: set[str],
        expected_unfilled_word: list[str],
        expected_wrong_letters: set[str],
    ):
        self.assert_guess_letter(
            word,
            unfilled_word,
            expected_unfilled_word,
            wrong_letters,
            expected_wrong_letters,
            guessed_letter,
        )
        LostWonAssertions().assert_win(word, unfilled_word)


if __name__ == "__main__":
    unittest.main()
