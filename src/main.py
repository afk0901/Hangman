from src.guess_letter import guess_letter
from src.won_lost import lost, win
from src.word_generation import populate_unfilled_word, generate_random_word

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
            unfilled_word = populate_unfilled_word(word)
            wrong_letters.clear()

        elif lost(wrong_letters):
            print("DAMN! YOU LOST THE GAME! HANGEEEEED!")
            print("Press y to try again :) Press any key than y to quit.")
            try_again = input().lower()
            unfilled_word = populate_unfilled_word(word)
            wrong_letters.clear()
