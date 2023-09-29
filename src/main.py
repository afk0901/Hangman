import random

from src.guess_letter import guess_letter
from src.won_lost import lost, win


def generate_random_word():
    """
    Generates a random word from an array.
    :return: A random word
    """
    #words = ['appelsínusafi', 'amma', 'mamma', 'pabbi']
    return "orange"#random.choice(words)


if __name__ == '__main__':
    word = "Orange"
    wrong_letters = set()
    unfilled_word = []

    # Populating unfilled word
    for w in word:
        unfilled_word.append("_")

    while True:
        letter = input()
        guess_letter(unfilled_word, word, letter, wrong_letters)
        print(unfilled_word)
        print("Wrong letters:")
        print(wrong_letters)
        if win(unfilled_word, word):
            print("YOU WON! CONGRATULATIONS! THIS IS THE WORD!")
            break
        elif lost(wrong_letters):
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            break

