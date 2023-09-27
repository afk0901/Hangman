"""
Contains methods that handles the given letter,
such as the positions of the letter or
wrong letter.
"""


def letter_positions(word, letter):
    """
    If word contains letter then return their positions
    in the string.

    :param word: The existing word
    :param letter: Letter that's being guessed
    :return: Array of the positions of the letters.
    If they do not exist then empty array is returned.
    """
    positions = []
    for index, _ in enumerate(word):
        if word[index] == letter:
            positions.append(index)
    return positions


def fill_in_letter(unfilled_word, letter, positions):
    """
    Fills in a letter to an unfilled word such as: <letter> _ _ _ _ ...

    :param unfilled_word: Word that's not complete such as: <letter> _ _ _ _ ...
    :param letter: The letter to fill in
    :param positions: The positions of the letter in the word
    :return: Array with the letter filled in among with existing letters
    """
    for pos in positions:
        unfilled_word[pos] = letter

