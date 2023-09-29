"""
Handles what happens when the user guesses a letter.
"""
from src.letter import letter_positions, fill_in_letter


def guess_letter(unfilled_word: list[str],
                 word: str,
                 letter: str,
                 wrong_letters: set[str]):
    """
    Fills in the letter if it's in the word otherwise
    appends to the wrongly_guessed_letter array.

    :param unfilled_word: Word that's not complete, such as <letter> _ _ _ _ ...
    :param letter: Guessed letter
    :param word: The actual word
    :param wrong_letters:
        Set of letters that already exist and are wrong.
        Empty if no letters have been guessed.
    """
    positions = letter_positions(word, letter)
    fill_in_letter(unfilled_word, letter, positions)

    if wrong_letter_guessed(word, letter):
        wrong_letters.add(letter)

    #TODO: If user puts in a word that contains other than characters
    # raise error.


def wrong_letter_guessed(word, letter):
    """
     Determines if the user guessed the wrong letter.
    :param word: The actual word
    :param letter: The guessed letter
    :return: boolean depending on if the letter
             is in the word or not.
    """
    return letter not in word
