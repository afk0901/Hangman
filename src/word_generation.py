import json

import requests

"""
This module contains methods to generate words for the Hangman game.
That includes generating a word with no letters.
"""


def populate_unfilled_word(the_word: str):
    """
    Populates an unfilled word from the actual word.
    Such as test -> ["_" "_" "_" "_"]
    :param the_word: The actual word
    :return: List of underscores. List length is equal the_word length
    """
    uncompleted_word = []
    for char in range(len(the_word)):
        uncompleted_word.append("_")
    return uncompleted_word


def generate_random_word() -> str:
    """
    Generates a random word from an API.
    If the API is down, a random element
    from a fallback array is returned
    and the error is logged for further inspection if needed.
    :return: A random word
    """

    resp = requests.get("https://random-word-api.herokuapp.com/word")

    # TODO: Check if the user has an internet connection.
    # Next version.
    # This may happen even tho the user have.
    # Just print no internet connection or check your connection.
    # or provide a fallback?
    # for now, the user has to figure it by himself.

    # TODO: Regenerate the word if it's not alphanumeric
    # Let's do that in the next version. The API we are
    # using now should always do so.

    return json.loads(resp.content)[0]  # Deserialize and return one word.
