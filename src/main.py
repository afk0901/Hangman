"""This is the file where you should run the whole system. Puts everything together."""

from src.guess_letter import guess_letter
from src.input_validation import input_validation
from src.won_lost import lost, win
from src.word_generation import populate_unfilled_word, generate_random_word
from src.reset_game_state import reset_game_state


if __name__ == "__main__":
    word = generate_random_word()
    wrong_letters: set[str] = set()
    unfilled_word = populate_unfilled_word(word)

    TRY_AGAIN = "y"

    while TRY_AGAIN == "y":
        print(unfilled_word)
        print("Wrong letters:")
        print(wrong_letters)
        letter = input()

        while input_validation(letter, wrong_letters):
            print("invalid input")
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
            TRY_AGAIN = input().lower()

        elif lost(wrong_letters):
            print(unfilled_word)
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            print("The word is: ")
            print(word)
            print("Press y to try again :) Press any key than y to quit.")
            TRY_AGAIN = input().lower()

        if win(unfilled_word, word) or lost(wrong_letters):
            reset_game = reset_game_state()
            word = reset_game["new_word"]
            unfilled_word = reset_game["unfilled_word"]
            wrong_letters = set()
