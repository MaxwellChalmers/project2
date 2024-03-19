import os

import click

from giphyCLI import GiphyCLI


API_KEY = os.environ["GIF_KEY"]


searchUrl = "https://api.giphy.com/v1/gifs/search?"
trendingUrl = "https://api.giphy.com/v1/gifs/trending?"


@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
def trending():
    print("trending subcommand called!")
    cli = GiphyCLI(API_KEY)
    cli.trending()
    cli.trending(markdown=True)


# giphy_api = GiphyAPI()
# resp = giphy_api.callTrending(API_KEY, 1)
# info = resp["data"][0]
# print(info.keys())
# url = info["bitly_gif_url"]
# title = info["title"]
# print("1) " + title + " (" + url + ")")



@gif.command()
<<<<<<< HEAD


@click.argument("query")
@click.option("--count", default = 5)
@click.option("--markdown", is_flag=True, default=False, 
              help="sends the gif in markdown format")
@click.option("--lucky", is_flag=True, default=False, 
              help="sends only the first result" )
def search(count, markdown, lucky, query):
=======
def search():
>>>>>>> parent of c2e836f (click options)
    print("search subcommand called!")
    cli = GiphyCLI(API_KEY)
    cli.search()
    cli.search(markdown=True)
    cli.search(query="Dance Party", markdown=True, limit=50)



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
