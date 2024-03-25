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
    # cli.trending()
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
    # cli.search(limit=count)
    cli.search(markdown=markdown, limit=count, query=query, lucky=lucky)
    # cli.search(query="Dance Party", markdown=True, limit=50)


@gif.command()
@click.argument("message")
def ransom(message):
    cli = GiphyCLI(API_KEY)
    cli.ransom(message)
    
def main():
    gif()
