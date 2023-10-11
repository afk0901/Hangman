from src.guess_letter import guess_letter
from src.won_lost import lost, win
from src.word_generation import populate_unfilled_word, generate_random_word


# TODO: User can only guess one letter at time not many letters

# TODO: If user puts in a word that contains other than characters raise error.

# TODO: Ensure capitalized letters are lowered

# TODO: Dissallow Non-alphanumeric characteres

# TODO: Dissallow duplicate guesses and empty inputs

# TODO: Ensure utf-8 encoding

# TODO: User gets a message if letter has already been guessed.


def reset_game_state(the_word: str):
    """
    Resets the game state to the initial state.
    :param the_word: The actual word

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


if __name__ == "__main__":
    word = generate_random_word()
    # word = "nonconstruction"
    print(word)
    wrong_letters = set()
    unfilled_word = populate_unfilled_word(word)

    try_again = "y"

    while try_again == "y":
        print(word)
        print(unfilled_word)
        print("Wrong letters:")
        print(wrong_letters)
        letter = input()

        unfilled_word = guess_letter(unfilled_word, word, letter, wrong_letters)[
            "unfilled_word"
        ]
        wrong_letters = guess_letter(unfilled_word, word, letter, wrong_letters)[
            "wrong_letters"
        ]

        if win(unfilled_word, word):
            print(unfilled_word)
            print("YOU WON! CONGRATULATIONS! THIS IS THE WORD!")
            print("Press y to try again :) ")
            try_again = input().lower()

        elif lost(wrong_letters):
            print(unfilled_word)
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            print("Press y to try again :) Press any key than y to quit.")
            try_again = input().lower()

        if win(unfilled_word, word) or lost(wrong_letters):
            word = reset_game_state(word)["new_word"]
            unfilled_word = reset_game_state(word)["unfilled_word"]
            wrong_letters = set()
