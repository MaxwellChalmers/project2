import os
import re
import unittest
from io import StringIO
from unittest.mock import patch

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
        api.openJSON("A")
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


# CLI testing code courtesy of chatGPT
class TestGiphyCLI(unittest.TestCase):

    def setUp(self):
        # Create a GiphyCLI instance with a mock API key
        self.giphy_cli = GiphyCLI(API_KEY)

    @patch("sys.stdout", new_callable=StringIO)
    def test_trending_print_output(self, mock_stdout):
        # Test the output printed by the trending method
        self.giphy_cli.trending(limit=7)
        output = mock_stdout.getvalue()

        pattern = r"\d+\) .+ \(http[s]?://.+?\)\n"
        self.assertTrue(re.match(pattern, output))

        self.assertEqual(output.count("\n"), 7)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_print_output(self, mock_stdout):
        # Test the output printed by the search method
        self.giphy_cli.search(query="cats", limit=7)
        output = mock_stdout.getvalue()
        self.assertTrue(output)  # Ensure that some output is printed
        pattern = r"\d+\) .+ \(http[s]?://.+?\)\n"
        self.assertTrue(re.match(pattern, output))
        self.assertEqual(output.count("\n"), 7)

    @patch("sys.stdout", new_callable=StringIO)
    def test_ransom_print_output(self, mock_stdout):
        # Test the output printed by the ransom method
        self.giphy_cli.ransom("AAAA_BBBB_CCCC")
        output = mock_stdout.getvalue()
        self.assertTrue(output)  # Ensure that some output is printed

        # Define the regex pattern for the expected output
        pattern = r"!\[.\]\(http[s]?://.+?\)"

        # Assert that the output matches the regex pattern
        self.assertTrue(re.match(pattern, output))

        # Assert that the number of lines matches the expected count
        # We count the number of lines by splitting the output by '_'
        expected_lines = len("test_message".split("_")) + 1
        self.assertEqual(output.count("\n"), expected_lines)

    @patch("sys.stdout", new_callable=StringIO)
    def test_trending_print_output_small(self, mock_stdout):
        # Test the output printed by the trending method
        self.giphy_cli.trending(cached=True)
        output = mock_stdout.getvalue()

        pattern = r"\d+\) .+ \(http[s]?://.+?\)\n"
        self.assertTrue(re.match(pattern, output))

        self.assertEqual(output.count("\n"), 20)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_print_output_small(self, mock_stdout):
        # Test the output printed by the search method
        self.giphy_cli.search(cached=True)
        output = mock_stdout.getvalue()
        self.assertTrue(output)  # Ensure that some output is printed
        pattern = r"\d+\) .+ \(http[s]?://.+?\)\n"
        self.assertTrue(re.match(pattern, output))

    def test_trending_markdown_small(self):
        # Test the output format of the trending method with markdown flag (small test)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.giphy_cli.trending(markdown=True, cached=True)
            output = mock_stdout.getvalue()

            # Assert that the output is in markdown format
            pattern = r"\d+\) !\[.+?\]\(http[s]?://.+?\)"
            self.assertTrue(re.match(pattern, output))

            # Assert that the number of lines matches the expected count
            self.assertEqual(output.count("\n"), 20)

    def test_trending_markdown_large(self):
        # Test the output format of the trending method with markdown flag (large test)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.giphy_cli.trending(markdown=True)
            output = mock_stdout.getvalue()

            # Assert that the output is in markdown format
            pattern = r"\d+\) !\[.+?\]\(http[s]?://.+?\)"
            self.assertTrue(re.match(pattern, output))

            # Optionally, further assertions on the content and structure of the output

    def test_search_lucky_small(self):
        # Test the output format of the search method with lucky flag (small test)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.giphy_cli.search(lucky=True, cached=True)
            output = mock_stdout.getvalue()

            # Assert that the output contains only one result
            self.assertEqual(output.count("\n"), 1)

    def test_search_lucky_large(self):
        # Test the output format of the search method with lucky flag (large test)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.giphy_cli.search(lucky=True)
            output = mock_stdout.getvalue()

            # Assert that the output contains only one result
            self.assertEqual(output.count("\n"), 1)


if __name__ == "__main__":
    unittest.main()
