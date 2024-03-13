import os

import click

from giphyAPI import GiphyAPI

API_KEY = os.environ["GIF_KEY"]


searchUrl = "https://api.giphy.com/v1/gifs/search?"
trendingUrl = "https://api.giphy.com/v1/gifs/trending?"


@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
def trending():
    print("trending subcommand called!")
    giphy_api = GiphyAPI()
    resp = giphy_api.callTrending(API_KEY, 1)
    info = resp["data"][0]
    print(info.keys())
    url = info["bitly_gif_url"]
    title = info["title"]
    print("1) " + title + " (" + url + ")")


@gif.command()
def search():
    giphy_api = GiphyAPI()
    print("search subcommand called!")
    resp = giphy_api.callSearch(API_KEY)
    info = resp["data"][0]
    print(info.keys())
    url = info["bitly_gif_url"]
    title = info["title"]
    print("1) " + title + " (" + url + ")")


if __name__ == "__main__":
    gif()

    # apiCall = (
    #   "https://api.giphy.com/v1/gifs/trending?api_key="
    #  + API_KEY
    # + "&limit=1&offset=0&rating=g"
    # )

    # resp = requests.get(apiCall)

    # gify = resp.json()

    # print(gify.keys())

    # data = gify.get("data").pop()
    # for k in data.keys():
    # print(k + " = " + str(data.get(k)) + "\n")
