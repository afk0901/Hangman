"""
Handles what happens when the user guesses a letter.
"""
from src.letter import letter_positions, fill_in_letter


def guess_letter(unfilled_word, word, letter, wrongly_guessed_letters):
    """
    Fills in the letter if it's in the word otherwise
    appends to the wrongly_guessed_letter array.

    :param unfilled_word: Word that's not complete such as: <letter> _ _ _ _ ...
    :param letter: Guessed letter
    :param word: The actual word
    :param wrongly_guessed_letters:
        Letters that already exist and are wrong.
        Empty if no letters have been guessed.
    """
    positions = letter_positions(word, letter)
    fill_in_letter(unfilled_word, letter, positions)
    # TODO: Correct letter, do the above. Incorrect letter,
    #  fill in the wrongly_guessed letters and add to wrong guesses


def wrong_letter_guessed(word, letter):
    """
     Determines if the user guessed the wrong letter.
    :param word: The actual word
    :param letter: The guessed letter
    :return: boolean depending on if the letter
             is in the word or not.
    """
    return letter not in word


def letter_already_guessed(unfilled_word, letter):
    """
    Determines if the user has already guessed the letter

    :param unfilled_word: unfilled_word: Word that's not complete such as: <letter> _ _ _ _ ...
    :param letter: The guessed letter
    :return: True if user has already guessed the letter
             otherwise False
    """
    return letter in "".join(unfilled_word)
