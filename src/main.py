import random


def generate_random_word():
    """
    Generates a random word from an array.
    :return: A random word
    """
    #words = ['appelsínusafi', 'amma', 'mamma', 'pabbi']
    return "orange"#random.choice(words)


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


def guess_letter(unfilled_word, word, letter, wrongly_guessed_letters):
    """
    Fills in the letter if it's in the word otherwise
    appends to the existing letters

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
    User looses the game when guessed x many times
    (draw the hangman to find out.)
    :return: True or False depending on if the game is lost or not
    """
    ...


if __name__ == '__main__':
    ...

