"""
Contains methods that tells us if the user lost or won the game.
"""


def win(unfilled_word, word):
    """
    Did the user win the game?

    :param unfilled_word: The word that has been guessed
    :param word: The actual word
    :return: True if game is won False otherwise if not yet won.
    """
    unfilled_word = "".join(unfilled_word)
    return unfilled_word == word


def lost(wrong_guesses):
    """
    Did the user lost the game?
    User looses the game when guessed wrong 11 times
    :return: True or False depending on if the game is lost or not
    """
    return len(wrong_guesses) == 11
