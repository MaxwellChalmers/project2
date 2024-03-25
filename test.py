import os
import unittest
from unittest.mock import patch
from io import StringIO
import re

from giphyAPI import GiphyAPI
from giphyCLI import GiphyCLI
API_KEY = os.environ["GIF_KEY"]


class TestAPI(unittest.TestCase):

    def test_Trending(self):
        api = GiphyAPI(API_KEY)
        trending = api.callTrending()
        self.assertIsInstance(trending, list)
        for gif in trending:
            self.assertIsInstance(gif, dict)
            self.assertIn("bitly_gif_url", gif)
            self.assertIn("title", gif)
            self.assertIn("images", gif)
            self.assertIsInstance(gif["images"], dict)
            self.assertIn("original", gif["images"])
            self.assertIsInstance(gif["images"]["original"], dict)
            self.assertIn("url", gif["images"]["original"])

    def test_Search(self):
        api = GiphyAPI(API_KEY)
        search = api.callSearch()
        api.storeJSON(api.callSearch(query="A", limit=20), "A")
        api.openJSON("A" )
        self.assertIsInstance(search, list)
        for gif in search:
            self.assertIsInstance(gif, dict)
            self.assertIn("bitly_gif_url", gif)
            self.assertIn("title", gif)
            self.assertIn("images", gif)
            self.assertIsInstance(gif["images"], dict)
            self.assertIn("original", gif["images"])
            self.assertIsInstance(gif["images"]["original"], dict)
            self.assertIn("url", gif["images"]["original"])

    
# CLI testing courtesy of chatGPT
# this needs to be changed so the small tests are legit with dumby responces from 
# the API, I think the best way to do this is to save the json as a file somewhere and create a method that returns the list of dicts
# from those files, this can also be used later on improve the ransom function, aka memozize the letter gifs and to prune non letter 
# gifs away from the json in order to produce longer and better ransom notes
class TestGiphyCLI(unittest.TestCase):

    
    def setUp(self):
        # Create a GiphyCLI instance with a mock API key
        self.giphy_cli = GiphyCLI(API_KEY)

    @patch('sys.stdout', new_callable=StringIO)
    def test_trending_print_output(self, mock_stdout):
        # Test the output printed by the trending method
        self.giphy_cli.trending(limit=7)
        output = mock_stdout.getvalue()

        
        pattern = r'\d+\) .+ \(http[s]?://.+?\)\n'
        self.assertTrue(re.match(pattern, output))

        self.assertEqual(output.count('\n'), 7)
       
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_print_output(self, mock_stdout):
        # Test the output printed by the search method
        self.giphy_cli.search(query="cats", limit=7)
        output = mock_stdout.getvalue()
        self.assertTrue(output)  # Ensure that some output is printed
        pattern = r'\d+\) .+ \(http[s]?://.+?\)\n'
        self.assertTrue(re.match(pattern, output))
        self.assertEqual(output.count('\n'), 7)

    @patch('sys.stdout', new_callable=StringIO)
    def test_ransom_print_output(self, mock_stdout):
        # Test the output printed by the ransom method
        self.giphy_cli.ransom("test_message")
        output = mock_stdout.getvalue()
        self.assertTrue(output)  # Ensure that some output is printed

        # Define the regex pattern for the expected output
        pattern = r'!\[.\]\(http[s]?://.+?\)'
        
        # Assert that the output matches the regex pattern
        self.assertTrue(re.match(pattern, output))

        # Assert that the number of lines matches the expected count
        # We count the number of lines by splitting the output by '_'
        expected_lines = len("test_message".split('_'))
        self.assertEqual(output.count('\n'), expected_lines)

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
