import unittest
import httpretty

from src.word_generation import generate_random_word

"""
Contains tests for the API that generates random words for us.
"""


class GenerateRandomWordAPITest(unittest.TestCase):
    def setUp(self):
        # Monkey patching the socket module
        httpretty.enable(verbose=True, allow_net_connect=False)

    def test_generate_random_word_request_ok(self):
        # Faking the request
        httpretty.register_uri(
            httpretty.GET,
            "https://random-word-api.herokuapp.com/word",
            body='["pogonophorans"]',
        )

        self.assertEqual("pogonophorans", generate_random_word())

    def test_generate_random_word_API_broken(self):
        # When the API doesnt return JSON response, raise error.

        # Faking the request, producing illegal JSON.
        httpretty.register_uri(
            httpretty.GET,
            "https://random-word-api.herokuapp.com/word",
            body="{I'm not a legal JSON response",
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

        # Using Exception because to simulate behavior
        # better instead of relying on a package.

        with self.assertRaises(Exception):
            generate_random_word()

    def test_generate_random_word_resource_not_found(self):
        # Faking the request, producing 500 server errors
        httpretty.register_uri(
            httpretty.GET,
            "https://random-word-api.herokuapp.com/testertestyflopp",
            status=404,
            body="[{}]",
        )

        with self.assertRaises(Exception):
            generate_random_word()

    def test_generate_random_word_no_internet_connection(self):
        # Next version problem
        ...

    def tearDown(self):
        # disable afterward, so that you will have no problems in code that uses that socket module
        httpretty.disable()
        # reset HTTPretty state (clean up registered urls and request history)
        httpretty.reset()


if __name__ == "__main__":
    unittest.main()
