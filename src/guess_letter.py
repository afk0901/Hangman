"""This module handles what happens when the user guesses a letter."""

from src.letter import letter_positions, fill_in_letter


def guess_letter(
    unfilled_word: list[str], word: str, letter: str, wrong_letters: set[str]
):
    """
    Fill in the letter if it's in the word otherwise append to the wrongly_guessed_letter array.

    :param unfilled_word: Word that's not complete, such as <letter> _ _ _ _ ...
    :param letter: Guessed letter
    :param word: The actual word
    :param wrong_letters:
        Set of letters that already exist and are wrong.
        Empty if no letters have been guessed.

    :returns: A dictionary of the unfilled word and the wrong letters
    """
    positions = letter_positions(word, letter)

    unfilled_word = fill_in_letter(unfilled_word, letter, positions)

    # So that we are not changing the parameter reference,
    # then we make a copy.

    the_wrong_letters = wrong_letters.copy()
    if wrong_letter_guessed(word, letter):
        the_wrong_letters.add(letter)
    return {"unfilled_word": unfilled_word, "wrong_letters": the_wrong_letters}


def wrong_letter_guessed(word, letter):
    """
     Determine if the user guesses the wrong letter.

    :param word: The actual word
    :param letter: The guessed letter
    :return: boolean depending on if the letter
             is in the word or not.
    """
    return letter not in word
