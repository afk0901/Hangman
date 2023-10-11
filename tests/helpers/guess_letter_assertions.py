import unittest

from src.guess_letter import guess_letter
from tests.helpers.lost_won_assertions import LostWonAssertions


class GuessLetterAssertions(unittest.TestCase):
    def assert_guess_letter(
        self,
        unfilled_word: list[str],
        expected_unfilled_word: list[str],
        wrong_letters: set[str],
        expected_wrong_letters: set[str],
    ):
        """
        Asserts if the unfilled word is in the correct state after a wrong guess
        and the wrong letter set is correct.

        :param unfilled_word: Unfilled word list such as ["_","_","_"]
        :param expected_unfilled_word: an Unfilled word list such as ["_","_","_"], the test should expect this list
        :param wrong_letters: Set of wrongly guessed letters from software under test.
        :param expected_wrong_letters: Set of wrongly guessed letters, the test should expect this set.
        """
        self.assertEqual(wrong_letters, expected_wrong_letters)
        self.assertEqual(unfilled_word, expected_unfilled_word)

    def assert_guess_letter_neither_won(
        self,
        word: str,
        expected_unfilled_word,
        unfilled_word: list[str],
        wrong_letters: set[str],
        expected_wrong_letters: set[str],
        letter: str,
    ):
        unfilled_word_wrong_letters = guess_letter(
            unfilled_word, word, letter, wrong_letters
        )

        self.assert_guess_letter(
            unfilled_word_wrong_letters["unfilled_word"],
            expected_unfilled_word,
            unfilled_word_wrong_letters["wrong_letters"],
            expected_wrong_letters,
        )
        # Did not lose, neither did the user win.
        LostWonAssertions().assert_neither_won(unfilled_word, word, wrong_letters)

    def assert_guess_letter_user_lost(
        self,
        word: str,
        unfilled_word: list[str],
        expected_unfilled_word: list[str],
        wrong_letters: set[str],
        expected_wrong_letters: set[str],
        letter,
    ):
        unfilled_word_wrong_letters = guess_letter(
            unfilled_word, word, letter, wrong_letters
        )

        self.assert_guess_letter(
            unfilled_word_wrong_letters["unfilled_word"],
            expected_unfilled_word,
            unfilled_word_wrong_letters["wrong_letters"],
            expected_wrong_letters,
        )

        LostWonAssertions().assert_lost(unfilled_word_wrong_letters["wrong_letters"])

    def assert_guess_letter_user_won(
        self,
        unfilled_word: list[str],
        word: str,
        letter: str,
        wrong_letters: set[str],
        expected_unfilled_word: list[str],
        expected_wrong_letters: set[str],
    ):
        unfilled_word_wrong_letters = guess_letter(
            unfilled_word, word, letter, wrong_letters
        )

        self.assert_guess_letter(
            unfilled_word_wrong_letters["unfilled_word"],
            expected_unfilled_word,
            unfilled_word_wrong_letters["wrong_letters"],
            expected_wrong_letters,
        )

        LostWonAssertions().assert_win(
            word, unfilled_word_wrong_letters["unfilled_word"]
        )


if __name__ == "__main__":
    unittest.main()
