"""Contains methods that tell us if the user lost or won the game."""


def win(unfilled_word: list[str], word: str):
    """
    Check if the user wins the game.

    :param unfilled_word: The word that has been guessed
    :param word: The actual word
    :return: True if game is won False otherwise if not yet won.
    """
    unfinished_word = "".join(unfilled_word)
    return unfinished_word == word


def lost(wrong_guesses: set[str]):
    """
    Check if user loses the game.

    User loses the game when guessed wrong 11 times

    :return: True or False depending on if the game is lost or not
    """
    return len(wrong_guesses) == 11
