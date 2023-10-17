"""This is the file where you should run the whole system. Puts everything together."""

from src.guess_letter import guess_letter
from src.input_validation import input_validation
from src.won_lost import lost, win
from src.word_generation import populate_unfilled_word, generate_random_word
from src.reset_game_state import reset_game_state

from src.logs.logging_setup import log


def main():
    logger = log()
    logger.info("Game starts")
    word = generate_random_word()
    wrong_letters: set[str] = set()
    unfilled_word = populate_unfilled_word(word)
    logger.info(f"The generated word is: {word}")
    logger.info(f"The unfilled word is: {unfilled_word}")
    logger.info(f"Wrong letters are: {wrong_letters}")

    TRY_AGAIN = "y"

    while TRY_AGAIN == "y":
        print(unfilled_word)
        print("Wrong letters:")
        print(wrong_letters)
        letter = input()
        logger.info(f"User typed in: {letter}")

        while input_validation(letter, wrong_letters):
            print("invalid input")
            letter = input()
            logger.info(f"User typed in: {letter}")

        unfilled_word = guess_letter(unfilled_word, word, letter, wrong_letters)[
            "unfilled_word"
        ]
        wrong_letters = guess_letter(unfilled_word, word, letter, wrong_letters)[
            "wrong_letters"
        ]

        logger.info(f"The generated word is: {word}")
        logger.info(f"The unfilled word is: {unfilled_word}")
        logger.info(f"Wrong letters are: {wrong_letters}")

        if win(unfilled_word, word):
            logger.info(f"User has won the game.")
            print(unfilled_word)
            print("YOU WON! CONGRATULATIONS! THIS IS THE WORD!")
            print("Press y to try again :) ")
            TRY_AGAIN = input().lower()
            logger.info(f"User typed in: {TRY_AGAIN}")

        elif lost(wrong_letters):
            logger.info("User has lost the game.")
            print(unfilled_word)
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            print("The word is: ")
            print(word)
            print("Press y to try again :) Press any key than y to quit.")
            TRY_AGAIN = input().lower()
            logger.info(f"User typed in: {TRY_AGAIN}")

        if win(unfilled_word, word) or lost(wrong_letters):
            logger.info("Resetting game state")
            reset_game = reset_game_state()
            word = reset_game["new_word"]
            unfilled_word = reset_game["unfilled_word"]
            wrong_letters = set()

            logger.info(f"The new word is: {word}")
            logger.info(f"The new unfilled word is: {unfilled_word}")
            logger.info(f"Wrong letters are: {wrong_letters}")

        logger.info("Game ends")


if __name__ == "__main__":
    main()
