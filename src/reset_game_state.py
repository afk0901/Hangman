from src.word_generation import generate_random_word, populate_unfilled_word


def reset_game_state():
    """
    Resets the game state to the initial state.

    :return: A dictionary of unfilled_word and wrong_letters
    in its initial state and generates a new word and stores
    in the dictionary as new_word.
    """
    new_word = generate_random_word()
    unfinished_word = populate_unfilled_word(new_word)
    return {
        "unfilled_word": unfinished_word,
        "wrong_letters": set(),
        "new_word": new_word,
    }
