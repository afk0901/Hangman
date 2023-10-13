"""
Contains methods that handle the given letter.

Such as the positions of the letter or wrong letter.
"""


def letter_positions(word, letter):
    """
    If word contains the letter, then return their positions in the string.

    :param word: The existing word
    :param letter: Letter that's being guessed
    :return: List of the letter positions.
             If they do not exist, then an empty array is returned.
    """
    positions = []

    for index, _ in enumerate(word):
        if word[index] == letter:
            positions.append(index)
    return positions


def fill_in_letter(unfilled_word, letter, positions):
    """
    Fill in a letter to an unfilled word such as <letter> _ _ _ _ ...

    :param unfilled_word: Word that's not complete, such as <letter> _ _ _ _ ...
    :param letter: The letter to fill in
    :param positions: The positions of the letter in the word
    :return: List with the letter in the correct place.
    """
    # Create a copy of the unfilled_word list to avoid side effects.
    filled_word = unfilled_word.copy()

    for pos in positions:
        filled_word[pos] = letter
    return filled_word
