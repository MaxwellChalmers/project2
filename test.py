import os
import unittest

from giphyAPI import GiphyAPI

API_KEY = os.environ["GIF_KEY"]


class TestAPI(unittest.TestCase):

    def test_Trending(self):
        api = GiphyAPI()
        trending = api.callTrending(API_KEY)
        self.assertIsInstance(trending, dict)

    def test_Search(self):
        api = GiphyAPI()
        search = api.callSearch(API_KEY)
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
