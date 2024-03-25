from giphyAPI import GiphyAPI


class GiphyCLI:

    def __init__(self, KEY):
        self.API_KEY = KEY

    # limit = 1 == lucky = True  JK I was wrong ignore this comment XD

    

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
            if lucky : number = ""
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
            if lucky : number = ""
            if markdown:
                print(number + "![" + title + "](" + url + ")")
            else:
                print(number  + title + " (" + bitlyUrl + ")")

    def ransom(self, message):
        api = GiphyAPI(self.API_KEY)

        rMessage = ""
        for c in message:
            if (c == "_"): 
                rMessage += "\n"
            else:
                letterGif = api.callSearch(query=c, limit=1)
                gif = letterGif[0]
                #title = gif["title"]
                url = gif["images"]["fixed_height_small"]["url"]
                rMessage += ("![" + c + "](" + url + ")") 
        print(rMessage)
    