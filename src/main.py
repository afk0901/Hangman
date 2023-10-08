from src.guess_letter import guess_letter
from src.won_lost import lost, win
from src.word_generation import populate_unfilled_word, generate_random_word


# TODO: User can only guess one letter at time not many letters

# TODO: If user puts in a word that contains other than characters raise error.

# TODO: Ensure capitalized letters are lowered

# TODO: Dissallow Non-alphanumeric characteres

# TODO: Dissallow duplicate guesses and empty inputs

# TODO: Ensure utf-8 encoding


def reset_game_state(the_word: str, unfinished_word: list[str]):
    """
    Resets the game state to the initial state
    :param the_word:
    :param unfinished_word:
    #:param the_wrong_letters:

    :return: Unfinished word that has been cleared.
            (Only underscores)
    """
    ...
    # the_wrong_letters.clear()
    unfinished_word = populate_unfilled_word(the_word)
    return True


if __name__ == "__main__":
    word = generate_random_word()
    print(word)
    wrong_letters = set()
    unfilled_word = populate_unfilled_word(word)

    try_again = "y"

    while try_again == "y":
        print(unfilled_word)
        letter = input()
        guess_letter(unfilled_word, word, letter, wrong_letters)
        print(unfilled_word)
        print("Wrong letters:")
        print(wrong_letters)

        if win(unfilled_word, word):
            print("YOU WON! CONGRATULATIONS! THIS IS THE WORD!")
            print("Press y to try again :) ")
            try_again = input().lower()
            # reset_game_state(word, unfilled_word, wrong_letters)

        elif lost(wrong_letters):
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            print("Press y to try again :) Press any key than y to quit.")
            try_again = input().lower()
            unfilled_word = populate_unfilled_word(word)
            wrong_letters.clear()
            # reset_game_state()
