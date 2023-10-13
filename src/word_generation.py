"""
This module contains methods to generate words for the Hangman game.

That includes generating a word with no letters.
"""

import json

import requests


def populate_unfilled_word(the_word: str):
    """
    Populate an unfilled word from the actual word. Such as test -> ["_" "_" "_" "_"].

    :param the_word: The actual word
    :return: List of underscores. List length is equal the_word length
    """
    uncompleted_word = []
    for char in range(len(the_word)):
        uncompleted_word.append("_")
    return uncompleted_word


def generate_random_word() -> str:
    """
    Generate a random word from an API.

    :return: A random word
    """
    resp = requests.get("https://random-word-api.herokuapp.com/word", timeout=60)
    return json.loads(resp.content)[0]  # Deserialize and return one word.
