from src.guess_letter import guess_letter
from src.won_lost import lost, win


def generate_random_word():
    """
    Generates a random word from an array.
    :return: A random word
    """
    # TODO: Generate random word from some dataset. Implement a connection to random generator API.

    # words = ['appelsínusafi', 'amma', 'mamma', 'pabbi']
    return "orange"  # random.choice(words)


def populate_unfilled_word(uncompleted_word: list[str], the_word: str):
    # Populating unfilled word
    uncompleted_word.clear()
    for char in the_word:
        uncompleted_word.append("_")
    return uncompleted_word


if __name__ == "__main__":
    word = "Orange"
    wrong_letters = set()
    unfilled_word = []
    populate_unfilled_word(unfilled_word, word)

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
            unfilled_word = populate_unfilled_word(unfilled_word, word)
            wrong_letters.clear()

        elif lost(wrong_letters):
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            print("Press y to try again :) Press any key than y to quit.")
            try_again = input().lower()
            unfilled_word = populate_unfilled_word(unfilled_word, word)
            wrong_letters.clear()
