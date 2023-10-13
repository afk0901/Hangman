"""This module takes care of the input validation of the Hangman game."""


def _only_one_letter_at_time(guessed_letter: str):
    """
    User can only guess one letter at a time.

    :param guessed_letter: Letter or the invalid string that
                           the user guessed.
    Raises ValueError if the length of guessed_letter is not 1
    """
    if len(guessed_letter) != 1:
        raise ValueError


def _only_alphabetic(guess: str):
    """
    Raise ValueError if user guesses non-alphabetical letters.

    :param guess: The user's guess
    """
    if not guess.isalpha():
        raise ValueError


def _no_empty_guess(guess: str):
    """
    Raise ValueError if guess is empty.

    Space is considered to be empty as it makes
    no sense to guess space in the reality.

    :param guess: The letter that the user guesses
    """
    if guess == "" or guess == " ":
        raise ValueError


def _already_guessed(guess: str, wrong_letters: set):
    """
    Raise valueError if the letter is already guessed.

    :param guess: The user's guess
    :param wrong_letters: Set of all the wrong letters that
                          the user has guessed.
    """
    if guess in wrong_letters:
        raise ValueError


def input_validation(guessed_letter: str, wrong_letters: set):
    """
    Validate the user's input. Returns False if no error True otherwise.

    :param guessed_letter: The letter the user guessed.
    :param wrong_letters:  The wrongly guessed letters.
    :return: True if input is okay, False otherwise
    """
    guessed_letter = guessed_letter.lower()
    try:
        _only_one_letter_at_time(guessed_letter)
        _already_guessed(guessed_letter, wrong_letters)
        _only_alphabetic(guessed_letter)
        _no_empty_guess(guessed_letter)
    except ValueError:
        return True
    return False
