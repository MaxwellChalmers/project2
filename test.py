import os
import unittest

from giphyAPI import GiphyAPI

API_KEY = os.environ["GIF_KEY"]


class TestAPI(unittest.TestCase):

    def test_Trending(self):
        api = GiphyAPI(API_KEY)
        trending = api.callTrending()
        self.assertIsInstance(trending, dict)

    def test_Search(self):
        api = GiphyAPI(API_KEY)
        search = api.callSearch()

        self.assertIsInstance(search, dict)


class TestCLI(unittest.TestCase):

    def test_Trending(self):
        self.assertTrue(True)

    def test_Search(self):
        self.assertTrue(True)

    def test_Lucky(self):
        self.assertTrue(True)

    def test_Markdown(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
