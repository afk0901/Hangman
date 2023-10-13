def only_one_letter_at_time(guessed_letter: str):
    """
    User can only guess one letter at a time.
    :param guessed_letter: Letter or the invalid string that
                           the user guessed.
    Raises ValueError if the length of guessed_letter is not 1
    """
    if len(guessed_letter) != 1:
        raise ValueError


def only_alphabetic(guess: str):
    """
    Raises ValueError if user guesses non-alphabetical letters.
    :param guess: The user's guess
    """
    if not guess.isalpha():
        raise ValueError


def no_empty_guess(guess: str):
    """
    Raises ValueError if guess is empty.
    Space is considered to be empty as it makes
    no sense to guess space in the reality.
    :param guess: The letter that the user guesses
    """
    if guess == "" or guess == " ":
        raise ValueError


def already_guessed(guess: str, wrong_letters: set):
    """
    Raises valueError if the letter is already guessed.
    :param guess: The user's guess
    :param wrong_letters: Set of all the wrong letters that
                          the user has guessed.
    """
    if guess in wrong_letters:
        raise ValueError


def input_validation():
    # TODO: Check if each of the validation method raises
    # exception.

    # TODO: User can only guess one letter at time not many letters

    # TODO: If user puts in a word that contains other than characters raise error.

    # TODO: Dissallow Non-alphanumeric characteres

    # TODO: Ensure capitalized letters are lowered
    #  (Put to lower case in the beginning)

    # TODO: Dissallow empty inputs

    # TODO: User gets a message if letter has already been guessed.

    ...
