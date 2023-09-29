from src.won_lost import win, lost
import unittest


class LostWonAssertions(unittest.TestCase):
    """
    This class contains methods that test for the
    winning and loosing states.
    Contains methods to assert when nobody won, the user won,
    or the user lost.
    """

    def assert_not_lost_not_won(
        self, unfilled_word: list[str], word: str, wrong_letters: set[str]
    ):
        """
        Asserts if the user has not lost the game, neither win the game.
        :param: unfilled_word:
        :param: word:

        """
        did_lost = win(unfilled_word, word)
        did_win = lost(wrong_letters)
        self.assertFalse(did_win)
        self.assertFalse(did_lost)

    def assert_win(self, word: str, unfilled_word: list[str]):
        """
         Asserts if the user won the game
        :param word: The actual word
        :param unfilled_word: Incomplete word as a list such as ["_","_","_"]
        """
        did_win = win(unfilled_word, word)
        self.assertTrue(did_win)

    def assert_lost(self, wrong_guesses: set[str]):
        did_lost = lost(wrong_guesses)
        self.assertTrue(did_lost)
