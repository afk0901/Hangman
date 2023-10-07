import json
import unittest
import httpretty
import requests

from src.word_generation import generate_random_word


class GenerateRandomWord(unittest.TestCase):
    def test_generate_random_word_request_ok(self):
        # Monkey patching the socket module
        httpretty.enable(verbose=True, allow_net_connect=False)

        # Faking the request
        httpretty.register_uri(
            httpretty.GET,
            "https://random-word-api.herokuapp.com/word",
            body='["pogonophorans"]',
        )

        self.assertEqual("pogonophorans", generate_random_word())

        httpretty.disable()  # disable afterward, so that you will have no problems in code that uses that socket module
        httpretty.reset()  # reset HTTPretty state (clean up registered urls and request history)

    def test_generate_random_word_API_down(self):
        # When the API is broken, raise error.

        # Monkey patching the socket module
        httpretty.enable(verbose=True, allow_net_connect=False)

        # Faking the request, producing 500 server errors
        httpretty.register_uri(
            httpretty.GET,
            "https://random-word-api.herokuapp.com/word",
            status=500,
            body="Internal Server Error",
        )

        # Was discovering that Python uses __enter__ and __exit__
        # to control resources when we use if and self.assertRaises(RuntimeError)
        # is a context-manager. It performs a setup with __enter__ method
        # then performs a cleanup in the __exit__ method.
        #
        # This is just genius because then you get rid of resource
        # setups and cleanups such as try...catch and finally,
        # and many resources such as databases, files, and more.
        # This also reduces the probability of incorrect setup
        # and teardown of the resource.

        with self.assertRaises(RuntimeError):
            generate_random_word()

    def test_generate_random_word_resource_not_found(self):
        ...

    def test_generate_random_word_no_internet_connection(self):
        ...


if __name__ == "__main__":
    unittest.main()
