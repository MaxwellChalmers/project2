import os
import click
import requests

API_KEY = os.environ["GIF_KEY"]
searchUrl = "https://api.giphy.com/v1/gifs/search?"
trendingUrl = "https://api.giphy.com/v1/gifs/trending?"


class GiphyCLI:

    def __init__(self, KEY):
        self.API_KEY = KEY

    def trending(self, limit=5, markdown=False, lucky=False):
        if limit > 50:
            print("The maximum number of results is 50, setting limit to 50")
            limit = 50
        api = GiphyAPI(self.API_KEY)
        gifs = api.callTrending(limit=limit)
        for i in range(limit):
            gif = gifs[i]
            bitlyUrl = gif["bitly_gif_url"]
            title = gif["title"]
            url = gif["images"]["original"]["url"]
            number = str(i + 1) + ") "
            if lucky:
                number = ""
            if markdown:
                print(number + "![" + title + "](" + url + ")")
            else:
                print(number + title + " (" + bitlyUrl + ")")

    def search(self, query="cats", limit=5, markdown=False, lucky=False):
        if len(query) > 50:
            print("There is a char limit of 50 on search terms")
            print("I will shorten your search to the limit")
            print("trying again with a shorter query recomended!")
            query = query[:50]
        if limit > 50:
            print("The maximum number of results is 50, setting limit to 50")
            limit = 50

        api = GiphyAPI(self.API_KEY)
        gifs = api.callSearch(query=query, limit=limit)

        for i in range(limit):
            gif = gifs[i]
            bitlyUrl = gif["bitly_gif_url"]
            title = gif["title"]
            url = gif["images"]["original"]["url"]
            number = str(i + 1) + ") "
            if lucky:
                number = ""
            if markdown:
                print(number + "![" + title + "](" + url + ")")
            else:
                print(number + title + " (" + bitlyUrl + ")")

    def ransom(self, message):
        api = GiphyAPI(self.API_KEY)

        rMessage = ""
        for c in message:
            if c == "_":
                rMessage += "\n"
            else:
                letterGif = api.callSearch(query=c, limit=1)
                gif = letterGif[0]
                url = gif["images"]["fixed_height_small"]["url"]
                rMessage += ("![" + c + "](" + url + ")")
        print(rMessage)


class GiphyAPI:

    def __init__(self, KEY):
        self.API_KEY = KEY

    @staticmethod
    def buildSearchCall(
            KEY,
            query="cats",
            limit=5,
            offset=0,
            rating="g",
            lang="en",
            random_id="bob",
            bundle="messaging_non_clips",
    ):
        searchParams = {
            "api_key": KEY,
            "q": query,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "lang": lang,
            "random_id": random_id,
            "bundle": bundle,
        }
        return searchParams

    @staticmethod
    def buildTrendingCall(
            KEY,
            limit=5,
            offset=0,
            rating="g",
            random_id="rob",
            bundle="messaging_non_clips",
    ):
        trendingParams = {
            "api_key": KEY,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "random_id": random_id,
            "bundle": bundle,
        }
        return trendingParams

    def callTrending(self, limit=5):
        callParams = self.buildTrendingCall(self.API_KEY, limit)
        resp = requests.get(trendingUrl, params=callParams)
        return resp.json()["data"]

    def callSearch(self, query="cats", limit=5):
        callParams = self.buildSearchCall(self.API_KEY, query, limit)
        resp = requests.get(searchUrl, params=callParams)
        return resp.json()["data"]


@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
@click.option("--count", default=5, help="the number of results")
@click.option(
    "--markdown",
    is_flag=True,
    default=False,
    help="sends the gif in markdown format",
)
@click.option(
    "--lucky", is_flag=True, default=False, help="sends only the first result"
)
def trending(count, markdown, lucky):
    print("trending subcommand called!")
    cli = GiphyCLI(API_KEY)
    if lucky:
        count = 1
    cli.trending(markdown=markdown, limit=count, lucky=lucky)


@gif.command()
@click.argument("query")
@click.option("--count", default=5)
@click.option(
    "--markdown",
    is_flag=True,
    default=False,
    help="sends the gif in markdown format",
)
@click.option(
    "--lucky", is_flag=True, default=False, help="sends only the first result"
)
def search(count, markdown, lucky, query):
    print("search subcommand called!")
    cli = GiphyCLI(API_KEY)
    if lucky:
        count = 1
    cli.search(markdown=markdown, limit=count, query=query, lucky=lucky)


@gif.command()
@click.argument("message")
def ransom(message):
    cli = GiphyCLI(API_KEY)
    cli.ransom(message)


def main():
    gif()


if __name__ == "__main__":
    main()
