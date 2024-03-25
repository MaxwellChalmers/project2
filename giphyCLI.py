import random

from giphyAPI import GiphyAPI


class GiphyCLI:

    def __init__(self, KEY):
        self.API_KEY = KEY

    # limit = 1 == lucky = True  JK I was wrong ignore this comment XD

    def trending(self, limit=5, markdown=False, lucky=False, cached=False):
        if limit > 50:
            print("The maximum number of results is 50, setting limit to 50")
            limit = 50
        api = GiphyAPI(self.API_KEY)
        gifs = api.callTrending(limit=limit)
        if cached:
            gifs = api.cachedJSON()
        for i in range(len(gifs)):
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

    def search(
        self, query="cats", limit=5, markdown=False, lucky=False, cached=False
    ):
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

        if cached:
            gifs = api.cachedJSON()
        if lucky:
            gifs = gifs[:1]

        for i in range(len(gifs)):
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

    # ONLY CAPS LOCK LETTERS AND _ AS INPUT OR THIS WILL BREAK
    def ransom(self, message):
        api = GiphyAPI(self.API_KEY)

        rMessage = ""
        for c in message:
            if c == "_":
                rMessage += "\n"
            else:
                letterGifs = api.openJSON("letters/" + c)
                gif = random.choice(letterGifs)
                url = gif["images"]["fixed_height_small"]["url"]
                rMessage += "![" + c + "](" + url + ")"
        print(rMessage)
